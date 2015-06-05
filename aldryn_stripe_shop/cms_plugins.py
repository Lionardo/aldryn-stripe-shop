from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import CheckoutPlugin, ProductPlugin
from models import Stripe, Product
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _
from views import stripeView


class CheckoutPlugin(CMSPluginBase):
    model = CheckoutPlugin
    render_template = "aldryn_stripe_shop/checkout.html"
    text_enabled = True


    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context

class ProductPlugin(CMSPluginBase):
    model = ProductPlugin
    render_template = "aldryn_stripe_shop/product.html"
    text_enabled = True


    def render(self, context, instance, placeholder):
        products = instance.product
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'product': products,
        })
        return context

plugin_pool.register_plugin(CheckoutPlugin)
plugin_pool.register_plugin(ProductPlugin)
