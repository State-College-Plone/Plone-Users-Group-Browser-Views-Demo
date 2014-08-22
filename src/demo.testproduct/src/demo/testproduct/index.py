from plone.indexer.decorator import indexer
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName


@indexer(IContentish)
def get_last_modified_user(object, **kw):
    pr = getToolByName(object, "portal_repository")
    history = pr.getHistoryMetadata(object)
    if history:
        revisions = history.getLength(countPurged=False)
        vdatafull = history.retrieve(revisions-1, countPurged=False)
        vdata = vdatafull['metadata']
        modifier = vdata['sys_metadata']['principal']
        return modifier
    return None

