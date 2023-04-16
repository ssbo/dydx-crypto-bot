from dydx3.constants import API_HOST_GOERLI, API_HOST_MAINNET
from decouple import config

MODE_DEVELOPMENT = "DEVELOPMENT"
MODE_PRODUCTION = "PRODUCTION"
SAVED = "saved"

BUY = "BUY"
SELL = "SELL"

# !!!! SELECT MODE !!!!
MODE = MODE_DEVELOPMENT

# Close all open positions and orders
ABORT_ALL_POSITIONS = False

# Find cointegrated pairs
FIND_COINTEGRATED = True

# Place trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1HOUR"

# Stats window
WINDOW = 21

# Thresholds - Opening
MAX_HALF_LIFE = 24
ZSCORE_THRESH = 1.5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1880

# Threshold - Closing
CLOSE_AT_ZSCORE_CROSS = True

ETHEREUM_ADDRESS = "0x1302753900Bf9E757FCae490CF7d50afAA8142f2"

STARK_PRIVATE_KEY_MAINNET = config("STARK_PRIVATE_KEY_MAINNET")
DYDX_API_KEY_MAINNET = config("DYDX_API_KEY_MAINNET")
DYDX_API_SECRET_MAINNET = config("DYDX_API_SECRET_MAINNET")
DYDX_API_PASSPHRASE_MAINNET = config("DYDX_API_PASSPHRASE_MAINNET")

# KEYS - Development
# Must to be on Testnet on DYDX

STARK_PRIVATE_KEY_TESTNET = config("STARK_PRIVATE_KEY_TESTNET")
DYDX_API_KEY_TESTNET = config("DYDX_API_KEY_TESTNET")
DYDX_API_SECRET_TESTNET = config("DYDX_API_SECRET_TESTNET")
DYDX_API_PASSPHRASE_TESTNET = config("DYDX_API_PASSPHRASE_TESTNET")

# KEYS - Export
STARK_PRIVATE_KEY  = STARK_PRIVATE_KEY_MAINNET if MODE == MODE_PRODUCTION else STARK_PRIVATE_KEY_TESTNET
DYDX_API_KEY  = DYDX_API_KEY_MAINNET if MODE == MODE_PRODUCTION else DYDX_API_KEY_TESTNET
DYDX_API_SECRET  = DYDX_API_SECRET_MAINNET if MODE == MODE_PRODUCTION else DYDX_API_SECRET_TESTNET
DYDX_API_PASSPHRASE  = DYDX_API_PASSPHRASE_MAINNET if MODE == MODE_PRODUCTION else DYDX_API_PASSPHRASE_TESTNET

# HOST - Export
HOST = API_HOST_MAINNET if MODE == MODE_PRODUCTION else API_HOST_GOERLI

# HTTP PROVIDER
HTTP_PROVIDER_MAINNET = "https://eth-mainnet.g.alchemy.com/v2/eioGiMtWAgf_fvocr9NynL8hfCYkdZ2k"
HTTP_PROVIDER_TESTNET = "https://eth-goerli.g.alchemy.com/v2/XE1i7-pVAmBemOKBn8I_60hPFhG1Edvf"
HTTP_PROVIDER = HTTP_PROVIDER_MAINNET if MODE == MODE_PRODUCTION else HTTP_PROVIDER_TESTNET