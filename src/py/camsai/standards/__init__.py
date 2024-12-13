from pydantic import BaseModel, ValidationError


def is_valid_with_pydantic(example: dict, pydantic_model: BaseModel):
    """
    Validates a given example against the base model.

    Args:
        example (dict): example to validate.
        pydantic_model (BaseModel): base model to validate the example with.

    Returns:
        bool: True if the example is valid, False otherwise.
    """
    try:
        pydantic_model(**example)
        return True
    except ValidationError as e:
        return False


is_valid = is_valid_with_pydantic
