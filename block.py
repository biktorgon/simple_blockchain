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
    try:
        blocks = sorted(blocks, key=int)
    except ValueError:
        results.append({'block': 'Error', 'result': 'The file name must contain only digits'})
        blocks = []

    for block in blocks[1:]:
        with open('/'.join((BLOCKS_DIR, block)), 'r') as current_block:
            block_data = json.load(current_block)

        prev_block = str(int(block) - 1)
        try:
            actual_hash = get_hash(prev_block)
        except FileNotFoundError:
            results.append({'block': 'Error', 'result': 'File not found! Blockchain is broken'})
            break
        except PermissionError:
            results.append({'block': 'Error', 'result': 'Permission error'})
            break

        if block_data['hash'] == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        results.append({'block': prev_block, 'result': res})

    return results


def write_block_transact(who, amount, to_whom):
    block = 0
    blocks = os.listdir(BLOCKS_DIR)
    block_hash = ''
    try:
        blocks = sorted(blocks, key=int)
    except ValueError:
        raise ValueError('The file name must contain only digits')

    if len(blocks) > 0:
        block = blocks[-1]
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
