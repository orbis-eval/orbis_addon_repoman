from jsonschema import Draft7Validator

from orbis_addon_repoman.format.json.folder import iterate_over_json_files
from .cluster_json import schema as schema_cluster
from .harvest_json import schema as schema_harvest

schemas = [schema_cluster, schema_harvest]


def create(download_destination):
    convert = []
    for json_file, file in iterate_over_json_files(download_destination):
        annotations = _get_annotations(json_file)
        json_file = _check_json_schema(annotations)
        if json_file and json_file not in convert:
            convert.append(json_file)

    return convert


def _get_annotations(json):
    if 'annotations' in json:
        return json['annotations']
    elif 'gold_standard_annotation' in json:
        return json['gold_standard_annotation']
    return []


def _check_json_schema(annotations):
    for schema in schemas:
        if Draft7Validator(schema['schema']).is_valid(annotations):
            return schema
    return None
