from crypt import methods
from pickle import GET
from flask import Blueprint, jsonify, abort, request
from ..models import Reviews, db
import sqlalchemy

bp = Blueprint('reviews', __name__, url_prefix='/reviews')


@bp.route('', methods=[GET])
def index():
    reviews = Reviews.query.all()
    result = []
    for review in reviews:
        result.append(reviews.serialize())
    return jsonify(result)

# @bp.route('', methods=['GET'])
# def index():
#     customers = Customers.query.all()
#     result = []
#     for customer in customers:
#         result.append(customer.serialize())
#     return jsonify(result)
