from flask import Blueprint, request, jsonify
from sqlalchemy.exc import IntegrityError
from .db import get_session
from .models import Parameter
from .schemas import ParameterInSchema, ParameterOutSchema



bp = Blueprint("api", __name__, url_prefix="/v1")


@bp.get("/health")
def health():
    return {"status": "ok"}, 200


@bp.post("/parameters")
def create_param():
    payload = request.get_json() or {}
    data = ParameterInSchema().load(payload)
    session = get_session()()
    try:
        p = Parameter(name=data["name"], value=data["value"], value_type=data["value_type"])
        session.add(p)
        session.commit()
    except IntegrityError:
        session.rollback()
        return jsonify({"error": "parameter with this name already exists"}), 409
    out = ParameterOutSchema().dump(p)
    return jsonify(out), 201


@bp.get("/parameters")
def list_params():
    session = get_session()()
    q = session.query(Parameter)
    name = request.args.get("name")
    if name:
        q = q.filter(Parameter.name == name)
    items = q.order_by(Parameter.id.asc()).all()
    out = ParameterOutSchema(many=True).dump(items)
    return jsonify(out), 200


@bp.get("/parameters/<string:name>")
def get_param(name: str):
    session = get_session()()
    p = session.query(Parameter).filter_by(name=name).first()
    if not p:
        return jsonify({"error": "not found"}), 404
    return jsonify(ParameterOutSchema().dump(p)), 200


@bp.put("/parameters/<string:name>")
@bp.patch("/parameters/<string:name>")
def update_param(name: str):
    payload = request.get_json() or {}
    data = ParameterInSchema(partial=(request.method == "PATCH")).load({**payload, "name": name})
    session = get_session()()
    p = session.query(Parameter).filter_by(name=name).first()
    if not p:
        return jsonify({"error": "not found"}), 404
    p.value = data["value"]
    p.value_type = data["value_type"]
    session.commit()
    return jsonify(ParameterOutSchema().dump(p)), 200