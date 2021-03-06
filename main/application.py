import json
from urllib.parse import urlparse
from uuid import uuid4
from flask import Flask, jsonify, request

from blockchain.blockchain import Blockchain
from api.services.patient import PatientService

app = Flask(__name__)
node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain('resources/data.json')
patientService = PatientService()

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200, {'Access-Control-Allow-Origin': '*'} 

@app.route('/transactions', methods=['POST'])
def new_transaction():
    message = request.get_data(as_text=True)
    message = message.replace("\r\n", "\r").replace("\n", "\r")
    index = blockchain.new_transaction(message)
    patientService.save(message)
    response = {'message': f'Transaction will be added to Block {index}'}
    return jsonify(response), 201, {'Access-Control-Allow-Origin': '*'} 

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()

    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400

    for node in nodes:
        blockchain.register_node(node)

    response = {
        'message': 'New nodes have been added',
        'total_nodes': list(blockchain.nodes),
    }
    return jsonify(response), 201

@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()

    if replaced:
        response = {
            'message': 'Our chain was replaced',
            'new_chain': blockchain.chain
        }
    else:
        response = {
            'message': 'Our chain is authoritative',
            'chain': blockchain.chain
        }

    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000,
                        type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
