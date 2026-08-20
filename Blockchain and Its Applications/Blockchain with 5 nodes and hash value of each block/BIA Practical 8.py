import hashlib
import datetime

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = str(datetime.datetime.now())
        self.transactions = transactions if isinstance(transactions, list) else [transactions]
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

    def print_hashes(self):
        print("\nHashes of All Blocks in the Blockchain:\n")
        for block in self.chain:
            print(f"Block {block.index}, Hash: {block.hash}")

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

my_blockchain = Blockchain()
my_blockchain.add_block("Block 1 Data: Alice pays Bob 5 BTC")
my_blockchain.add_block("Block 2 Data: Bob pays Charlie 2 BTC")
my_blockchain.add_block("Block 3 Data: Charlie pays Donald 1 BTC")
my_blockchain.add_block("Block 4 Data: Donald pays Emma 0.5 BTC")
my_blockchain.print_hashes()
print("\nChecking Blockchain Validity...")
if my_blockchain.is_chain_valid():
    print("Blockchain is VALID!")
else:
    print("Blockchain is INVALID!")
    
