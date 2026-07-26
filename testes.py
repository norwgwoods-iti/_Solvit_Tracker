from pydantic import BaseModel, Field, field_validator
import re

test_1 = {
    "id": 1,
    "name": "Васяш#",
    "description": "",
}


class TestSchema(BaseModel):
    id: int
    name: str = Field(min_length=5)
    description: str

    @field_validator('name')
    def name_val(cls, value):
        pattern = r'^@#%^&*$'
        if re.match(pattern, value):
            raise ValueError(f'Недопустимое имя поля {cls}')
        return value

print(repr(TestSchema(**test_1)))
# print("--------------------------------")
# print(TestSchema(**test_1))
# print("--------------------------------")
# print(TestSchema(**test_1).name)
