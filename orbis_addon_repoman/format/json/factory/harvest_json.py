from ..convert.convert_harvest import ConvertHarvest

schema = {
    "schema": {
        "type": "array",
        "additionalItems": False,
        "items": {
            "type": "object",
            "required": ["post_text"],
            "additionalProperties": False,
            "properties": {
                "post_text": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                },
                "datetime": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                },
                "user": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                },
                "post_link": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                }
            }
        }
    },
    "convert": ConvertHarvest(),
    "description": "Convert fhgr harvest json files"
}
