#!/bin/sh

exec gunicorn -w 4 app:app -b 0.0.0.0:5000
