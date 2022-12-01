from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):
    User = get_user_model()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ID_user =  models.IntegerField()
    bio = models.TextField(blank=True)
    profileImg = models.ImageField(upload_to= 'profile_images', default = 'empty-profile-image.jpeg')
    location = models.CharField(max_length= 100, blank=True)

    def __str__(self):
        return self.user.username

    
