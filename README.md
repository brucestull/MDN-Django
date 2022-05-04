## Django Library Application

### Resources:
* [Django Web Framework (Python)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
* https://github.com/brucestull/MDN-Django
* https://github.com/brucestull/MDN-Django/projects/2

### Commands and virtual environment:
* Virtual environment: `C:\Users\Bruce\.virtualenvs\MDN-Django-I7w_2BnS\Scripts\activate.ps1`
* Server start: `python manage.py runserver 8060`
* Routes:
    * http://localhost:8060/
    * http://localhost:8060/admin/
* Production routes:
    * https://bunbuns-books.herokuapp.com/
    * https://git.heroku.com/bunbuns-books.git


### Project deployed to Heroku:

1. `heroku login`

1. `heroku create bunbuns-books`

1. `git remote -v`
    ```
    heroku  https://git.heroku.com/bunbuns-books.git (fetch)
    heroku  https://git.heroku.com/bunbuns-books.git (push)
    origin  https://github.com/brucestull/MDN-Django.git (fetch)
    origin  https://github.com/brucestull/MDN-Django.git (push)
    ```

1. `pipenv install django-on-heroku gunicorn`

1. Modify `locallibrary/settings.py`:
    ```
    import django_on_heroku
    django_on_heroku.settings(locals())
    ```

1. Create `locallibrary/Procfile`:
    ```
    web: gunicorn locallibrary.wsgi
    release: python manage.py migrate users && python manage.py migrate
    ```

### Django Tutorial Part 2: Creating a skeleton website

1. 


### Second Phase