from django.db import models


class StartPage(models.Model):
    arztozka_img = models.ImageField(upload_to='photos/Start_Page/')
