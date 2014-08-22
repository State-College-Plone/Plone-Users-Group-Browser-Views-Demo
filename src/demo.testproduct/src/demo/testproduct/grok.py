from zope.interface import Interface
from five import grok
from Products.CMFCore.interfaces import ISiteRoot


class TestGrokView(grok.View):
    grok.context(ISiteRoot)
