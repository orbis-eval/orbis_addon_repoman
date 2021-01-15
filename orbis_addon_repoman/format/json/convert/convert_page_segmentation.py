# -*- coding: utf-8 -*-

import logging

from .convert import Convert

logger = logging.getLogger(__name__)


class ConvertPageSegmentation(Convert):
    """docstring for Convert"""

    def __init__(self):
        super(ConvertPageSegmentation, self).__init__()

    def _get_annotations(self, url, gold_annotations, file_name):
        annotations = []
        for name, items in gold_annotations.items():
            for item in items:
                annotations.append({
                    "key": url,
                    "entity_type": name,
                    "type_url": name,
                    "score": 1,
                    "surfaceForm": item["surface_form"],
                    "start": item["start"],
                    "end": item["end"],
                })
        return annotations
