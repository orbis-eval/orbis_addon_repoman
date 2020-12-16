from ..convert.convert_page_segmentation import ConvertPageSegmentation

schema = {
    "schema": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "target_group": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                },
                "certificate": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                },
                "course_content": {
                    "type": "object",
                    "properties": {
                        "surface_form": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"}
                    }
                },
                "prerequisite": {
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
    "convert": ConvertPageSegmentation(),
    "description": "Page segmentation json"
}
