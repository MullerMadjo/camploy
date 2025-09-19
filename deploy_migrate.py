# deploy_migrate.py
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "camploy.settings")
django.setup()

from django.core.management import call_command

print("Applying migrations to PostgreSQL...")
call_command("migrate")
print("Migrations applied successfully!")
