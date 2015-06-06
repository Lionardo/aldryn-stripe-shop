from django.contrib import admin
from django.db import models
from django import forms

from .models import Stripe, Product


class CheckoutAdmin(admin.ModelAdmin):
    class Meta:
        model = Stripe


class ProductAdmin(admin.ModelAdmin):
    model = Product
    #I need to add the ckeditor to the description field
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(
                attrs={'class': 'ckeditor'})
        },
    }
    list_display = ['description']

    class Media:
        js = ('ckeditor/ckeditor.js',)


admin.site.register(Stripe, CheckoutAdmin)
admin.site.register(Product, ProductAdmin)
