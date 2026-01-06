from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    first_name : str = Field(examples= ["Manish"])
    last_name : str = Field(examples= ["Kumar"])
    wage : Optional[int] = Field(default=1000, examples=[1000])
    role : Optional[str] = Field(default="Engineer", examples= ["Data Engineer"])

class Attendance(BaseModel):
    labour_id : Optional[int] = Field(default=None, examples=[21])
    first_name : str = Field(default=None, examples= ["Manish"])
    last_name : str = Field(default=None, examples= ["Kumar"])

class UIResponse(BaseModel):
    status: str
    status_code: int
    data: any
    message: str


    model_config = {
        "arbitrary_types_allowed": True
    }

# # # Why is this needed?
# By default, Pydantic validates fields against known types like int, str, list, dict, etc. 
# If you include a field with a custom class (e.g., LabourService, DBConnection, or any user-defined type), Pydantic doesn’t know how to generate a schema or validate it, so it raises an error
#
# # # What does arbitrary_types_allowed=True do?
# It tells Pydantic to skip validation and schema generation for unknown types.
# The custom type is accepted as-is and stored in the model without conversion.
#
# Useful when:
# You inject service objects (e.g., database connections) into models.
# You have complex classes that don’t need JSON serialization or validation.   
#
# Best Practice: 
# Use this only for internal fields, not for request/response models. 
# For API responses, convert custom types to primitives or dicts using field_serializer.