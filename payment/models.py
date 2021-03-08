from django.db import models
from django.contrib.auth.models import User

class ExtendUser(models.Model):
    company = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')

    class Meta:
        db_table = 'extend_user'

class Bank(models.Model):
    bank_name = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)

    class Meta:
        db_table = 'bank'

class Account(models.Model):
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE,related_name='bank')
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='account_user')
    account_number = models.CharField(max_length=12)
    balance = models.FloatField(max_length=20)
    class Meta:
        db_table = 'account'

class Card(models.Model):
    expiry_date = models.DateField()
    cvv = models.IntegerField()
    account = models.OneToOneField(Account,on_delete=models.CASCADE,related_name='account')
    card_number = models.CharField(max_length=16)
    card_type = models.CharField(max_length=10)
    start_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'card'

class Subscription(models.Model):
    name = models.CharField(max_length=10)
    amount = models.FloatField(max_length=20)
    start_date = models.DateField(auto_now=True)
    expiry_date = models.DateField()

    class Meta:
        db_table = 'subscription'

class UserSubscripiton(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='subscribe_user')
    subscription = models.ForeignKey(Subscription,on_delete=models.CASCADE,related_name='subscribe')
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_subscripiton'