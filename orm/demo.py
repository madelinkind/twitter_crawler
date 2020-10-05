# Turn off bytecode generation
import sys
# sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# import and setup django
import django
django.setup()

# Import your models for use in your script
from db.models import TwitterUser

def list_users():
    # Start of application script (demo code below)
    for u in TwitterUser.objects.all():
        print(f"id: {u.id}\tScreenname: {u.screen_name}")

if __name__ == '__main__':
    list_users()