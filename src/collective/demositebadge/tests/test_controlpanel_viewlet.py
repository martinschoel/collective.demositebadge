import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile , quickInstallProduct
from AccessControl import getSecurityManager
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from zope.component import getUtility

from collective.demositebadge.viewlets import DemoSiteBadgeViewlet


from collective.demositebadge.testing import \
    COLLECTIVE_DEMOSITEBADGE_INTEGRATION_TESTING


class TestExample(unittest.TestCase):

    layer = COLLECTIVE_DEMOSITEBADGE_INTEGRATION_TESTING

    def setUp(self):
        # you'll want to use this to set up anything you need for your tests
        # below
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.viewlet = DemoSiteBadgeViewlet(request=self.request,
            view='collective.demositebadge', context=self.portal)

    def test_update(self):
        registry = getUtility(IRegistry)
        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            True
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u'Testing site'
        self.viewlet.update()
        self.assertEqual(u'Testing site', self.viewlet.text)
        
        
    def test_available(self):
        registry = getUtility(IRegistry)
        
        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            True
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u'Testing site'
        self.viewlet.update()
        result = self.viewlet.available()
        self.assertTrue(result)
        
        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            False
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u'Testing site'
        self.viewlet.update()
        result = self.viewlet.available()
        self.assertFalse(result)
        
        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            True
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u''
        self.viewlet.update()
        result = self.viewlet.available()
        self.assertFalse(result)
        
        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            False
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u''
        self.viewlet.update()
        result = self.viewlet.available()
        self.assertFalse(result)

