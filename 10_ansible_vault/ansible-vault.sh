#! /bin/bash

# Ansible-Vault Documentation
# https://docs.ansible.com/ansible/latest/cli/ansible-vault.html

# Synopsis
# usage: ansible-vault [-h] [--version] [-v]
#                  {create,decrypt,edit,view,encrypt,encrypt_string,rekey}

# Encrypt inventory file
ansible-vault encrypt inventory.txt

# View encrypted inventory file
ansible-vault view inventory.txt

# Create encrypted inventory file
ansible-vault create inventory.txt

# Edit encrypted inventory file
ansible-vault edit inventory.txt

# Run playbook with encrypted inventory file
ansible-playbook playbook.yml -i inventory.txt --ask-vault-pass

# Run playbook with encrypted inventory file - vault password in password file
ansible-playbook playbook.yml -i inventory.txt --vault-password-file ~/.vault_pass.txt

# Run playbook with encrypted inventory file - vault password passed in by a program
ansible-playbook playbook.yml -i inventory.txt --vault-password-file ~/.vault_pass.py