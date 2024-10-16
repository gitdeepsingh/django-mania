### django-mania:: Getting Started

##### globally
```
pip3 install pipenv
```

##### inside project dir

We now will work , install apps, run servers, create apps in virtual env pipenv provides. To enter into the virtual env, run below command
```
pipenv shell
```
```
django-admin startproject djangomania . 
```
- creates manage.py- a wrapper around django-admin. Going forward we will be using manage.py instead of django-admin

- we can try running django admin runserver; this will give error as it does not include project settings, but manage.py do. So we run
```
python manage.py runserver
```
- Check out djangomania/settings.py to see INSTALLED_APPS

make sure we are still i virtula env, then create a new app, and register that under INSTALLED_APPS under djangomania/settings.py
```
python manage.py startapp playground
```

we can create multiple apps inside a project. Eacvh app can serve different purposes related to that project.
 
##### views in django

 - open playground/views.py (view handles data exchange, requests and returns response)
 - create a view (request) and map it to a url
 - start server and hit http://127.0.0.1:8000/playground/hello/

##### templates in django
   - to render HTML on browser
   - we can replace django template engine with our preferred temnplate engine
   - we often not use django to build templates but mostly to create APIs

##### setup debug_toolbar
https://django-debug-toolbar.readthedocs.io/en/latest/installation.html 

##### restapi
 - create REST API using djangorestframework
 - to migrate models to DB tables. check restapi/migrations/0001_initial.py
 ```
 python3 manage.py makemigrations
 ```
 ```
 python3 manage.py migrate
 ```
 - above command will create db.sqlite3
 - then we create restapi/serializer.py that will transform model into json data
 - GET: http://127.0.0.1:8000/restapi/users/
 - POST: http://127.0.0.1:8000/restapi/users/create