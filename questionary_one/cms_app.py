# -*- coding: utf-8 -*-
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _


class QuestionaryOneApp(CMSApp):
    name = _('Questionary_one')
    urls = ['questionary_one.urls']
    app_name = 'questionary_one'

apphook_pool.register(QuestionaryOneApp)
