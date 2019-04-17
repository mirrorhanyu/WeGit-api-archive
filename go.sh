#!/usr/bin/env bash

set -e

function setUp {
    VIRTUAL_ENV="env"
    rm -rf ${VIRTUAL_ENV}
    virtualenv ${VIRTUAL_ENV} --python=python3
    source ${VIRTUAL_ENV}/bin/activate
    pip3 install -r requirments.txt
}


function run {
    setUp
    gunicorn -w 4 -b 0.0.0.0:5000 main:app
}

run