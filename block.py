import json
import os
import hashlib


TRANSACT_DIR = os.curdir + '/blockchain_transact/'


def get_hash(file_name):
    file = open(TRANSACT_DIR + file_name, 'rb').read()
    return hashlib.md5(file).hexdigest()


def check_blocks_hash():
    results = []
    files = os.listdir(TRANSACT_DIR)
    files = sorted(files, key=int)

    for file in files[1:]:
        with open(TRANSACT_DIR + str(file)) as current_file:
            current_file_data = json.load(current_file)
            prev_file = str(int(file) - 1)
            actual_hash = get_hash(prev_file)

            if current_file_data['hash'] == actual_hash:
                res = 'Ok'
            else:
                res = 'Corrupted'

            results.append({'block': prev_file, 'result': res})

    return results


def write_file_transact(who, amount, to_whom, block_hash=''):
    file = 0
    files = os.listdir(TRANSACT_DIR)

    if len(files) != 0:
        file = sorted(files, key=int)[-1]
        if not block_hash:
            block_hash = get_hash(file)

    new_file = str(int(file) + 1)
    data = {
        'name': who,
        'amount': amount,
        'to_whom': to_whom,
        'hash': block_hash
    }

    with open(TRANSACT_DIR + new_file, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
