import struct
import re
from config import DATA_START, DATA_END, DATA_STRUCTURE, TIMESTAMP, ID\
    , INTERPRETER_PATH, DB_PATH, DB_TARGET_PATH
from canmatrix.convert import convert as cm_convert
import json

def log2spi(line):
    # valid line ???
    if 'Tx' in line:
        line = line.strip(' ')
        data_arg = []
        split_data = re.findall(r'\w+\.?\w*', line)
        data_arg.append(float(split_data[TIMESTAMP]))
        data_arg.append(int(split_data[ID]))
        for _ in split_data[DATA_START:DATA_END]:
            data_arg.append(int(_, base=16))

        spi_data = struct.pack(DATA_STRUCTURE, *data_arg)
        return spi_data

def dbc2json():
    cm_convert(DB_PATH, DB_TARGET_PATH)
    with open(DB_TARGET_PATH, 'r') as db_json_fp:
        db_data = json.load(db_json_fp)
    print(db_data)
    return db_data

def get_signals(db_data):
    for msg in db_data['messages']:
        print(msg['name'])
        for sig in msg['signals']:
            print('\t', sig['name'])

if __name__ == '__main__':
    # line = '0.050251 1  5               Tx   d 8 00 00 00 00 00 00 00 00  Length = 244000 BitCount = 125 ID = 5'
    # log2spi(line)
    json_data = dbc2json()
    get_signals(json_data)
