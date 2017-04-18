# Haven

## Description
Weaves content.

We use:
* [marshmallow-jsonapi](https://github.com/marshmallow-code/marshmallow-jsonapi) to create a JSON-api and schema validation.
* [Blueprints](http://flask.pocoo.org/docs/0.11/blueprints/) and [Flask-restful](https://github.com/flask-restful/flask-restful) to create modular REST apis.
* [PostgreSQL](https://www.postgresql.org/) as our datastore.
* [Alembic](http://alembic.zzzcomputing.com/en/latest/) for migrations.


## Database
Dependency on PostgreSQL.

## Bootstrap
```
cd haven
virtualenv env
source env/bin/activate
pip install fabric

# Bootstrap your environment
fab bootstrap

# Bootstrap your database
fab bootstrap_database
fab bootstrap_database:env=test
```

## Testing
```
source env/bin/activate
fab test
```

## Running a server locally
```
source env/bin/activate
fab serve
```

## Production server
TBD
