from flask import Blueprint, request

# from app import db

from flask import jsonify

bp=Blueprint('shoebot', __name__)

@bp.route('/user_request', methods=['GET', 'POST'])
def user_request():
    
    # Get text message from request body
    text = request.form.get('text')

    # Make call to openAI API


    # Get top 5 products and return those

    return jsonify({"text": "Product_Objects"})