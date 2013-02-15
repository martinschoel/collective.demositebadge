from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile, quickInstallProduct
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import ploneSite

from plone.testing import z2

from zope.configuration import xmlconfig


class CollectivedemositebadgeLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import collective.demositebadge
        xmlconfig.file(
            'configure.zcml',
            collective.demositebadge,
            context=configurationContext
        )
    
    def setUpPloneSite(self, portal):
        
#        applyProfile(portal, 'collective.demositebadge:settings')
        quickInstallProduct(portal,'collective.demositebadge')

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')


COLLECTIVE_DEMOSITEBADGE_FIXTURE = CollectivedemositebadgeLayer()
COLLECTIVE_DEMOSITEBADGE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_DEMOSITEBADGE_FIXTURE,),
    name="CollectivedemositebadgeLayer:Integration"
)
