import hashlib
import datetime


class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index) +
            self.timestamp +
            str(self.transactions) +
            self.previous_hash
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transactions):
        previous_hash = self.get_latest_block().hash
        new_block = Block(len(self.chain), transactions, previous_hash)
        self.chain.append(new_block)

    def display_chain(self):
        for block in self.chain:
            print(f"Block Number: {block.index}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Transactions: {block.transactions}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Block Hash: {block.hash}")
            print("\n")

my_blockchain = Blockchain()

my_blockchain.add_block(["Alice pays Bob 5 BTC", "Bob pays Charlie 2 BTC"])
my_blockchain.add_block(["Charlie pays Donald 1 BTXC"])
my_blockchain.add_block(["Donald pays Emma 0.5 BTC", "Emma pays Fred 0.1 BTC"])

my_blockchain.display_chain()
