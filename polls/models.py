from django.db import models
from django.db.models.query import QuerySet
from django.utils.translation import gettext_lazy as _


class User(models.Model):
    photo = models.BinaryField(null=True)
    username = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    

class Category(models.Model):
    name = models.CharField(max_length=60)
    classname_fontawesome = models.CharField(max_length=40)

   
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    question_text = models.CharField(max_length=200)
    op1 = models.CharField(max_length=15)
    op2 = models.CharField(max_length=15)
    op3 = models.CharField(max_length=15)
    op4 = models.CharField(max_length=15)


class Choice(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.IntegerField()


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fr_user_sender_id')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fr_user_recipient_id')
    accepted = models.BooleanField(default=False)


class UserReport(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_user_sender_id')
    violator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_user_violator_id')
    reason = models.CharField(null=True, max_length=200)


class QuestionReport(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='report_question_sender_id')
    violator = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='report_question_violator_id')
    reason = models.CharField(null=True, max_length=200)


class Punishment(models.Model):
    class PunishmentType(models.IntegerChoices):
        BAN = 1, _('Banned')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    punishment = models.IntegerField(choices=PunishmentType.choices)
    begin = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)
