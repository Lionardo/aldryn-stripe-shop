from django.utils.translation import ugettext as _
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from models import CheckoutPlugin, ProductPlugin


class CheckoutPlugin(CMSPluginBase):
    model = CheckoutPlugin
    module = _('stripe shop')
    name = _("Checkout")
    render_template = "aldryn_stripe_shop/checkout.html"

    def render(self, context, instance, placeholder):
        stripe = instance.stripe
        context.update({
            'instance': instance,
            'placeholder': placeholder,
            'stripe': stripe,
        })
        return context


class ProductPlugin(CMSPluginBase):
    model = ProductPlugin
    module = _('stripe shop')
    name = _("Product")
    render_template = "aldryn_stripe_shop/product.html"
    allow_children = True

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
