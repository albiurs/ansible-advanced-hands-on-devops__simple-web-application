MySQL DB Deployment 
===================

Installation of default-mysql-server and default-mysql-client.
Complete deployment of database, root and user accounts.


Requirements
------------

-


Role Variables
--------------

db_name: NameOfDbToDeoploy
db_user: dbUserName
db_password: PasswordOfDbUser
db_root_password: DbRootPssword


Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.


Example Playbook
----------------

---
- name: Deploy MySQL
  hosts: anyTargetHosts
  roles:
    - mysql_db


License
-------

GNU GENERAL PUBLIC LICENSE Version 3


Author Information
------------------

Urs Albisser, Publicept, https://publicept.ch
