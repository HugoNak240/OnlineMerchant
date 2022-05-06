from flask import Blueprint, jsonify, abort, request
from ..models import Customers, db
import sqlalchemy


bp = Blueprint('customers', __name__, url_prefix='/customers')

# GET method queries all customers  Good2Go 05/04/21

@bp.route('', methods=['GET'])
def index():
    customers = Customers.query.all()
    result = []
    for customer in customers:
        result.append(customer.serialize())
    return jsonify(result)


@bp.route('/add', methods=['POST'])
def create():

    if 'username' not in request.json or 'password' not in request.json or 'email'not in request.json or 'address' not in request.json:
        return abort(400)
    # if request.json['username'] in Customers.username:


    c = Customers(
        username=request.json['username'],
        password=request.json['password'],
        email=request.json['email'],
        address=request.json['address']
        )
    db.session.add(c)
    db.session.commit()
    return jsonify(c.serialize())

# @bp.route('', methods=[])
