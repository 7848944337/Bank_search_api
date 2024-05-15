from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# Configure database URI using environment variable or provide a default value
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Bank(db.Model):
    __tablename__ = 'banks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Branch(db.Model):
    __tablename__ = 'branches'
    ifsc = db.Column(db.String(11), primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('banks.id'), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    city = db.Column(db.String(100))
    district = db.Column(db.String(100))
    state = db.Column(db.String(100))
    bank_name = db.Column(db.String(100), nullable=False)

@app.route('/banks', methods=['GET'])
def get_banks():
    banks = Bank.query.all()
    banks_list = [{'id': bank.id, 'name': bank.name} for bank in banks]
    return jsonify(banks_list)

@app.route('/branches/<bank_id>', methods=['GET'])
def get_branch_details(bank_id):
    branch = Branch.query.filter_by(bank_id=bank_id).first()
    if not branch:
        return jsonify({'error': 'Branch not found'}), 404

    branch_details = {
        'ifsc': branch.ifsc,
        'bank_id': branch.bank_id,
        'branch': branch.branch,
        'address': branch.address,
        'city': branch.city,
        'district': branch.district,
        'state': branch.state,
        'bank_name': branch.bank_name
    }
    return jsonify(branch_details)

if __name__ == '__main__':
    app.run(debug=True)
