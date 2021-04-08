from ..convert.convert_page_segmentation import ConvertPageSegmentation

schema = {
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "target_groups": {"$ref": "#/definitions/cluster"},
            "certificates": {"$ref": "#/definitions/cluster"},
            "course_contents": {"$ref": "#/definitions/cluster"},
            "prerequisites": {"$ref": "#/definitions/cluster"}
        },
        "definitions": {
            "cluster": {
                "type": "array",
                "additionalItems": False,
                "items": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    },
                    "required": ["surface_form", "start", "end"]
                }
            }
        }
    },
    "convert": ConvertPageSegmentation(),
    "description": "Page segmentation json"
}
