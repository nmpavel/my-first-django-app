#!/bin/bash

echo "Create Migrations"
python3 manage.py makemigrations crud
echo "================================"

echo "Migrate"
python3 manage.py migrate
echo "================================"

echo "Start server"
python3 manage.py runserver 0.0.0.0:8000
  
