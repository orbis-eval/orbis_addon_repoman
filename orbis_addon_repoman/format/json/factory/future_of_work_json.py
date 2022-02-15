from ..convert.convert_future_of_work import ConvertFutureOfWork

schema = {
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "work_activity": {"$ref": "#/definitions/cluster"}
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
                        "end": {"type": "number"},
                        "type": {"type": "string"}
                    },
                    "required": ["surface_form", "start", "end", "type"]
                }
            }
        }
    },
    "convert": ConvertFutureOfWork(),
    "description": "Future of Work json"
}
