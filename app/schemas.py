# app/schemas.py
from marshmallow import Schema, fields, ValidationError, validates_schema
from marshmallow_enum import EnumField
from .models import ValueType

def infer_type(value):
    if value is None:        
        return None
    if isinstance(value, bool):
        return ValueType.boolean
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return ValueType.number
    if isinstance(value, str):
        return ValueType.string
    if isinstance(value, list):
        return ValueType.array
    if isinstance(value, dict):
        return ValueType.json
    raise ValidationError("Unsupported value type")

class ParameterInSchema(Schema):
    name = fields.String(required=True)
    value = fields.Raw(required=True, allow_none=True)
    value_type = EnumField(ValueType, required=False, allow_none=True)

    @validates_schema
    def validate_and_fill_type(self, data, **_):
        v = data.get("value")
        vt = data.get("value_type") or infer_type(v)

        # Si vt es None (caso value == None), no validamos contra Enum
        if vt is None:
            data["value_type"] = None
            return

        # Validación simple por tipo
        if vt == ValueType.number and not (isinstance(v, (int, float)) and not isinstance(v, bool)):
            raise ValidationError({"value": "must be number"})
        if vt == ValueType.boolean and not isinstance(v, bool):
            raise ValidationError({"value": "must be boolean"})
        if vt == ValueType.string and not isinstance(v, str):
            raise ValidationError({"value": "must be string"})
        if vt == ValueType.array and not isinstance(v, list):
            raise ValidationError({"value": "must be array"})
        if vt == ValueType.json and not isinstance(v, dict):
            raise ValidationError({"value": "must be json object"})

        data["value_type"] = vt

class ParameterOutSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    value = fields.Raw(allow_none=True)
    value_type = EnumField(ValueType, allow_none=True)
