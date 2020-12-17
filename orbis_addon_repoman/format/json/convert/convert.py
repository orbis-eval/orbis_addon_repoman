# -*- coding: utf-8 -*-

import os
import json
import gzip
import pathlib
import hashlib

import logging
from ..folder import iterate_over_json_files
from ..annotation import get_annotation_key

logger = logging.getLogger(__name__)


class Convert(object):
    """docstring for Convert"""

    def __init__(self):
        super(Convert, self).__init__()

    def convert(self, download_destination, corpus_dir, download_name, corpus_url, download_time):

        with open(os.path.join(corpus_dir, "source.txt"), "w") as open_file:
            open_file.write(f"Downloaded from {corpus_url} at {download_time}")

        gold_dir = self._create_folder(corpus_dir, "gold")
        corpus_dir = self._create_folder(corpus_dir, "corpus")

        gold_annotations = {}
        for gold_content, file in iterate_over_json_files(download_destination):
            doc_id = hashlib.md5(gold_content['url'].encode('utf-8')).hexdigest()
            annotations = self._get_annotations(gold_content['url'], get_annotation_key(gold_content), file.name)
            filename = os.path.join(corpus_dir, doc_id + ".txt")
            self._write_corpus_file(filename, gold_content['text'])
            if 'html' in gold_content:
                filename = os.path.join(corpus_dir, doc_id + "-modified.txt")
                self._write_corpus_file(filename, gold_content['html'])
            gold_annotations[doc_id] = annotations
            if not annotations:
                logger.warning(f"No annotations in file [{file.name}]")

        filename = os.path.join(gold_dir, download_name + ".json.gz")
        self._write_gold_file(filename, gold_annotations)

    def _get_annotations(self, url, gold_annotations, file_name):
        raise NotImplementedError

    @staticmethod
    def _create_folder(base_dir, folder):
        folder_path = os.path.join(base_dir, folder)
        pathlib.Path(folder_path).mkdir(parents=True, exist_ok=True)
        return folder_path

    @staticmethod
    def _write_corpus_file(filename, corpus_text):
        if not os.path.exists(filename):
            with open(filename, "w", encoding="utf-8") as open_file:
                open_file.write(corpus_text)

    @staticmethod
    def _write_gold_file(filename, gold_content_json):
        json_str = json.dumps(gold_content_json)
        json_bytes = json_str.encode('utf-8')
        with gzip.GzipFile(filename, "w") as gzip_file:
            gzip_file.write(json_bytes)
