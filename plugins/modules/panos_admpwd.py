#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright 2016 Palo Alto Networks, Inc
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: panos_admpwd
short_description: change admin password of PAN-OS device using SSH with SSH key
description:
    - Change the admin password of PAN-OS via SSH using a SSH key for authentication.
    - Useful for AWS instances where the first login should be done via SSH.
author: "Luigi Mori (@jtschichold), Ivan Bojer (@ivanbojer)"
version_added: '1.0.0'
requirements:
    - paramiko
options:
    ip_address:
        description:
            - IP address (or hostname) of PAN-OS device
        required: true
        type: str
    username:
        description:
            - username for initial authentication
        required: false
        type: str
        default: admin
    key_filename:
        description:
            - filename of the SSH Key to use for authentication
        required: true
        type: str
    newpassword:
        description:
            - password to configure for admin on the PAN-OS device
        required: true
        type: str
"""

EXAMPLES = """
# Tries for 10 times to set the admin password of 192.168.1.1 to "badpassword"
# via SSH, authenticating using key /tmp/ssh.key
- name: set admin password
  panos_admpwd:
    ip_address: "192.168.1.1"
    username: "admin"
    key_filename: "/tmp/ssh.key"
    newpassword: "badpassword"
  register: result
  until: result is not failed
  retries: 10
  delay: 30
"""

RETURN = """
status:
    description: success status
    returned: success
    type: str
    sample: "Last login: Fri Sep 16 11:09:20 2016 from 10.35.34.56.....Configuration committed successfully"
"""


import sys
import time

from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule

try:
    import paramiko

    HAS_LIB = True
except ImportError:
    HAS_LIB = False

_PROMPTBUFF = 4096


def wait_with_timeout(module, shell, prompt, timeout=60):
    now = time.time()
    result = ""
    while True:
        if shell.recv_ready():
            result += to_text(shell.recv(_PROMPTBUFF))
            endresult = result.strip()
            if len(endresult) != 0 and endresult[-1] == prompt:
                break

        if time.time() - now > timeout:
            module.fail_json(msg="Timeout waiting for prompt")

    return result


def set_panwfw_password(module, ip_address, key_filename, newpassword, username):
    stdout = ""

    ssh = paramiko.SSHClient()

    # add policy to accept all host keys, I haven't found
    # a way to retrieve the instance SSH key fingerprint from AWS
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(ip_address, username=username, key_filename=key_filename)
    shell = ssh.invoke_shell()

    # wait for the shell to start
    buff = wait_with_timeout(module, shell, ">")
    stdout += buff

    # step into config mode
    shell.send("configure\n")
    # wait for the config prompt
    buff = wait_with_timeout(module, shell, "#")
    stdout += buff

    if module.check_mode:
        # exit and close connection
        shell.send("exit\n")
        ssh.close()
        return False, "Connection test successful. Password left intact."

    # set admin password
    shell.send("set mgt-config users " + username + " password\n")

    # wait for the password prompt
    buff = wait_with_timeout(module, shell, ":")
    stdout += buff

    # enter password for the first time
    shell.send(newpassword + "\n")

    # wait for the password prompt
    buff = wait_with_timeout(module, shell, ":")
    stdout += buff

    # enter password for the second time
    shell.send(newpassword + "\n")

    # wait for the config mode prompt
    buff = wait_with_timeout(module, shell, "#")
    stdout += buff

    # commit !
    shell.send("commit\n")

    # wait for the prompt
    buff = wait_with_timeout(module, shell, "#", 120)
    stdout += buff

    if "successfully" not in buff:
        module.fail_json(msg="Error setting " + username + " password: " + stdout)

    # exit
    shell.send("exit\n")

    ssh.close()

    return True, stdout


def main():
    argument_spec = dict(
        ip_address=dict(required=True),
        username=dict(default="admin"),
        key_filename=dict(required=True),
        newpassword=dict(no_log=True, required=True),
    )
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)
    if not HAS_LIB:
        module.fail_json(msg="paramiko is required for this module")

    ip_address = module.params["ip_address"]
    if not ip_address:
        module.fail_json(msg="ip_address should be specified")
    key_filename = module.params["key_filename"]
    if not key_filename:
        module.fail_json(msg="key_filename should be specified")
    newpassword = module.params["newpassword"]
    if not newpassword:
        module.fail_json(msg="newpassword is required")
    username = module.params["username"]

    try:
        changed, stdout = set_panwfw_password(
            module, ip_address, key_filename, newpassword, username
        )
        module.exit_json(changed=changed, stdout=stdout)
    except Exception:
        x = sys.exc_info()[1]
        module.fail_json(msg=x)


if __name__ == "__main__":
    main()
