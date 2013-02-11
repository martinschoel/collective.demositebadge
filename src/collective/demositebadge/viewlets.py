from plone.app.layout.viewlets import common as base
from zope.component import getMultiAdapter
from Acquisition import aq_inner
from zope.component import getUtility
from plone.registry.interfaces import IRegistry



class DemoSiteBadgeViewlet(base.ViewletBase):

    text = None
    registry = None
    
    def avaliable(self):
    
        if self.registry[\
                'collective.demositebadge.interfaces.IBadgeSettings.check']\
           and self.registry[\
                'collective.demositebadge.interfaces.IBadgeSettings.text']:
            return True
        else:
            return False
    
    def update(self):
    
        context = aq_inner(self.context)
        portal = getMultiAdapter((context, self.request),
                                 name=u'plone_portal_state').portal()
        self.registry = getUtility(IRegistry)
        self.text = self.registry[\
            'collective.demositebadge.interfaces.IBadgeSettings.text']
