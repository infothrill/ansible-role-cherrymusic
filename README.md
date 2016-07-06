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

	cherrymusic_fetch_album_art: "True"

Wether to fetch album art.

Dependencies
------------

None.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: infothrill.cherrymusic, cherrymusic_fetch_album_art: "False" }

License
-------

MIT / BSD

Author Information
------------------

This role was created in 2016 by Paul Kremer.
