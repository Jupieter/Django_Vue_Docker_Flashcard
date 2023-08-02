from django.apps import AppConfig
import os
from django.conf import settings

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
    path = path = os.path.join(settings.BASE_DIR, 'api')