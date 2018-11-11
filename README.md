Ansible role: cherrymusic
=========================

[![Build Status](https://img.shields.io/travis/infothrill/ansible-role-cherrymusic/master.svg?label=travis_master)](https://travis-ci.org/infothrill/ansible-role-cherrymusic)
[![Updates](https://pyup.io/repos/github/infothrill/ansible-role-cherrymusic/shield.svg)](https://pyup.io/repos/github/infothrill/ansible-role-cherrymusic/)
[![Ansible Role](https://img.shields.io/ansible/role/10778.svg)](https://galaxy.ansible.com/infothrill/cherrymusic/)


An [Ansible](http://www.ansible.com) role to install [cherrymusic](http://www.fomori.org/cherrymusic/) on a Linux system.

Requirements
------------

Nothing specific so far.

Role Variables
--------------

Available variables are listed below, along with default values (see defaults/main.yml):

	cherrymusic_basedir: /cherrymusic

The path were the music files are located (or where symlinks to the actual music files are located).

	cherrymusic_fetch_album_art: true

Wether to fetch album art.

	cherrymusic_user: "cherrymusic"

The unix user for running cherrymusic.

	cherrymusic_update: false

Wether "cherrymusic --update" should be run.

	cherrymusic_port: 8080

The port to listen on.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: infothrill.cherrymusic, cherrymusic_fetch_album_art: false }

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2016 by Paul Kremer.
