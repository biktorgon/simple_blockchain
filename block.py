import json
import os
import hashlib


BLOCKS_DIR = '/'.join((os.curdir, 'blockchain_transact'))


def get_hash(file_name):
    with open('/'.join((BLOCKS_DIR, file_name)), 'rb') as block:
        return hashlib.md5(block.read()).hexdigest()


def check_blocks_hash():
    results = []
    blocks = os.listdir(BLOCKS_DIR)
    blocks = sorted(blocks, key=int)

    for block in blocks[1:]:
        with open('/'.join((BLOCKS_DIR, block)), 'r') as current_block:
            block_data = json.load(current_block)
            prev_block = str(int(block) - 1)
            actual_hash = get_hash(prev_block)

            if block_data['hash'] == actual_hash:
                res = 'Ok'
            else:
                res = 'Corrupted'

            results.append({'block': prev_block, 'result': res})

    return results


def write_block_transact(who, amount, to_whom, block_hash=''):
    block = 0
    blocks = os.listdir(BLOCKS_DIR)

    if len(blocks) != 0:
        block = sorted(blocks, key=int)[-1]
        if not block_hash:
            block_hash = get_hash(block)

    new_block = str(int(block) + 1)
    data = {
        'name': who,
        'amount': amount,
        'to_whom': to_whom,
        'hash': block_hash
    }

    with open('/'.join((BLOCKS_DIR, new_block)), 'w') as block:
        json.dump(data, block, indent=4, ensure_ascii=False)
