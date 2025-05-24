from django.db import models
from django.utils import timezone

class Crypto_Coins(models.Model):
    title = models.CharField(max_length=250)
    creat_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Physic_coin(models.Model):
    title = models.CharField(max_length=250)
    creat_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Currensy_coin(models.Model):
    title = models.CharField(max_length=250)
    creat_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

# now We are going create some classes
class CryptoCoins(models.Model):
    title = models.CharField(max_length=100)
    code_coins = models.CharField(max_length=255)
    since = models.CharField(max_length=255)
    build_compainy = models.CharField(max_length=255)
    blockcheyn = models.CharField(max_length=255)
    category = models.ForeignKey(Crypto_Coins, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.title} {self.blockcheyn}"
class PhysicCoins(models.Model):
    title = models.CharField(max_length=100)
    code_coins = models.CharField(max_length=255)
    since = models.CharField(max_length=255)
    build_compainy = models.CharField(max_length=255)
    blockcheyn = models.CharField(max_length=255)
    category = models.ForeignKey(Physic_coin, on_delete=models.CASCADE)
    def __str__(self):
       return f"{self.title} {self.blockcheyn}"
    
class CurrensyCoins(models.Model):
    title = models.CharField(max_length=100)
    code_coins = models.CharField(max_length=255)
    since = models.CharField(max_length=255)
    build_compainy = models.CharField(max_length=255)
    blockcheyn = models.CharField(max_length=255)
    category = models.ForeignKey(Currensy_coin, on_delete=models.CASCADE)

    def __str__(self):
       return f"{self.title} {self.blockcheyn}"

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')
