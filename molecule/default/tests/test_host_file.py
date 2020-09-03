#!/usr/bin/env python3
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_hosts_file(host):
    f = host.file('/root/hosts')

    # All of these tests should pass
    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o644'
    assert f.contains('127.0.0.1 molecule.example.com')
