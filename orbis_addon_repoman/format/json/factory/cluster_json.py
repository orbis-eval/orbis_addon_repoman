from ..convert.convert_cluster import ConvertCluster

schema = {
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "patternProperties": {
            "^[A-Za-z0-9_]*$": {
                "type": "array",
                "items": {
                    "type": "object",
                    "required": ["key", "surfaceForm", "start", "end", "entity_type", "entity_metadata"],
                    "properties": {
                        "key": {"type": "string"},
                        "surfaceForm": {"type": "string"},
                        "start": {"type": "number"},
                        "end": {"type": "number"},
                        "entity_type": {"type": "string"},
                        "entity_metadata": {
                            "type": "object",
                            "properties": {
                                "document_index_end": {"type": "array"},
                                "document_index_start": {"type": "array"}
                            }
                        }
                    }
                }
            }
        }
    },
    "convert": ConvertCluster(),
    "description": "Convert cluster json files"
}
