"""Create a blockchain."""

import datetime  # datetime functions
import hashlib  # for hashing
import json  # for json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse


class Blockchain:
    """Classic blockchain."""

    def __init__(self):
        """Initialize chain and set genesis block."""
        self.chain = []

        self.transactions = []

        # create genesis block
        self.create_block(proof=1, previous_hash='0')

        # the nodes of our blockchain network
        self.nodes = set()

    def create_block(self, proof, previous_hash):
        """Add block to the blockchain."""
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}

        # clear tansactions
        self.transactions = []

        self.chain.append(block)
        return block

    def get_previous_block(self):
        """Get the latest block from the chain."""
        return self.chain[-1]

    @staticmethod
    def proof_of_work(previous_proof):
        """Get the proof of work before we add to the block."""
        # initialize proof
        new_proof = 1

        # turns true once proof is valid
        check_proof = False

        # loop till proof of work problem is solved
        while check_proof is False:

            # generate hash from new_proof and previous_proof
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()

            # if number has 4 zeros in front
            # then proof of work problem is solved
            if hash_operation[:4] == '0000':
                check_proof = True
            # else try a new one
            else:
                new_proof += 1

        return new_proof

    @staticmethod
    def hash(block):
        """Retrurn hash from block."""
        encoded_block = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        """Check if entire block chain is valid."""
        # start with the genesis block
        previous_block = chain[0]

        block_index = 1
        while block_index < len(chain):
            # next block
            block = chain[block_index]

            # if previous_hash does not match hash of previous block
            # then we know someone was messsing with the block chain
            if block['previous_hash'] != self.hash(previous_block):
                return False

            # check if proof is valid.
            previous_proof = previous_block['proof']
            proof = block['proof']

            # verify proof
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()

            if hash_operation[:4] != '0000':
                return False

            # move on to the next block
            previous_block = block
            block_index += 1

        return True

    def add_transaction(self, sender, receiver, amount):
        """Create transactions."""
        self.transactions.append(
            {'sender': sender, 'receiver': receiver, 'amount': amount})

        previous_block = self.get_previous_block()

        # return index of next block tansaction will be added to
        return previous_block['index'] + 1

    def add_nodes(self, address):
        """Add node to blockchain network."""
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        """Replace the chain with the longest chain from the network."""
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)

        for node in network:
            response = requests.get(f"http://{node}/get_chain")
            if response.status_code = 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_lenght = length
                    longest_chain = chain

        if longest_chain:
            self.chain = longest_chain
            return True

        return False


        # flask
app = Flask(__name__)

node_address = str(uuid4()).replace('-', '')

# create blockchain
blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    """Add a block to the blockchain."""
    # get previous block and proof
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']

    # first generate the proof of work so that we can add to this chain
    proof = blockchain.proof_of_work(previous_proof)

    # generate the hash from the previous bloc
    previous_hash = blockchain.hash(previous_block)

    # give minner some crypto
    blockchain.add_transaction(
        sender=node_address, receiver='Diego', ammount=1)

    # add block to blockchain
    block = blockchain.create_block(proof, previous_hash)

    # send a response back
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}

    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    """Retrun the blockchain."""
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}

    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    """Check if blockchain is valid."""
    is_chain_valid = blockchain.is_chain_valid(blockchain.chain)

    if is_chain_valid:
        response = {'message': 'block chain is valid'}
    else:
        response = {'message': 'block chain  is not valid'}

    return jsonify(response), 200


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    json = request.get_json()
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return "some elements are missing.", 400

    index = blockchain.add_transaction(
        json['sender'], json['receiver'], json['amount'])

    response = {'message': f"This transaction will be added to Block {index}"}
    return jsonfy(response), 201


# so that I can print json
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

app.run(host='0.0.0.0', port=5000)
