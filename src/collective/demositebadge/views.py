from zope.publisher.browser import BrowserView
from zope.component import getUtility
from zope.component import getMultiAdapter

from plone.registry.interfaces import IRegistry

from Acquisition import aq_inner


class DemoSiteBadgeView(BrowserView):
    
    def available(self):
        context = aq_inner(self.context)
        portal = getMultiAdapter((context, self.request),
            name=u'plone_portal_state').portal()
        registry = getUtility(IRegistry)
        text = registry[\
            'collective.demositebadge.interfaces.IBadgeSettings.text']
    
        if registry[\
                'collective.demositebadge.interfaces.IBadgeSettings.check'] \
           and text:
            return text
        else:
            return ''
