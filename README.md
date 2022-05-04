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
    * http://localhost:8060/catalog/
    * http://localhost:8060/katalog/
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

1. Add `SECRET_KEY` to Heroku Config Variables:
`heroku config:set SECRET_KEY=<value>` # Didn't work. Needed to use Heroku website for some reason.

1. `git push heroku main`

1. `heroku run python manage.py createsuperuser`

1. Edit code:
    * https://thinkster.io/tutorials/configuring-django-settings-for-production

1. `heroku config:set DJANGO_SETTINGS_MODULE='locallibrary.settings.production'`

1. Verify DEBUG=False in prod:
    1. `heroku login`
    1. `heroku run python manage.py shell`
    1. `from django.conf import settings as s`
    1. `print(s.DEBUG)`

### Django Tutorial Part 2: Creating a skeleton website
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website

* New concepts:
    * [RedirectView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#redirectview)

### Django Tutorial Part 3: Using models
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

