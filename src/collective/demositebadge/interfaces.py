from zope.interface import Interface
from zope import schema


class IBadgeSettings(Interface):
    
    check = schema.Bool(title=u'Display badge')
    text = schema.TextLine(title=u'Text to show')
