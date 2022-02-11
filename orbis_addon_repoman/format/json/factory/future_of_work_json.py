from ..convert.convert_future_of_work import ConvertFutureOfWork

schema = {
    "schema": {
                "type": "array",
                "additionalItems": False,
                "items": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"},
                    },
                    "required": ["surface_form", "start", "end"]
                }
    },
    "convert": ConvertFutureOfWork(),
    "description": "Future of Work json"
}
