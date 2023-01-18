from django.contrib.auth.models import AbstractUser
from django.db import models





class User(AbstractUser):
    pass


class Listing(models.Model):
    CATEGORIES_CHOICES = [
        ('books','Books'),
        ('bussiness','Business & Industrial'),
        ('clothing','Clothing, Shoes & Accessories'),
        ('collectibles','Collectibles'),
        ('electronics','Consumer Electronics'),
        ('crafts','Crafts'),
        ('dolls','Dolls & Bears'),
        ('home','Home & Garden'),
        ('motor','Motors'),
        ('pets','Pet Supplies'),
        ('sports','Sporting Goods'),
        ('mobile', 'Mobile Phones/Gadgets'),
        ('merch','Merchandise, Cards & Fan Shop'),
        ('toys','Toys & Hobbies'),
        ('antiques','Antiques'),
        ('computers','Computers/Tablets & Networking'),
        ('others', 'Others')
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200, blank=True, null=True)
    img = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=35, choices=CATEGORIES_CHOICES, blank=True, null=True)
    start_bid = models.IntegerField()
    active_status = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="bids_won")

    def __str__(self):
        return f'{self.title}'


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="biddings")
    amount = models.IntegerField()
    winner = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.id}: {self.amount}'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="list_comments")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    comment = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.comment}'

        
class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlisted")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="watchlist")
    
    def __str__(self):
        return f'{self.user_id}: {self.list_id}'

