import unittest2 as unittest

from Products.CMFCore.utils import getToolByName
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile , quickInstallProduct
from AccessControl import getSecurityManager
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.registry.interfaces import IRegistry
from zope.component import getUtility
from Acquisition import aq_inner

from collective.demositebadge.views import DemoSiteBadgeView


from collective.demositebadge.testing import \
    COLLECTIVE_DEMOSITEBADGE_INTEGRATION_TESTING


# TODO: add proper name to testing class
class TestView(unittest.TestCase):

    layer = COLLECTIVE_DEMOSITEBADGE_INTEGRATION_TESTING

    def setUp(self):
        # you'll want to use this to set up anything you need for your tests
        # below
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.view = DemoSiteBadgeView(request=self.request,  
            context=self.portal)

    
    
   def test_get_demo_label(self):
        registry = getUtility(IRegistry)

        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            True
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u'Testing site'
        result = self.view.get_demo_label()
        self.assertEqual(result,'Testing site')

        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            False
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u'Testing site'
        result = self.view.get_demo_label()
        self.assertEqual(result,'')

        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            True
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u''
        result = self.view.get_demo_label()
        self.assertEqual(result,'')

        registry['collective.demositebadge.interfaces.IBadgeSettings.check'] =\
            False
        registry['collective.demositebadge.interfaces.IBadgeSettings.text'] =\
            u''
        result = self.view.get_demo_label()
        self.assertEqual(result,'')

