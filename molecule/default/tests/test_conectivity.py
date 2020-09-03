#!/usr/bin/env python3
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_hosts_file(host):
    example = host.addr('localhost')

    assert example.is_resolvable
    assert example.is_reachable
    assert '127.0.0.1' in example.ipv4_addresses
