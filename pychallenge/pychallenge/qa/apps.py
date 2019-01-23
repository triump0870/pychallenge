from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class QaConfig(AppConfig):
    name = 'pychallenge.qa'
    verbose_name = _('Q&A')
