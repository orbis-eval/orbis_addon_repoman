from ..convert.convert_cluster import ConvertCluster

schema = {
    "schema": {
        "type": "object",
        "patternProperties": {
            "^I_": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "key": {"type": "string"},
                        "surfaceForm": {"type": "string"},
                        "start": {"type": "string"},
                        "end": {"type": "string"},
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
