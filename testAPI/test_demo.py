import json

from jsonschema import validate

#直接把schema写在函数里
def test_schema1():
    schema = {
        "type": "object",
        "properties": {
            "price": {"type": "number"},
            "name": {"type": "string"}
        }
    }
    validate(instance={"name": "Eggs", "price": 31.22}, schema=schema)

#直接把schema写在json文件里
def test_schema2():
    data = {"name": "Eggs", "price": 31.22}
    schema = json.load(open('schema.json'))
    validate(data, schema=schema)