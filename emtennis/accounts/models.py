from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """Create Profile model for each user """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True)
    ranking = models.CharField(null=True, max_length=10)


