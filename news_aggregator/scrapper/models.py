from django.db import models

# Create your models here.



class NyTimesModel(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()
    creator = models.TextField()
    publication_date = models.CharField(max_length=255)
    media_url = models.TextField()
    media_description = models.TextField()
    media_credit = models.TextField()
    categories = models.TextField()

    def __str__(self):
        return self.title

class FoxNewsModel(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()
    creator = models.TextField()
    publication_date = models.CharField(max_length=255)
    media_url = models.TextField()
    media_description = models.TextField()
    media_credit = models.TextField()
    categories = models.TextField()

    def __str__(self):
        return self.title

class PcMagModel(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()
    creator = models.TextField()
    publication_date = models.CharField(max_length=255)
    media_url = models.TextField()
    media_description = models.TextField()
    media_credit = models.TextField()
    categories = models.TextField()

    def __str__(self):
        return self.title

class CnetModel(models.Model):
    title = models.TextField()
    link = models.TextField()
    description = models.TextField()
    creator = models.TextField()
    publication_date = models.CharField(max_length=255)
    media_url = models.TextField()
    media_description = models.TextField()
    media_credit = models.TextField()
    categories = models.TextField()

    def __str__(self):
        return self.title

