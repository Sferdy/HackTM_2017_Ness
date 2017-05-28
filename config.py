from os.path import dirname, abspath, join

SERVER_IP = '10.1.0.16'
PORT = 9999

SERVER_ADDR = (SERVER_IP, PORT)

TIMESTAMP = 0
ID = 2
DATA_START = 6
DATA_END = 14

DATA_STRUCTURE = 'fBBBBBBBBB'

BASE_PATH = dirname(abspath(__file__))
DB_PATH = join(BASE_PATH, 'CANoe/HackTM_DBC/HTM2017.dbc')
DB_TARGET_PATH = join(BASE_PATH, 'CANoe/HackTM_DBC/HTM2017.json')
LOG_PATH = join(BASE_PATH, 'CANoe/HackTM2017_CANoe_Log/Logging.asc')
INTERPRETER_PATH = join(BASE_PATH, 'venv/bin/python')


