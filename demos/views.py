import logging
import time

from django.shortcuts import render
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)

class DivideByView(TemplateView):

    template_name = 'demos/divide.html'

    def get_context_data(self, **kwargs):
        context = super(DivideByView, self).get_context_data(**kwargs)
        context['numerator'] = float(self.request.GET.get('n', None))
        context['denominator'] = float(self.request.GET.get('d', None))
        logger.info(
            'about to do this: {0} / {1}'.format(
                context['numerator'],
                context['denominator']
            )
        )
        context['result'] = context['numerator'] / context['denominator']
        return context

class SleepView(TemplateView):

    template_name = 'demos/sleep.html'

    def get_context_data(self, **kwargs):
        context = super(SleepView, self).get_context_data(**kwargs)
        context['seconds'] = float(self.request.GET.get('seconds', None))
        logger.info(
            'sleeping for {0} seconds'.format(
                context['seconds']
            )
        )
        time.sleep(context['seconds'])
        return context