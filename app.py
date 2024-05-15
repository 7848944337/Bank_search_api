from flask import Flask, jsonify
from sqlalchemy.exc import SQLAlchemyError
from flask_cors import CORS
from config import Config
from models import db, Bank, Branch



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
CORS(app) 

@app.route('/banks', methods=['GET'])
def get_banks():
    try:
        banks = Bank.query.all()
        banks_list = [{'id': bank.id, 'name': bank.name} for bank in banks]
        return jsonify(banks_list)
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@app.route('/branches/<bank_id>', methods=['GET'])
def get_branch_details(bank_id):
    try:
        branches = Branch.query.filter_by(bank_id=bank_id).all()
        if not branches:
            return jsonify({'error': 'No branches found for this bank'}), 404

        branch_details = []
        for branch in branches:
            branch_details.append({
                'ifsc': branch.ifsc,
                'bank_id': branch.bank_id,
                'branch': branch.branch,
                'address': branch.address,
                'city': branch.city,
                'district': branch.district,
                'state': branch.state,
                'bank_name': branch.bank_name
            })
        return jsonify(branch_details)
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'Running'}), 200


