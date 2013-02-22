from zope.publisher.browser import BrowserView
from zope.component import getUtility
from zope.component import getMultiAdapter

from plone.registry.interfaces import IRegistry

from Acquisition import aq_inner


class DemoSiteBadgeView(BrowserView):
    
    def available(self):
        registry = getUtility(IRegistry)
    
        if registry[\
                'collective.demositebadge.interfaces.IBadgeSettings.check'] \
           and registry[\
                'collective.demositebadge.interfaces.IBadgeSettings.text']:
            return True
        else:
            return False
    
    def get_demo_label(self):
        context = aq_inner(self.context)
        portal = getMultiAdapter((context, self.request),
            name=u'plone_portal_state').portal()
        registry = getUtility(IRegistry)
        text = registry[\
            'collective.demositebadge.interfaces.IBadgeSettings.text']
        return text
