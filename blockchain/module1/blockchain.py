"""
doc string
"""

import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:
    """ class block string """

    def __init__(self):
        """ initialize chain """

        self.chain = []

        # create genesis block
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        """ add block to the blockchain """

        # create a block:
        #   the previous_hash is for security, if someone tried
        #   to change the data then the previous_hash of next block
        #   would not match,
        #   this is a way to make sure no one is messing with the block chain

        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}

        self.chain.append(block)
        return block

    def get_previous_block(self):
        """ get the latest block from the chain """
        # get the last item in the chain
        return self.chain[-1]

    @staticmethod
    def proof_of_work(previous_proof):
        """ get the proof of work before we add to the block """

        new_proof = 1
        check_proof = False

        # loop till proof of work problem is solved
        while check_proof is False:

            # generate hash from new_proof and previous_proof
            # math operation must me none symetrical
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
        """ generate hash from block """

        # encodeing that sha256 is expecting
        encoded_block = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        """ check if entire block chain is valid """

        # start with the genesis block
        previous_block = chain[0]

        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]

            # if previous_hash does not match hash of previous block
            # then we know someone was messsing with the block chain
            # hashing is hard to generate but easy to check
            if block['previous_hash'] != self.hash(previous_block):
                return False

            # check if proof is valid
            #   get previous proof and current proof
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


# flask
app = Flask(__name__)

# create blockchain
blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
def mine_block():
    """ add a block to the blockchain """

    # get previous block and it's proof
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']

    # first generate the proof of work so that we can add to this chain
    proof = blockchain.proof_of_work(previous_proof)

    # generate the hash from the previous bloc
    previous_hash = blockchain.hash(previous_block)

    # add block to blockchain
    block = blockchain.create_block(proof, previous_hash)

    # send a response back
    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash']}
    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
def get_chain():
    """ get_chain """
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/is_valid', methods=['GET'])
def is_valid():
    """ check if blockchain is valid """

    is_chain_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_chain_valid:
        response = {'message': 'block chain is valid'}
    else:
        response = {'message': 'block chain  is not valid'}
    return jsonify(response), 200




# so that I can print json
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

app.run(host='0.0.0.0', port=5000)
