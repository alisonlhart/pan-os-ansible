### [2.17.3](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.17.2...v2.17.3) (2023-07-11)


### Bug Fixes

* **eda:** Make `custom_logger` argument optional ([#456](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/456)) ([49ed307](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/49ed3079e646072401075b68da07bd0799818e42))
* **panos_admpwd:** Fix success criteria and update example in docs ([#457](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/457)) ([9ecdb65](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/9ecdb65bb88db4528cbae7221f4ea930a62e49c9))
* **panos_bgp_peer_group:** Fix for IBGP export next-hop options ([#459](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/459)) ([9489fa2](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/9489fa25b6f3f898aa6c080d6f1676c1747e073f))
* **panos_ike_crypto_profile:** Update DH group choices ([#461](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/461)) ([8194318](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/8194318c496f192e9eb63526cc7a13df4f1ca493))
* **panos_ipsec_profile:** Update DH group choices ([#462](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/462)) ([1798a3b](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/1798a3b0ab7b4cf415d44df0c13d96cec5111252))
* **panos_software:** Modify valid sequence for downloads only ([#463](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/463)) ([214c4bb](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/214c4bb9f2c7a9421694f808ba8f0f83e635dca5))

### [2.17.2](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.17.1...v2.17.2) (2023-06-28)


### Bug Fixes

* **panos_ike_crypto_profile:** Fixed auth type `non-auth` for IKE profile ([#418](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/418)) ([0a2abe8](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/0a2abe80055982ddf2035d24f9adde36ce226a55))

### [2.17.1](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.17.0...v2.17.1) (2023-06-23)


### Bug Fixes

* Tox-compliant EDA code, and Tox checks in CI ([#453](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/453)) ([9a50c9b](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/9a50c9bb5e841ddfe0eeca7ea9021eb289e0e5db))
* **eda:** Move EDA plugin to correct path ([#444](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/444)) ([dc524e9](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/dc524e93b87f0163cc3019636617198a59ebf51f))

## [2.17.0](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.16.0...v2.17.0) (2023-06-14)


### Features

* **panos_export:** Create directory if it doesn't exist ([#434](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/434)) ([9422af0](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/9422af0b17d1d534c73391cc95640ad6dea3d824))
* **panos_import:** Add private key blocking to keypair import ([#417](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/417)) ([3fd5bac](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/3fd5bacdd0324ab636a0456f19993d588f900dcb))
* **panos_software:** name config load option ([#398](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/398)) ([378d5a6](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/378d5a679463918dd2e635f20ba0b086f50feb97))

## [2.16.0](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.15.0...v2.16.0) (2023-05-12)


### Features

* **event_driven_ansible:** New plugin for event-driven ansible ([c4b627d](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/c4b627dac496f7233ca6016aa85f60c8378ada41))
* **panos_log_forwarding_profile_match_list:** Add decryption log-type to log forwarding ([#429](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/429)) ([a1dab0a](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/a1dab0a2b14f3ba1fa566161ce1a3f28819683cb))

## [2.15.0](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.14.0...v2.15.0) (2023-04-27)


### Features

* **panos_http_profile:** Decrypt and GP for HTTP profiles ([#427](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/427)) ([f6c86d9](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/f6c86d9d592ea7e4b17d7e4186ffb18c2349e359))

## [2.14.0](https://github.com/PaloAltoNetworks/pan-os-ansible/compare/v2.13.3...v2.14.0) (2023-04-26)


### Features

* **panos_aggregate_interface:** Fast failover for LACP on aggregate network interfaces ([#423](https://github.com/PaloAltoNetworks/pan-os-ansible/issues/423)) ([ad89bcd](https://github.com/PaloAltoNetworks/pan-os-ansible/commit/ad89bcd46ec46b5b1cb6d6363f8f13db0ba5655f))

# Changelog

Details can be found [here](https://github.com/PaloAltoNetworks/pan-os-ansible/releases)
