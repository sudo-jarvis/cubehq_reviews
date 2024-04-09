# CubeHQ Assignment Task

Python Version - 3.8

## Setup

The first thing to do is to clone the repository:

```sh
git clone https://github.com/sudo-jarvis/cubehq_reviews.git
cd cubehq_reviews
```

Create a virtual environment to install dependencies in and activate it:

```sh
virtualenv -p python3.8 venv
source venv/bin/activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

Run any migrations present:

```sh
python manage.py migrate
```

Once `pip` has finished downloading the dependencies:

```sh
python manage.py runserver
```
