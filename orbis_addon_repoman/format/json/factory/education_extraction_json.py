from ..convert.convert_education_extraction import ConvertEducationExtraction

schema = {
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "target_groups": {"$ref": "#/definitions/cluster"},
            "certificates": {"$ref": "#/definitions/cluster"},
            "course_contents": {"$ref": "#/definitions/cluster"},
            "prerequisites": {"$ref": "#/definitions/cluster"},
            "learning_objectives": {"$ref": "#/definitions/cluster"},
            "none_types": {"$ref": "#/definitions/cluster"},
        },
        "definitions": {
            "cluster": {
                "type": "array",
                "additionalItems": False,
                "items": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "key": {"type": "string"},
                        "type": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    },
                    "required": ["surface_form", "start", "end", "key", "type"]
                }
            }
        }
    },
    "convert": ConvertEducationExtraction(),
    "description": "education extraction json"
}
