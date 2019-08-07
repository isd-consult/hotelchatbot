from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class BroadcastMessage(models.Model):
    content = models.CharField(max_length=250)
    writer = models.CharField(max_length=50)

class CustomUser(AbstractUser):
    CUSTOMER = 'customer'
    FRONTDESK = 'frontdesk' 
    CONCIERGE = 'concierge'
    ACTIVITIESDESK = 'activitiesdesk'
    OPERATOR = 'operator'
    ROLE = (
        (CUSTOMER, 'customer'),
        (FRONTDESK, 'frontdesk'), 
        (CONCIERGE, 'concierge'),
        (ACTIVITIESDESK, 'activitiesdesk'),
        (OPERATOR, 'operator'),
    )
    role = models.CharField(max_length=20, choices=ROLE, default=CUSTOMER)
    checkindatetime = models.DateTimeField(default=timezone.now, null=True, blank=True)
    checkoutdatetime = models.DateTimeField(default=timezone.now, null=True, blank=True)
    roomnumber = models.CharField(max_length = 20, null=True, blank=True)
    broadcastmessage = models.ManyToManyField(BroadcastMessage)

    def __str__(self):
        return self.username

class ChatBotHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    usertext = models.TextField()
    bottext = models.TextField()
    chatdatetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.usertext + "&" + self.bottext

class Room(models.Model):
    name = models.CharField(max_length=40, unique=True)
    members = models.ManyToManyField(CustomUser, related_name="rooms")
    is_active = models.BooleanField(default=False)
    alias = models.CharField(max_length=40, unique=True)
    def __str__(self):
        return self.name


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    language = models.CharField(max_length=5)
    content = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

class Theme(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class CurrentTheme(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

