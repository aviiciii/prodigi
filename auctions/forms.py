from cProfile import label
from django import forms
from .models import User, Listing, Bid, Comment, Watchlist


class NewItem(forms.ModelForm):
    
    class Meta:
        model = Listing
        fields = ('title', 'desc', 'img', 'category', 'start_bid')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control'}),
            'img': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'start_bid' : forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Title',
            'desc': 'Description',
            'img': 'Image URL',
            'category': 'Category',
            'start_bid' : 'Starting Bid',
        }