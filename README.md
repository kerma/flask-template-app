# Flask template app

Simple Flask app with Gunicorn and Docker. 

Implements the basics I constantly keep re-inventing for Flask based apps:

1. Package structure
1. Developing with Flask builtin server while in Docker
1. PostgreSQL and psycopg2 (ORM is not needed, mkey..)
1. Blueprints
1. Flask-Restful for API's
1. Bootstrap base template and static files

## Database 

I don't really believe in ORMs, so plain old SQL it is. PostgreSQL is also a bit nicer to work with than MySQL, the only pain being getting psycopg2 installed to Alpine based docker image. Database root and application user credentials can be found 
in `docker-compose.yml`.


## Build, install, run

    docker build -t kerma/flask-template-app .
    docker-compose up

You can skip build step if you have [devpi-server](https://devpi.net/) running on `localhost:3141`.
After Postgres has booted itself run (password: `flask`):

    sh script/bootstrap.sh

`Hello World` can be now seen on `http://localhost:8080`.

For restful API you can use POST, PUT and GET methods on `/rest/hello/` endpoint. 
For example using [httpie](https://httpie.org/):

    $ http POST http://localhost:8080/rest/hello/ value=world
    HTTP/1.0 200 OK
    Content-Length: 16
    Content-Type: application/json
    Date: Fri, 14 Sep 2018 14:08:42 GMT
    Server: Werkzeug/0.14.1 Python/3.7.0

    {
        "id": 1
    }


    $ http http://localhost:8080/rest/hello/1
    HTTP/1.0 200 OK
    Content-Length: 38
    Content-Type: application/json
    Date: Fri, 14 Sep 2018 14:09:24 GMT
    Server: Werkzeug/0.14.1 Python/3.7.0

    {
        "id": 1,
        "value": "world"
    }


