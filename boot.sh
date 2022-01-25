#!/bin/sh
exec gunicorn -b :8080 --timeout 300 app:application
