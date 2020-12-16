from ..convert.convert_harvest import ConvertHarvest

schema = {
    "schema": {
        "type": "array",
        "items": {
            "type": "object",
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
            },
            "required": ["post_text"]
        }
    },
    "convert": ConvertHarvest(),
    "description": "Convert fhgr harvest json files"
}
