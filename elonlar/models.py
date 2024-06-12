from django.db import models
import uuid
import random
import string
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.conf import settings





class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name
    
class Mahalla(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=1000, unique=True)

    def __str__(self) -> str:
        return self.name


class Streert(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=1000)
    mahalla = models.ForeignKey(Mahalla, related_name='street', on_delete=models.CASCADE)

    class Meta:
        unique_together=['name', 'mahalla']

    def __str__(self) -> str:
        return self.name 



UZS, USD, EURO = ("UZS", "Dollar", "Yevro")
class Ads(models.Model):
    PAYMENT_TYPE = (
        (UZS, UZS),
        (USD, USD),
        (EURO, EURO)
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photo/images_ad/', default='photo/default-image.jpg/', null=True, blank=True,
                               validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'heic', 'heif'])])
    title = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE, default=UZS)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE)
    street = models.ForeignKey(Streert, on_delete=models.CASCADE)
    hous_number = models.IntegerField()
    moljal = models.TextField()
    tel_number = models.CharField(max_length=13)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    unique_code = models.CharField(max_length=6, unique=True, editable=False)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = self.generate_unique_code()
        super(Ads, self).save(*args, **kwargs)

    def generate_unique_code(self):
        while True:
            code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            if not Ads.objects.filter(unique_code=code).exists():
                return code
    


    
class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ads_id = models.ForeignKey(Ads, on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    
    