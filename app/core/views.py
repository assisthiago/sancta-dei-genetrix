import json

from django.conf import settings
from django.shortcuts import render


def index(request):
    context_data = {"mater_dei_titles": json.dumps(settings.MATER_DEI_TITLES)}
    return render(request, "index.html", context=context_data)
