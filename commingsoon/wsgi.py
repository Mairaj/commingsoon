"""
WSGI config for commingsoon project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "commingsoon.settings")

#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()

application = get_wsgi_application()
#application = DjangoWhiteNoise(application)
