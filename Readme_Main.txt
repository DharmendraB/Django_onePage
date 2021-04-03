1-#Install Python First (download and install it on PC)
2-#Install & Create Virtual Environment for Django project
pip install virtualenv

#create virtualenv
virtualenv -p python3 venv2021 [or] py -m venv venv2021

#Active virtualenv
venv2021\Scripts\activate.bat 
or
D:\vs_code\Django2021\mysite2021>venv2021\Scripts\activate.bat
 [A] Yes to All
 A
 
#if not create or Active Virtualenv then run this command[Set-ExecutionPolicy unrestricted] on Windows PowerShell
PS C:\WINDOWS\system32> Set-ExecutionPolicy unrestricted

#Install Django
py -m pip install Django

#Create Django project
django-admin startproject mysite2021

#Run Django project
python manage.py runserver

[The install worked successfully! Congratulations!]

#create Django App (onepage)
$ cd mysite2021
python manage.py startapp onepage

#Create Table and database 
$ python manage.py makemigrations
$ python manage.py migrate

#Create Super User (admin user)
$python manage.py createsuperuser
{   Username (leave blank to use 'lenovo'): admin
    Email address: gohildb.dev@gmail.com
    Password: 
    Password (admin@147):  
    Username: Admin
    Password: blog@123
}

#Run Django project
python manage.py runserver

#create OnePage App [Static app]
$python manage.py startapp onepage

#create Blog App [Dynamic App]
$python manage.py startapp Blog





