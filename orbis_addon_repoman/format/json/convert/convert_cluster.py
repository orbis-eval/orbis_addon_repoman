# -*- coding: utf-8 -*-

import logging

from .convert import Convert

logger = logging.getLogger(__name__)


class ConvertCluster(Convert):
    """docstring for Convert"""

    def __init__(self):
        super(ConvertCluster, self).__init__()

    def _get_annotations(self, gold_annotations, file_name):
        annotations = []
        if type(gold_annotations) == dict:
            for cluster, items in gold_annotations.items():
                if items:
                    for item in items:
                        if "key" in item and "entity_type" in item and "surfaceForm" in item and \
                                "entity_metadata" in item and \
                                "document_index_start" in item["entity_metadata"] and \
                                "document_index_end" in item["entity_metadata"]:
                            annotations.append({
                                "key": item["key"],
                                "score": 1,
                                "entity_type": item["entity_type"].lower(),
                                "type_url": item["entity_type"].lower(),
                                "surfaceForm": item["surfaceForm"],
                                "start": item["entity_metadata"]["document_index_start"][0],
                                "end": item["entity_metadata"]["document_index_end"][0],
                                "annotations": [{"type": "Cluster", "entity": cluster}],
                            })
                        else:
                            logger.warning(f"Ignored item {item}")
        else:
            logger.warning(f"List instead of dict in file {file_name}")
        return annotations
