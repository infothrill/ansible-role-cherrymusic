# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_cherrymusic_conf_file(host):
    f = host.file('/home/cherrymusic/.config/cherrymusic/cherrymusic.conf')

    assert f.exists
    assert f.user == 'cherrymusic'
