Ansible role: cherrymusic
=========================

Installs [cherrymusic](http://www.fomori.org/cherrymusic/) on a Linux system.

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
