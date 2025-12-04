#!/bin/sh

# Wait for DB
echo "Waiting for postgres..."
while ! nc -z db 5432; do
  sleep 0.5
done
echo "Postgres started"

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start server (CMD in Dockerfile will run Daphne)
exec "$@"
