# kladdera-api

Kladerradatsch is redefining Task Management for Mental Well-being.
At its core, Kladerradatsch acknowledges the variability of human energy levels. Unlike traditional task managers that demand relentless productivity regardless of one's mental state, Kladerradatsch adapts to the user's fluctuating energy resources throughout the day.

Imagine a tool that empowers users to seize the high-energy days for tackling tasks and ambitions with fervor. Yet, equally important, Kladerradatsch gently reminds users to prioritize self-care and basic needs during low-energy periods, recognizing that productivity should never come at the cost of well-being.

* live link: https://kladdera-9fa58a88bfbf.herokuapp.com/
* front-end: https://github.com/DasUnicorn/kladdera

## Content

<!-- toc -->

## Technologies Used

* GitHub – storage and deployment
* Sublime Text - Editor
* Heroku - Deployment

### Languages Used

* Python

### Frameworks, Libraries & Programs Used

* Django, as python framework
* Django Restframework, as REST API
* dj-rest-auth, for athetication
* djangorestframework-simplejwt, for authentication with JWT
* gunicorn, as http-server
* whitenoise, to serve static files
* poetry, as dependency management

## Testing

The API functionality has been tested with [httpx](https://www.python-httpx.org/)

Test Authentication:
* POST 'register/' -> works
* POST '/auth/login/' -> works
* POST '/task/' -> works
* GET '/task/' -> works
* GET '/task/1' -> works
* POST '/task/1' -> works
* POST '/mood/1' -> works
* GET '/mood/1' -> works
* GET '/mood/' -> works
* POST '/mood/' -> works

### PEP8 Tests:

For this test the [CI Python Linter](https://pep8ci.herokuapp.com/) was used.

kladdera_api
* init.py All clear, no errors found
* asgi.py All clear, no errors found
* persmissions.py All clear, no errors found
* settings.py:
142: E122 continuation line missing indentation or outdented
143: E122 continuation line missing indentation or outdented
163: E501 line too long (91 > 79 characters)
166: E501 line too long (81 > 79 characters)
169: E501 line too long (82 > 79 characters)
172: E501 line too long (83 > 79 characters)
* urls.py All clear, no errors found
* views.py  All clear, no errors found
* wsgi.py All clear, no errors found

mood
* init.py All clear, no errors found
* admin.py All clear, no errors found
* apps.py All clear, no errors found
* models.py All clear, no errors found
* serializers.py All clear, no errors found
* urls.py All clear, no errors found
* views.py All clear, no errors found

tasks
* init.py All clear, no errors found
* admin.py All clear, no errors found
* apps.py All clear, no errors found
* models.py:
19: E501 line too long (108 > 79 characters)
24: E501 line too long (85 > 79 characters)
* serializers.py All clear, no errors found
* urls.py All clear, no errors found
* views.py All clear, no errors found

users
* init.py  All clear, no errors found
* admin.py  All clear, no errors found
* apps.py  All clear, no errors found
* mangers.py All clear, no errors found
* models.py All clear, no errors found
* serializers.py All clear, no errors found
* urls.py All clear, no errors found
* views.py All clear, no errors found


### Manuel Testing:


## Deployment

### Local Deployment
1. Clone the git repository
2. Navigate into your local project folder
3. Install Poetry
4. Install the dependencies with 'poetry install'
5. Set the following global variables for your project in a local env.py file:
* ALLOWED_HOST
* CLIENT_ORIGIN
* CLIENT_ORIGIN_DEV
* DATABASE_URL
* SECRET_KEY
6. Start the application with 'python manage.py runserver'


### Heroku Deployment
1. Login, or sign up to [Heroku](heroku.com)
2. Create a new App
3. Connect the App to your Github Repository
4. If not set automaticly, set the heroku/python Buildpack
5. Set the following global variables for your project:
* ALLOWED_HOST
* CLIENT_ORIGIN
* CLIENT_ORIGIN_DEV
* DATABASE_URL
* SECRET_KEY
6. User the Heroku Deploy for deployment


## Credits
* https://python.plainenglish.io/django-custom-user-model-and-auth-using-jwt-simple-boilerplate-6acd78bf7767
* https://www.youtube.com/watch?v=diB38AvVkHw
* https://medium.com/@yashnarsamiyev2/custom-users-using-django-rest-framework-dda29f657e95
* https://dj-rest-auth.readthedocs.io/en/latest/configuration.html
* https://stackoverflow.com/questions/62966136/typeerror-field-id-expected-a-number-but-got-django-contrib-auth-models-anon