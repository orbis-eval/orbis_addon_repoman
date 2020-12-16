from jsonschema import Draft7Validator

from orbis_addon_repoman.format.json.folder import iterate_over_json_files
from .cluster_json import schema as schema_cluster
from .harvest_json import schema as schema_harvest
from .page_segmentation_json import schema as schema_page_segmentation
from ..annotation import get_annotation_key

schemas = [schema_cluster, schema_harvest, schema_page_segmentation]


def create(download_destination):
    convert = []
    for json_file, file in iterate_over_json_files(download_destination):
        annotations = get_annotation_key(json_file)
        json_file = _check_json_schema(annotations)
        if json_file and json_file not in convert:
            convert.append(json_file)

    return convert


def _check_json_schema(annotations):
    for schema in schemas:
        if Draft7Validator(schema['schema']).is_valid(annotations):
            return schema
    return None
