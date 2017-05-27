import struct
import re

TIMESTAMP = 0
ID = 2
DATA_START = 6
DATA_END = 14

DATA_STRUCTURE = 'fBBBBBBBBB'

def extract_data(line):
    # valid line ???
    if 'Tx' in line:
        line = line.strip(' ')
        data_arg = []
        split_data = re.findall(r'\w+\.?\w*', line)
        data_arg.append(float(split_data[TIMESTAMP]))
        data_arg.append(int(split_data[ID]))
        for _ in split_data[DATA_START:DATA_END]:
            data_arg.append(int(_))

        spi_data = struct.pack(DATA_STRUCTURE, *data_arg)
        return spi_data


if __name__ == '__main__':
    line = '0.050251 1  5               Tx   d 8 00 00 00 00 00 00 00 00  Length = 244000 BitCount = 125 ID = 5'
    extract_data(line)