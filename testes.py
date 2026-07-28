# from pydantic import BaseModel, Field, field_validator
# import re
#
# test_1 = {
#     "id": 1,
#     "name": "Васяяяя",
#     "description": "",
# }
#
#
# class TestSchema(BaseModel):
#     id: int
#     name: str
#     description: str
#
#     @field_validator("name")
#     def name_val(cls, value):
#
#         symbols = r'[!@#$%^&!*=+-;~]'
#
#         if re.search(symbols, value):
#             raise ValueError(f'Недопустимое имя поля {cls}')
#         return value
#
#
# print(repr(TestSchema(**test_1)))
# # print("--------------------------------")
# # print(TestSchema(**test_1))
# # print("--------------------------------")
# # print(TestSchema(**test_1).name)