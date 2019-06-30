#!/usr/bin/env bash

set -e

function setUp {
    VIRTUAL_ENV="env"
    rm -rf ${VIRTUAL_ENV}
    virtualenv ${VIRTUAL_ENV} --python=python3
    source ${VIRTUAL_ENV}/bin/activate
    pip3 install -r requirements.txt
}

function migrate {
    url="postgresql://${DATABASE_USERNAME}:${DATABASE_PASSWORD}@${DATABASE_ENDPOINT}/${DATABASE_NAME}"
    repository="migration"
    python migration/manage.py upgrade ${url} ${repository}
}

function run {
    setUp
    migrate
    gunicorn -w 4 -b 0.0.0.0:5000 main:app
}

run
