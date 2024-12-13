from camsai.standards import is_valid
from camsai.standards.mat3ra import MaterialSchema as Mat3raMaterialSchema
from mat3ra.esse.data.examples import EXAMPLES


def test_validate_pydantic_matera():
    example_material = next((e for e in EXAMPLES if e["path"] == "material"), None)["data"]
    # TODO: figure out why derivedProperties is not in the schema
    example_material["derivedProperties"] = []
    assert is_valid(example_material, Mat3raMaterialSchema)


