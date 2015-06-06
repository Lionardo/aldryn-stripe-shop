# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from django.utils.encoding import smart_unicode


class Stripe(models.Model):
    name = models.CharField(_('account name'), max_length=100, blank=True)
    publishable = models.CharField(max_length=255, blank=False)
    secret_key = models.CharField(max_length=255, unique=True)
    address = models.BooleanField(default=True, help_text="Do you wish to display the adress for checkout?")
    currency = models.BooleanField(default=True, help_text="Do you wish to display the currency for checkout?")
    image = models.BooleanField(default=True, help_text="Do you wish to show the products image on checkout?")
    remember_me = models.BooleanField(default=False, help_text="Do you wish to store user entries for next time?")
    description = models.BooleanField(default=False, help_text="Do you wish to show the products description on checkout?")
    bitcoin = models.BooleanField(default=False, help_text="Allow payments in bitcoin?")

    def __unicode__(self):
        return smart_unicode(self.name)

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
