from django.contrib.auth import get_user_model

def run():
    user = get_user_model().objects.first()

    user.is_active = True
    user.save()

    print(user.is_active)
    