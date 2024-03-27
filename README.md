# OnePage

Amplifying the voices of diverse creators worldwide: build your online presence
with one page for all of your profiles. Grow your small business or social media
page with your own, personalized platform.

## Description

OnePage is a platform that allows you to combine all of your online links into
one page. By providing a single place for your whole online presence, OnePage
will help you connect with your audience in a professional manner.

## Features

-   Built-in support for multiple online platforms
-   Allows linking to your own website
-   Fast and easy registration and setup

## Getting started

### Cloning the repository

```shell
# Clone from GitHub
git clone https://github.com/xtt28/onepage

# Use repository directory
cd onepage
```

### Activating the virtual environment

```shell
# Setup virtual environment
python3 -m venv .

# Use virtual environment shell
source bin/activate
```

### Installing dependencies

```shell
# Install from requirements.txt
pip install -r requirements.txt
```

### Development

#### Switching to the Django project directory

```shell
# Open Django project directory
cd onepage
```

#### Running the tests

```shell
# Run tests with Django
./manage.py test
```

#### Applying migrations

```shell
# Run all database migrations
./manage.py migrate
```

#### Running the development server

```shell
# Run the development server
./manage.py runserver

# Will be accessible at http://localhost:8000
```

### Production

#### Set environment variables

By default, the project uses the `SECRET_KEY` environment variable for the
Django secret key. Set it with:

```shell
# Set SECRET_KEY environment variable
export SECRET_KEY=your_key
```

#### Collect static files

```shell
# Collect static files into the prod_static directory
./manage.py collectstatic
```

#### Preparing for deployment

Please refer to the Django [deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
for detailed instructions on deployment. You can run an automated check with:

```shell
# Automated pre-deployment check
./manage.py check --deploy
```

## Technology

### Frontend

-   [Pico CSS](https://picocss.com/)
-   [htmx](https://htmx.org)

### Backend

-   [Django](https://www.djangoproject.com/)
-   [SQLite](https://sqlite.org)
