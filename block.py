import time

def mine_block(last_block, data):
    """
    Mine a block based on given last_block and data.
    """
    timestamp = time.time_ns()
    last_hash = last_block.last_hash
    hash = f'{timestamp}-{last_hash}'
    
    return Block(timestamp, last_hash, hash, data)

def genesis():
    """
    Generate the genesis block.
    """
    return Block(1, 'genesis_last_hash', 'genesis_hash', [])
    

class Block:
    """
    Block: a unit of storage.
    Store transactions in a blcokchain that supports a cryptocurrency.
    """
    def __init__(self,timestamp, last_hash, hash, data):
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp},'
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash},'
            f'data: {self.data},'
        )

def main():
    genesis_block = genesis()
    block = mine_block(genesis_block, 'foo')
    print(block)

if __name__ == '__main__':
    main()