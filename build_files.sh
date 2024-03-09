echo "BUILD START"
#!/bin/bash

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput --clear

echo "BUILD END" 