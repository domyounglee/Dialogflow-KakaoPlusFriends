"""
WSGI config for bot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os, sys

sys.path.append('/home/ubuntu/Django')
sys.path.append('/home/ubuntu/bot_venv/lib/python3.5/site-packages')

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bot.settings")

application = get_wsgi_application()
