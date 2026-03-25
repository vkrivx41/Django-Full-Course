from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class MultiAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return None
        
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(
                Q(username=username) | Q(email=username) | Q(phone_number=username)
            )
        except UserModel.DoesNotExist:
            return None

        if user and user.check_password(password):
            return user
        
        return None
    
        

        

    
