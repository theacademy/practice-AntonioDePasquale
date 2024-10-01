from django.contrib.auth.backends import BaseBackend
from .models import SignInDetail

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = SignInDetail.objects.get(email=username)
            if user.check_password(password):
                return user
        except SignInDetail.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return SignInDetail.objects.get(pk=user_id)
        except SignInDetail.DoesNotExist:
            return None