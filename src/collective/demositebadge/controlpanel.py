from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper

from plone.z3cform import layout
from z3c.form import form, button
from collective.demositebadge.interfaces import IBadgeSettings
from Products.statusmessages.interfaces import IStatusMessage


class ControlPanelForm(RegistryEditForm):
    
    form.extends(RegistryEditForm)
    schema = IBadgeSettings
    
    
ControlPanelView = layout.wrap_form(ControlPanelForm, ControlPanelFormWrapper)
ControlPanelView.label = u"Demo Site Badge"
