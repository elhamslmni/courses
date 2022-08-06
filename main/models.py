from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    text = models.TextField()
    # chooses = models.ForeignKey(Choose, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def was_published_recently(self):
        if self.pub_date > timezone.now():
            return False
        return self.pub_date >= timezone.now() - timezone.timedelta(days=2)


class Choose(models.Model):
    text = models.TextField()
    number_of_vote = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class My_Course(models.Model):
    department = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    group_number = models.IntegerField()
    teacher = models.CharField(max_length=30)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    first_day = models.CharField(max_length=30)
    second_day = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Profile(models.Model):
    gender = models.CharField(max_length=7)
    bio = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # image = models.ImageField(upload_to=)

