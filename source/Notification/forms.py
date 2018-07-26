from datetime import datetime
from django.utils.timezone import make_aware


def clean(DateTime):

    if DateTime < make_aware(datetime.now()):
        return False
    return True
