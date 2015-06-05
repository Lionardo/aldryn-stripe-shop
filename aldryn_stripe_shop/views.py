from django.views.generic import DetailView
from .models import Stripe


class stripeView(DetailView):

    model = Stripe

    def get_context_data(self, **kwargs):
        context = super(stripeView, self).get_context_data(**kwargs)

        context.update({
            'stripe': self.object,
        })
        return context
