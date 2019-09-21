from __future__ import unicode_literals
from django.db import models
import datetime


class Manager(models.Manager):
    def validator(self, postData):
        errors = { }
        TITLE = postData['title']

        for x in Shows.objects.all():
            if x.title == TITLE:
                errors['title'] = 'Title already used'
        if len(postData['title']) < 5:
            errors['title'] = 'Title should be at least 5 letters'
        if postData['title'] == Shows.title:
            errors['title'] = 'Title should be at least 5 letters'
        if len(postData['network']) < 3:
            errors['network'] = 'Network should be at least 3 letters'
        if postData['release'] == datetime.date.today:
            errors['release_date'] = 'Needs to be a date, before today'
        if len(postData['description']) != 0:
            if len(postData['description']) < 10:
                errors['description'] = 'If there is a description it should be longer than 10 letters'  
        return errors


class Shows(models.Model):
    title = models.CharField(max_length=80, default='Add a title')
    network = models.CharField(max_length=80, default='Add a network')
    description = models.TextField(default='Add a description')
    release_date = models.DateField(default= datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()