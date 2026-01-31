from django.contrib.auth.models import User
from users.models import Profile


def run():
    users = User.objects.all()

    for user in users:
        try:
            profile = user.profile
        except Exception:
            profile = Profile(user=user, image="default.png")
            profile.save()
    
            print(f"Added profile for user: {user.username}")