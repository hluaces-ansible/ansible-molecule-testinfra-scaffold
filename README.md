# What is this?

A quick repo I made to illustrate how Molecule for Ansible works with Testinfra as a verifier.

You can use this as a scaffold to create testing plans for your roles, playbooks or collections.

In the near future I'll try to add a more thoroughly documented repository.

# What do I need to make it work?

For this particular example you'll need a running Docker installation.

Also, the following pip3 packages are needed. Most of them provide binaries that should be present on your `$PATH`, so configure your virtualenvs accordingly.

- ansible (v2.9.x preferred)
- molecule (v3 or higher)
- flake8
- ansible-lint
- yamllint
- testinfra
- docker

# How to test it?

Molecule has several test matrixes. I'm just naming a few of them for simplicity's sake:

- `molecule lint`: simply lint all the files in this repo (`.py` and `.yml`) using flake8, ansible-lint and yamllint.
- `molecule converge`: creates the Docker images used in these tests and provisions them with the `molecule/default/converge.yml` playbook. The generated containers won't be destroyed and can be inspected after the process ends.
- `molecule verify`: executes all the testinfra tests on the running containers. You should use `molecule converge` prior to this.
- `molecule test`: this pretty much executes all possible tests in order and destroys the containers upon ending. This is what you usually want in your pipelines.
- `molecule destroy`: Use this when you are done and want to clear molecule's cache and any created running containers.

All of the previous commands should be executed from this repository root directory.

# How to run these in pipelines?

You should either use Docker in Docker or a testing environment with shell capabilities able to use docker.

# Docker is not enough for my testing!

Molecule allows for more platform options (cloud images, KVM, amongst them). This POC is not covering them ATM.

# Contributing

Feel free to drop any request or issue it you have any doubts or you feel this POC could be improved.

# Would you like to know more?

- [Molecule documentation](https://molecule.readthedocs.io/en/latest/)
- [Testinfra documentation](https://testinfra.readthedocs.io/en/latest/)
