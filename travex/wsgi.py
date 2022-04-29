"""
WSGI config for travex project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from pathlib import Path

import dotenv
from django.core.wsgi import get_wsgi_application

BASE_DIR = Path(__file__).resolve().parent.parent

dotenv.read_dotenv(BASE_DIR, '.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travex.settings')
os.environ.get("SECRET_KEY")

application = get_wsgi_application()
