# -*- coding: utf-8 -*-

from . import convert
from orbis_addon_repoman import app


def run(file_destination, corpus_dir, file_name):

    if file_name.endswith("ttl"):
        convert.Convert().convert(file_destination, corpus_dir, file_name)
    else:
        convert.Convert().convert(file_destination, corpus_dir, file_name)

