Flask Spike
===========

Simple minimal flask project.

To run locally:

```
  $ sudo apt-get install pip
  $ pip install Flask gunicorn
  $ python hello.py
```

To deploy to heroku:

```
  $ heroku create myflaskprojectname
  $ heroku config:set PRODUCTION_MODE=true
  $ git push heroku master
```
