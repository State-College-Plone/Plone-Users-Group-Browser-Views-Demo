from Products.CMFCore.utils import getToolByName
import logging

logger = logging.getLogger("demo.testproduct")


def add_modified_index(site):
    catalog = getToolByName(site, 'portal_catalog')
    indexes = catalog.indexes()
    # Specify the indexes you want, with ('index_name', 'index_type')
    wanted = (('last_modified_by', 'FieldIndex'),)
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def importVarious(context):
    if context.readDataFile('demo.testproduct_various.txt') is None:
        return
    site = context.getSite()
    add_modified_index(site)
