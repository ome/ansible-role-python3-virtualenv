Python3 Virtualenv
==================


[![Build Status](https://travis-ci.org/ome/ansible-role-python3-virtualenv.svg)](https://travis-ci.org/ome/ansible-role-python3-virtualenv)
[![Ansible Role TODO](https://img.shields.io/ansible/role/TODO.svg)](https://galaxy.ansible.com/ome/python3_-_virtualenv/)

Install Python3 virtualenv dependencies and a wrapper script for the Ansible pip module.

There are multiple ways of creating Python virtualenvs including virtualenv, python3 -mvenv, but these may take different parameters.
In some situations, particularly if `ansible_python_interpreter` is set, the Ansible pip modules passes unrecognised parameters.
This role installs a wrapper script `/usr/local/bin/ome-python3-virtualenv` should work in all cases.


Author Information
------------------

ome-devel@lists.openmicroscopy.org.uk

License
-------

BSD
