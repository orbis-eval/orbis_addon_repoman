from ..convert.convert_education_extraction import ConvertEducationExtraction

schema = {
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "target_group": {"$ref": "#/definitions/cluster"},
            "certificate": {"$ref": "#/definitions/cluster"},
            "course_content": {"$ref": "#/definitions/cluster"},
            "prerequisite": {"$ref": "#/definitions/cluster"}
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
