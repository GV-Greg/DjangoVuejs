#!/bin/sh

set -e  # Exit on error
set -x  # Print commands being executed

echo "Current directory: $(pwd)"
echo "Listing contents:"
ls -la

# Générer les migrations si besoin
echo "Creating migrations..."
python manage.py makemigrations

# Appliquer les migrations
echo "Applying database migrations..."
python manage.py migrate

# Collecter les fichiers statiques
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Démarrer le serveur
echo "Starting server..."
exec "$@"