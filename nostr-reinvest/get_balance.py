import asyncio


from starknet_py.contract import Contract
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient

from starknet_py.net.signer.key_pair import KeyPair
from starknet_py.net.models.chains import StarknetChainId


FULLNODE_RPC = "http://pathfinder.xxxyyy.space/rpc/v0_9"
client = FullNodeClient(node_url=FULLNODE_RPC)


async def get_strk_balance(address):
    key = 0x035f14e889fd9a4fdaaf864922058771494de73a76843080153d6c4994acd107

    account = Account(
        address=0x041c3e6df37144f2287924103d2ced9e2e83a945bb72febf2b4c8a5571a100ac, client=client, key_pair=KeyPair.from_private_key(key), chain=StarknetChainId.MAINNET)
    # Create contract from contract's address - Contract will download contract's ABI to know its interface.
    contract = await Contract.from_address(address=0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d, provider=account)

    call_result = await contract.functions["balanceOf"].call(
        address)
    return (call_result[0] / pow(10, 18))


async def get_usdt_balance(address):
    usdt_contract_address = 0x068F5c6a61780768455de69077E07e89787839bf8166dEcfBf92B645209c0fB8
    key = 0x035f14e889fd9a4fdaaf864922058771494de73a76843080153d6c4994acd107

    account = Account(
        address=0x041c3e6df37144f2287924103d2ced9e2e83a945bb72febf2b4c8a5571a100ac, client=client, key_pair=KeyPair.from_private_key(key), chain=StarknetChainId.MAINNET)
    # Create contract from contract's address - Contract will download contract's ABI to know its interface.
    contract = await Contract.from_address(address=usdt_contract_address, provider=account)

    call_result = await contract.functions["balanceOf"].call(
        address)
    return (call_result[0] / pow(10, 6))

if __name__ == '__main__':
    asyncio.run(get_usdt_balance(
        0x0729373f0e1e4e9ba6f8923d0e089a63625258ec8d0649ad4456b1c6f4b417b9
    ))
