from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Event(models.Model):
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True, max_length=1025)
    start_time = models.TimeField()
    end_time = models.TimeField()
    registered_users = models.ManyToManyField(CustomUser, blank=True)
    link = models.URLField(blank=True, null=False)
    youtube_link = models.URLField(blank=True, null=False)
    webex_link = models.URLField(blank=True, null=False)

    def __str__(self):
        return self.name

    @property
    def status(self):
        curr = datetime.datetime.now().time()
        if time_in_range(self.start_time, self.end_time, curr):
            return 0
        elif self.start_time > curr:
            return -1
        elif self.end_time < curr:
            return 1
    
class PageImage(models.Model):
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(blank=True, null=False)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

    def __str__(self):
        return self.name
    
class Feedback(models.Model):
    name = models.CharField(max_length=1000, blank=True)
    link1 = models.URLField()
    link2 = models.URLField()
    link3 = models.URLField()
    link4 = models.URLField()

    def __str__(self):
        return self.name
    