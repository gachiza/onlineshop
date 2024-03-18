from django.contrib.auth.models import User

class UserLogin(): 
    class Meta:
        model = User
        fields = ['username', 'password']