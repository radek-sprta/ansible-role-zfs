# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2022-07-07

### Added

- Validate arguments

### Removed

- Support for Ansible 2.9 and lower.

### Changed

- Change pool and dataset definition format from dictionary to list of
  dictionaries, so it can support dashes in names.

## 0.1.0 - 2020-12-11

### Added

- First public version. Install ZFS, support creation of zpools and datasets.

[0.2.0]: https://gitlab.com/radek-sprta/ansible-role-node-exporter/compare/0.1.0...0.2.0
