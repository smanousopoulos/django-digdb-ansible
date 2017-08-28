# django-digdb-ansible 
A collection of Ansible roles for setting up a DigDB Django web app. See https://github.com/smanousopoulos/django-digdb

Requirements
------------
- Ubuntu linux (tested on 16.04)
- Ansible 

Quick start
-----------

1. Setup variables in roles/django/vars/main.yml. Check roles/django/defaults/main.yml for default values

2. Create hosts file. See hosts-example for reference 

3. Run `ansible-playbook -i hosts site.yml`
