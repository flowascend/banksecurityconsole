import os
import django
from datetime import datetime
from django.db.models.query import QuerySet
from datacenter.models import Passcard

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

def get_card_data(i: int, all_passcards: QuerySet[Passcard]) -> tuple[bool, datetime, str, str]:
    card = all_passcards[i]
    return (card.is_active, card.created_at, card.passcode, card.owner_name)

if __name__ == '__main__':
    all_passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    print('Passcards amount:', Passcard.objects.count())  # noqa: T001
    print('Active passcards amount:', len(active_passcards))  # noqa: T001
