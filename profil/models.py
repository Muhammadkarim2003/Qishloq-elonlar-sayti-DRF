from django.db import models
from django.contrib.auth.models import User
import uuid
from django.conf import settings




class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    tel_nimber = models.CharField(max_length=13)
    profile_photo = models.ImageField(upload_to='photo/profile_photos', default='profile_images/profile_default_image.png/')
    birth_date = models.DateField(null=True)




