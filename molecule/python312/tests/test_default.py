import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_virtualenv(host):
    venv = '/opt/test/python3-virtualenv'
    assert host.check_output(venv + '/bin/python --version').startswith('Python 3.12')
