import logging
import time

from django.shortcuts import render
from django.views.generic.base import TemplateView

logger = logging.getLogger(__name__)

class DivideByView(TemplateView):

    template_name = 'demos/divide.html'

    def get_context_data(self, **kwargs):
        context = super(DivideByView, self).get_context_data(**kwargs)
        context['errors'] = []
        numerator = self.request.GET.get('n', None)
        denominator = self.request.GET.get('d', None)

        if numerator is None or denominator is None:
            logger.error('you must set a numerator and denominator!')
            context['errors'].append('you must set a numerator and denominator!')
        else:
            numerator = float(numerator)
            denominator = float(denominator)

            if denominator == 0.0:
                logger.error('attempted to divide by zero!')
                context['errors'].append('you tried to divide by zero!')
            else:
                logger.info(
                    'about to do this: {0} / {1}'.format(
                        numerator,
                        denominator
                    )
                )
                context['result'] = numerator / denominator

        context['numerator'] = numerator
        context['denominator'] = denominator
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