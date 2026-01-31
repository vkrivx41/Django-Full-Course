from managers.models import Manager

def run():
    managers = Manager.objects.filter(phone_number__gt=10).delete()

    print(managers)