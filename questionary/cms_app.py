# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _



class QuestionaryApp(CMSApp):
    name = _('Questionary')
    urls = ['questionary.urls']
    app_name = 'questionary'

apphook_pool.register(QuestionaryApp)
