# -*- coding: utf-8 -*-
from django.db import models
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

class Stripe(models.Model):
    publishable = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255, unique=True)
    address = models.BooleanField(default=True)
    currency = models.BooleanField(default=True)
    image = models.BooleanField(default=True)
    remember_me = models.BooleanField(default=False)
    description = models.BooleanField(default=False)
    bitcoin = models.BooleanField(default=False)

    def copy_relations(self, oldinstance):
        self.sections = oldinstance.sections.all()

class CheckoutPlugin(CMSPlugin):
    stripe = models.ForeignKey(Stripe)

class Product(models.Model):
    stripe = models.ForeignKey(Stripe)
    title = models.CharField(_('Product title'), max_length=100, blank=True)
    description = models.TextField(_('Product description'), max_length=255, blank=True, default='')
    image = FilerImageField(null=True, blank=True, related_name="product_image")
    disclaimer = FilerFileField(null=True, blank=True, related_name="product_disclaimer")
    price = models.IntegerField(blank=True)

    def __unicode__(self):
        return smart_unicode(self.title)

    def copy_relations(self, oldinstance):
        self.sections = oldinstance.sections.all()

class ProductPlugin(CMSPlugin):
    product = models.ForeignKey(Product)
