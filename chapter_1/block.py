import hashlib
import json


class Block:
    id = None
    history = None
    parent_id = None
    parent_hash = None

    @staticmethod
    def get_hash(obj):
        return hashlib.sha256(json.dumps(obj.__dict__).encode('utf-8')).hexdigest()

block_a = Block()
block_a.id = 1
block_a.history = 'Nelson likes cats'

block_b = Block()
block_b.id = 2
block_b.history = 'Marie likes dog'
block_b.parent_id = 1
block_b.parent_hash = Block.get_hash(block_a)

block_c = Block()
block_c.id = 3
block_c.history = 'Sky hates dog'
block_c.parent_id = 2
block_c.parent_hash = Block.get_hash(block_b)

# Change history and compare hashes
print(f'Before history change: {Block.get_hash(block_b) == block_c.parent_hash}')
block_b.history = 'Tempered history'
print(f'Before history change: {Block.get_hash(block_b) == block_c.parent_hash}')

