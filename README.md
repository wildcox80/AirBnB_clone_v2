<h1 align="center">0x02. AirBnB clone - MySQL</h1>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

[![Twitter Wilder](https://img.shields.io/twitter/follow/WildsRincon?label=Wilder_Rincon&style=social)](https://twitter.com/WildsRincon)
[![Twitter Wilder](https://img.shields.io/twitter/follow/hikari_perdomo?label=Lily_Perdomo&style=social)](https://twitter.com/hikari_perdomo)


## Background Context

Environment variables will be your best friend for this project!

- HBNB_ENV: running environment. It can be “dev” or “test” for the moment (“production” soon!)
- HBNB_MYSQL_USER: the username of your MySQL
- HBNB_MYSQL_PWD: the password of your MySQL
- HBNB_MYSQL_HOST: the hostname of your MySQL
- HBNB_MYSQL_DB: the database name of your MySQL
- HBNB_TYPE_STORAGE: the type of storage used. It can be “file” (using FileStorage) or db (using DBStorage)

## Resources :notebook:

Read or watch:

- [cmd module](https://intranet.hbtn.io/rltoken/stklU8CC2E0LoJsq32OCOA)
- [packages](https://intranet.hbtn.io/rltoken/3UbebGAqbj8yJ0k4pga9IA)
- [unittest module](https://intranet.hbtn.io/rltoken/u7l9IP_paqAZQBk3knUzDw)
- [args/kwargs](https://intranet.hbtn.io/rltoken/2RJXEts8y09PKKNR4_KZaw)
- [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/KzB5FBMl5lh3orhpWtsNVQ)
- [How To Create a New User and Grant Permissions in MySQL](https://intranet.hbtn.io/rltoken/9KO9mYoUjjq0A3grVHRUxw)
- [Jimmy’s (My)SQL Cheat Sheet](https://intranet.hbtn.io/rltoken/CdIIZi6b8uNHxJuiXK3ZTw)
- [Python3 and environment variables](https://intranet.hbtn.io/rltoken/loAjB47LzpKUqAnTnW-Ejg)
- [Object Relational Mapping with Python’s SQL Alchemy](https://intranet.hbtn.io/rltoken/sTAjV8wYaUWRw3AOCBzQrA)
- [SQLAlchemy](https://intranet.hbtn.io/rltoken/ra96sKNSpT0U_6h1V0tBNA)
- [MySQL 5.7 SQL Statement Syntax](https://intranet.hbtn.io/rltoken/rjPdi3u-uyGe53UZtqvbCA)
- [AirBnB clone - ORM from Isaac Wong, Cohort #5, ](https://intranet.hbtn.io/rltoken/QTQdlcgZudeEa_50A57ZfQ)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google:**

### General

- What is Unit testing and how to implement it in a large project
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function
- How to create a MySQL database
- How to create a MySQL user and grant it privileges
- What ORM means
- How to map a Python Class to a MySQL table
- How to handle 2 different storage engines with the same codebase
- How to use environment variables

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project: ex: for models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge cases

### SQL Scripts


- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 14.04 LTS using MySQL 5.7 (version 5.7.8-rc)
- Your files will be executed with SQLAlchemy version 1.2.x
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

### Github

There should be one project repository per group. If you clone/fork/whatever a partner’s project repository with the same name before the second deadline, you risk a 0% score.


## More Info

<p align="center"><img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step2.png" /></p>

[HBNB Storage Abstraction](https://youtu.be/fb2zxES7ROU "HBNB Storage Abstraction")


### Comments for your SQL file:

```
$ cat my_script.sql
-- first 3 students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
```
## Task :notebook:

### Mandatory :heavy_check_mark:
- Fork me if you can! 
- Bug free!
- Console improvements
- MySQL setup development 
- MySQL setup test 
- Delete object
- DBStorage - States and Cities
- DBStorage - User
- DBStorage - Place
- DBStorage - Review
- DBStorage - Amenity... and BOOM!
 
## Authors :busts_in_silhouette: 
[@Wilder Rincón - Github](https://github.com/wildcox80)
[@Luz Perdomo - Github](https://github.com/luzperdomo92)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/luzperdomo92/AirBnB_clone_v2.svg?style=plastic
[contributors-url]: https://github.com/luzperdomo92/AirBnB_clone_v2/graphs/contributors
[license-shield]: https://img.shields.io/github/license/wildcox80/holberton-system_engineering-devops.svg?style=plastic
[license-url]: https://github.com/wildcox80/holberton-system_engineering-devops/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=plastic&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/wildsrincon
