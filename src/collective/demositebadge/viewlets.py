from plone.app.layout.viewlets import common as base
from zope.component import getMultiAdapter
from Acquisition import aq_inner
from zope.component import getUtility
from plone.registry.interfaces import IRegistry



class DemoSiteBadgeViewlet(base.ViewletBase):

    def available(self):
        context = aq_inner(self.context)
        portal = getMultiAdapter((context, self.request),
            name=u'plone_portal_state').portal()
        registry = getUtility(IRegistry)
        
        if registry['collective.demositebadge.interfaces.IBadgeSettings.check']:
            return 1
        else:  
            return 0
