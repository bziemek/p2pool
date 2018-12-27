from p2pool.bitcoin import networks

PARENT = networks.nets['litecoincash_testnet']

P2P_PORT = 62466
WORKER_PORT = 15555

SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 150 # shares
SPREAD = 7 # blocks
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1

VERSION_CHECK = lambda v: None if 150001 <= v else 'Litecoin Cash version too old. Upgrade to 0.15.0.1 or newer!'
VERSION_WARNING = lambda v: None if 160002 <= v else 'Litecoin Cash version out of date. Upgrade to 0.16.0.2 or newer ASAP!'
SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit', 'hive'])
MINIMUM_PROTOCOL_VERSION = 3301
NEW_MINIMUM_PROTOCOL_VERSION = 3302
SEGWIT_ACTIVATION_VERSION = 33
BLOCK_MAX_SIZE = 4000000
BLOCK_MAX_WEIGHT = 4000000

BOOTSTRAP_ADDRS = []
ANNOUNCE_CHANNEL = '#p2pool-lcc-alt'

IDENTIFIER = '17b751fd110a4637'.decode('hex')
PREFIX = 'fc962530dd5c11ef'.decode('hex')

PERSIST = True
