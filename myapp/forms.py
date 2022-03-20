from cProfile import label
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Category, Flower, Tag


class FlowerEditForm(ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    tags = forms.ModelMultipleChoiceField(
        Tag.objects.all(), label="Tags", widget=forms.SelectMultiple(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(Category.objects.all(
    ), label="Category", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Flower
        fields = ["title", "description", "tags", "category"]
