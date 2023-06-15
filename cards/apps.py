from django.apps import AppConfig
import os
from django.conf import settings

class CardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cards'
    path = path = os.path.join(settings.BASE_DIR, 'cards')
