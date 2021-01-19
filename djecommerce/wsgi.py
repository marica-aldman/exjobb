import os
from django.conf import settings
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djecommerce.settings')
os.environ["DJANGO_SETTINGS_MODULE"] = "djecommerce.settings.production"
application = get_wsgi_application()
