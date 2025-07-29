import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from app1.models import SampleModel

SampleModel.objects.create(code=404, msg="Not Found.")
