from StringIO import StringIO
from Products.Archetypes.Extensions.utils import install_subskin
from Products.CSSRegistry.config import *
from Products.CMFCore.utils import getToolByName


def install(self):
    out = StringIO()

    install_subskin(self, out, GLOBALS)

    # Install the CSSRegistry
    if TOOLNAME not in self.objectIds():
        factory = self.manage_addProduct['CSSRegistry']
        factory.manage_addTool(TOOLTYPE)
        print >> out, 'Added CSSRegistry'
    else:
        print >> out, 'CSSRegistry already exists.'

    # Install the JSRegistry
    if JSTOOLNAME not in self.objectIds():
        factory = self.manage_addProduct['CSSRegistry']
        factory.manage_addTool(JSTOOLTYPE)
        print >> out, 'Added JSRegistry'
    else:
        print >> out, 'JSRegistry already exists.'

    installPloneDefaultJS(self, out)
    
    installPloneDeafultCSS(self, out)
    
    return out.getvalue()





# the default-values-installers
def installPloneDeafultCSS(self, out):
    csstool = getToolByName(self, TOOLNAME)    
    csstool.registerStylesheet('ploneColumns.css', media="screen", rendering='import')
    csstool.registerStylesheet('plone.css', media="screen", rendering='import')
    csstool.registerStylesheet('ploneTextSmall.css', media="screen", rel='alternate stylesheet', rendering='link')
    csstool.registerStylesheet('ploneTextLarge.css', media="screen", rel='alternate stylesheet', rendering='link')
    csstool.registerStylesheet('plonePrint.css', media="print", rendering='import')
    csstool.registerStylesheet('plonePresentation.css', media="projection", rendering='import')
    csstool.registerStylesheet('ploneCustom.css', media="all", rendering='import')    
    print >> out, 'installed the Plone default styles'
    
    
def installPloneDefaultJS(self, out):
    """ Install all the jaascripts plne comes with normally"""
    jstool = getToolByName(self, JSTOOLNAME)    
    jstool.registerScript('plone_menu.js', expression='not:portal/portal_membership/isAnonymousUser')
    print >> out, 'installed the menu-javascript'
    
    jstool.registerScript('plone_javascripts.js')
    print >> out, 'installed the global plone javascripts'

    jstool.registerScript('plone_javascript_variables.js')
    print >> out, 'installed the javascript variables'

    