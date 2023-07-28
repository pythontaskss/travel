from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Team(models.Model):
    m_name = models.CharField(max_length=250)
    m_img = models.ImageField(upload_to='team')
    m_desc = models.TextField()

    def __str__(self):
        return self.m_name
