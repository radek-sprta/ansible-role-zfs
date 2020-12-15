# Ansible Role: ZFS [![Ansible Role](https://img.shields.io/ansible/role/52311)](https://galaxy.ansible.com/radek_sprta/zfs) [![GitHub tag (latest SemVer)](https://img.shields.io/github/v/tag/radek-sprta/ansible-role-zfs)](https://gitlab.com/radek-sprta/ansible-role-zfs/-/tags) [![Ansible Role](https://img.shields.io/ansible/role/d/52311)](https://galaxy.ansible.com/radek_sprta/zfs) [![Ansible Role](https://img.shields.io/ansible/quality/52311)](https://galaxy.ansible.com/radek_sprta/zfs) [![Pipeline status](https://gitlab.com/radek-sprta/ansible-role-zfs/badges/master/pipeline.svg)](https://gitlab.com/radek-sprta/ansible-role-zfs/commits/master)

Install ZFS, configure zpool and datasets.

## Role Variables

List of variables from `defaults/main.yml`.

    zfs_pools: {}

ZFS pools to define. Example configration of an encrypted pool might look like this:

    zfs_pools:
      tank:
        devices: []
        ashift: 13
        compression: zstd
        encryption: aes-256-gcm
        keylocation: prompt
        keyformat: passphrase
        passphrase: mysecret

ZFS datasets are defined in the following:

    zfs_datasets: {}

All parameters are passed as extra options, so an example dataset configuration might look like this:

    zfs_datasets:
      tank/media:
        mountpoint: /media
        records_size: 1M
      tank/photos:
        mountpoint: /mnt/photos
        compression: off

## Example Playbook

```yaml
- hosts: all

  vars:
    zfs_pools:
      tank:
        devices: []
        ashift: 13
        compression: zstd
        encryption: aes-256-gcm
        keylocation: prompt
        keyformat: passphrase
        passphrase: mysecret
    zfs_datasets:
      tank/media:
        mountpoint: /media
        records_size: 1M
      tank/photos:
        mountpoint: /mnt/photos
        compression: off
    
  roles:
     - radek-sprta.zfs
```

## License

MIT

## Author Information

Radek Sprta <mail@radeksprta.eu>
