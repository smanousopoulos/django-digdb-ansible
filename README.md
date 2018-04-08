# django-digdb-ansible 
A collection of Ansible roles for setting up a DigDB Django web app. See https://github.com/smanousopoulos/django-digdb

Requirements
------------
- Ubuntu linux (tested on 16.04)
- Ansible 

Quick start
-----------

1. Setup variables in roles/django/vars/main.yml. Check roles/django/defaults/main.yml for default values

2. Copy schema file(s) in roles/django/files/schema folder

3. Create hosts file. See hosts-example for reference 

4. Run `ansible-playbook -i hosts site.yml`

Notes
-----------

Default admin username/password is admin/admin. Make sure you change the password after first login

