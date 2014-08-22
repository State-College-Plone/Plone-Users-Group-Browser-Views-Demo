from plone.indexer.decorator import indexer
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName


def get_last_modified_by_username(object):
    pr = getToolByName(object, "portal_repository")
    history = pr.getHistoryMetadata(object)
    if history:
        revisions = history.getLength(countPurged=False)
        vdatafull = history.retrieve(revisions-1, countPurged=False)
        vdata = vdatafull['metadata']
        modifier = vdata['sys_metadata']['principal']
        return modifier
    return None


@indexer(IContentish)
def get_last_modified_user(object, **kw):
    return get_last_modified_user(object)
