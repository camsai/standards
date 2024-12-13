import jsonschema


def validate(example, schema):
    """
    Validates a given example against the schema.

    Args:
        example (dict|list): example to validate.
        schema (dict): schema to validate the example with.

    Raises:
        jsonschema.exceptions.ValidationError
    """
    jsonschema.validate(example, schema)
