import json
import os
import hashlib


TRANSACT_DIR = os.curdir + '/blockchain_transact/'


def get_hash(file_name):
    file = open(TRANSACT_DIR + file_name, 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_blocks_hash():
    results = []
    blocks = os.listdir(TRANSACT_DIR)
    blocks = sorted(blocks, key=int)

    for block in blocks[1:]:
        with open(TRANSACT_DIR + block) as current_block:
            current_block_data = json.load(current_block)
            prev_block = str(int(block) - 1)
            actual_hash = get_hash(prev_block)

            if current_block_data['hash'] == actual_hash:
                res = 'Ok'
            else:
                res = 'Corrupted'

            results.append({'block': prev_block, 'result': res})

    return results


def write_block_transact(who, amount, to_whom, block_hash=''):
    block = 0
    blocks = os.listdir(TRANSACT_DIR)

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

    with open(TRANSACT_DIR + new_block, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
