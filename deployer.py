import asyncio
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.contract import Contract
from starknet_py.net.networks import TESTNET
from utils import str_to_felt

ERC20_FILE = ['contracts/MyToken.cairo']

ERC20_NAME = str_to_felt("Pharaoh")
ERC20_SYMBOL = str_to_felt("PRH")
DECIMALS = 18
INITIAL_SUPPLY = 210000000000000000

OWNER = 0x03E6eB63F21EaA80bEF27B1B5F7f93e2bD5fA59712D6566E701e5a6e8D122838
ALLOWED_AMOUNT = 1000
TIMEDELTA = 86400 #24h

async def deploy():
    client = GatewayClient(TESTNET)
    print("Deploying ERC20 Contract...")
    erc20_contract = await Contract.deploy(
        client=client,
        compilation_source=ERC20_FILE,
        constructor_args=[ERC20_NAME, ERC20_SYMBOL, DECIMALS, INITIAL_SUPPLY, OWNER]
    )
    print(f'✨ ERC20 Contract deployed at {hex(erc20_contract.deployed_contract.address)}')

    await erc20_contract.wait_for_acceptance()
    return (erc20_contract)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(deploy())
