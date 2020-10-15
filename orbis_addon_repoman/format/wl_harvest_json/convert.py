# -*- coding: utf-8 -*-

import os
import json
import pathlib
import hashlib

import logging
logger = logging.getLogger(__name__)


class Convert(object):
    """docstring for Convert"""

    def __init__(self):
        super(Convert, self).__init__()

    def convert(self, download_destination, corpus_dir, download_name, corpus_url, download_time):

        with open(os.path.join(corpus_dir, "source.txt"), "w") as open_file:
            open_file.write(f"Downloaded from {corpus_url} at {download_time}")

        self.extract_files(download_destination, corpus_dir)
        self.extract_entities(download_destination, corpus_dir, download_name)

    def extract_files(self, download_destination, corpus_dir):
        gold_folder = os.path.join(corpus_dir, "corpus")
        pathlib.Path(gold_folder).mkdir(parents=True, exist_ok=True)

        folder = pathlib.Path(download_destination)
        for file in list(folder.glob('*.json')):
            with open(file, "r") as open_file:
                gold_content = json.load(open_file)

            doc_id = hashlib.md5(gold_content['url'].encode()).hexdigest()
            filename = os.path.join(gold_folder, doc_id + "-modified" + ".txt")

            if not os.path.exists(filename):
                with open(filename, "w", encoding="utf-8") as open_file:
                    open_file.write(gold_content['text'])

            filename = os.path.join(gold_folder, doc_id + ".txt")
            if not os.path.exists(filename):
                with open(filename, "w", encoding="utf-8") as open_file:
                    open_file.write(gold_content['html'])

    def extract_entities(self, download_destination, corpus_dir, download_name):
        gold_folder = os.path.join(corpus_dir, "gold")
        file_name = f'{download_name}.gs'
        pathlib.Path(gold_folder).mkdir(parents=True, exist_ok=True)

        lines = set()
        # gs file structure:
        # ---------------------
        #  0    1    2   3    4    5        6
        # doc|start|end|url|score|type|surface_form

        folder = pathlib.Path(download_destination)
        for file in list(folder.glob('*.json')):

            with open(file, "r") as open_file:
                gold_content = json.load(open_file)

            doc_id = hashlib.md5(gold_content['url'].encode()).hexdigest()

            for post in gold_content['gold_standard_annotation']:
                # print(post)
                for item in ['post_text', 'datetime', 'user', 'post_link']:
                    if post.get(item):
                        print("Processing")
                        document_number = doc_id
                        start = str(post[item]['start'])
                        end = str(post[item]['end'])
                        type_ = item
                        surface_form = post[item]['surface_form']
                        line = "\t".join([document_number, start, end, gold_content['url'], "1", type_, surface_form])
                        lines.add(line)

        with open(os.path.join(gold_folder, file_name), "w") as open_file:
            print(f"Writing to: {os.path.join(folder, file_name)}")
            for line in sorted(lines):
                # print(f"Writing line: {line}")
                open_file.write(f'{line}\n')
