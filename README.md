Python3 Virtualenv
==================

[![Actions Status](https://github.com/ome/ansible-role-python3-virtualenv/workflows/Molecule/badge.svg)](https://github.com/ome/ansible-role-python3-virtualenv/actions)
[![Ansible Role](https://img.shields.io/badge/ansible--galaxy-python3_virtualenv-blue.svg)](https://galaxy.ansible.com/ui/standalone/roles/ome/python3_virtualenv/)

Install Python3 virtualenv dependencies and a wrapper script for the Ansible pip module.

There are multiple ways of creating Python virtualenvs including virtualenv, python3 -mvenv, but these may take different parameters.
In some situations, particularly if `ansible_python_interpreter` is set, the Ansible pip modules passes unrecognised parameters.
This role installs a wrapper script `/usr/local/bin/ome-python3-virtualenv` should work in all cases.

Role Variables
--------------
python_version: The default Python version value is 3.12, with support also available for Python 3.11.
virtualenv_basedir: Base directory where the virtual environment is located
service_name: service name, e.g. omero-server
env_name: The virtual environment name, the default value is venv3

Example Playbooks 
-----------------
    # Example for use during OMERO.server installation or upgrade
    - hosts: localhost
      roles:
      - role: ome.ansible-role-python3-virtualenv
        # Uncomment the line below to use Python 3.11. 
        # python_version: "3.11"
        virtualenv_basedir: /opt/omero/server
        service_name: omero-server

    #  Example for use during OMERO.web installation or upgrade        
    - hosts: localhost
      roles:
      - role: ome.ansible-role-python3-virtualenv
        # Uncomment the line below to use Python 3.11. 
        # python_version: "3.11"
        virtualenv_basedir: /opt/omero/web
        service_name: omero-web


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk

License
-------

BSD
