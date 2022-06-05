## Dezzi's Depot Library
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
    * http://localhost:8060/catalog/the-word/

* Production routes:
    * https://dezzis-depot.herokuapp.com/
    * https://git.heroku.com/dezzis-depot.git
    
* Dashboard:
    * https://dashboard.heroku.com/apps


### Project deployed to Heroku:

1. `heroku login`

1. `heroku create dezzis-depot`

1. `git remote -v`
    ```
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
* [MDN Part 2](https://github.com/brucestull/MDN-Django/issues/8)
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/skeleton_website

* New concepts:
    * [RedirectView](https://docs.djangoproject.com/en/4.0/ref/class-based-views/base/#redirectview)

### Django Tutorial Part 3: Using models
* [MDN Part 3](https://github.com/brucestull/MDN-Django/issues/10)
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Models

* New concepts:
    * [ManyToManyField](https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_many/)

### Django Tutorial Part 4: Django admin site
* [MDN Part 4](https://github.com/brucestull/MDN-Django/issues/16)
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site

* New concepts:
    * [ModelAdmin](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#modeladmin-objects)
        * [list_display](https://stackoverflow.com/a/59587324/10958667)
        * [list_filter](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Admin_site#add_list_filters)
        * [TabularInline](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#django.contrib.admin.TabularInline)
    * [@admin.register(Model)](https://docs.djangoproject.com/en/4.0/ref/contrib/admin/#the-register-decorator)

### Django Tutorial Part 5: Creating our home page
* [MDN Part 5](https://github.com/brucestull/MDN-Django/issues/21)
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page

* New concepts:
    * [APP_DIRS](https://docs.djangoproject.com/en/4.0/topics/templates/#configuration)
    * Can use `catalog.views.index` for indeas on how to process user input for searches.
    * Git checkout commit and create branch:
        * `git branch before-index-page 480a32c059c5e843e59d714cb571dfd69ca559c2`
    * Git force local branch to match remote:
        * `git fetch origin`
        * `git reset --hard origin/branch-name`
    * Reset Heroku repo:
        * `heroku plugins:install heroku-repo`
        * `heroku repo:reset --app appname`
    * Push non-main branch:
        * `git push heroku testbranch:main`

### Django Tutorial Part 5: Creating our home page (REDO)
* [MDN Part 5](https://github.com/brucestull/MDN-Django/issues/23)
* https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Home_page


* New concepts:
    * 

#### Templates example:
* `<a href="{% url 'catalog:the-word' %}">The Word</a>`
* `common.py`:
    ```
    TEMPLATES = [
        {
            ...
            'DIRS': [ BASE_DIR / 'templates'],
            'APP_DIRS': True,
            ...
        },
    ]
    ```
* Template location:
`BASE_DIR\templates\catalog\the_word.html`
* View:
    ```
    def the_word(request):
        context = {
            'the_word': 'potatoes'
        }
        return render(request, 'catalog/the_word.html', context=context)
    ```
* URL:
    ```
        ...
        path('the-word/', views.the_word, name='the-word'),
        ...
    ```


