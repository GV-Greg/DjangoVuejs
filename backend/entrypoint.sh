#!/bin/sh

set -e  # Exit on error
set -x  # Print commands being executed

echo "Current directory: $(pwd)"
echo "Listing contents:"
ls -la

# Créer les migrations
echo "Creating migrations..."
python manage.py makemigrations decision_tree

# Appliquer les migrations
echo "Applying database migrations..."
python manage.py migrate

# Vérifier le contenu des fixtures
# echo "Checking fixtures file:"
# cat decision_tree/fixtures/initial_data.json

# Charger les données initiales
# echo "Loading initial data..."
# python manage.py loaddata decision_tree/fixtures/initial_data.json

# Vérifier les données chargées
# echo "Verifying loaded data..."
# python manage.py shell -c "from decision_tree.models import Program; print('Programs in database:', Program.objects.count()); [print(f'- {p.name} ({p.id})') for p in Program.objects.all()]"

# Collecter les fichiers statiques
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Créer le superutilisateur
# echo "Creating superuser..."
# python create_superuser.py

# Démarrer le serveur
echo "Starting server..."
exec "$@"
