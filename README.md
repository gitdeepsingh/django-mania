### django-mania:: Getting Started

##### globally
pip3 install pipenv

##### inside project dir
```
pipenv shell
django-admin startproject djangomania . 
```
- creates manage.py- a wrapper around django-admin. Going forward we will be using manage.py instead of django-admin

- we can try running django admin runserver; this will give error as it does not include project settings, but manage.py do. So we run
```
python manage.py runserver
```
- Check out djangomania/settings.py to see INSTALLED_APPS