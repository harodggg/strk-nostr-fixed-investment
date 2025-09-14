import asyncio
import time

import get_reward_information

from starknet_py.contract import Contract
from typing import Union
from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient

from starknet_py.net.signer.key_pair import KeyPair
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.client_models import Call
from starknet_py.net.client_models import ResourceBounds, ResourceBoundsMapping


FULLNODE_RPC = "http://pathfinder.xxxyyy.space/rpc/v0_9"
client = FullNodeClient(node_url=FULLNODE_RPC)

# nostr lend contract
LEND_NOSTRA_CONTRACT = 0x0453c4c996f1047d9370f824d68145bd5e7ce12d00437140ad02181e1d11dc83

STARK_CONTRACT = 0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d
USDT_CONTRACT = 0x068F5c6a61780768455de69077E07e89787839bf8166dEcfBf92B645209c0fB8

MY_ACCOUNT_KEY = {
    "private_key": 0x035f14e889fd9a4fdaaf864922058771494de73a76843080153d6c4994acd107,

    "address": 0x041c3e6df37144f2287924103d2ced9e2e83a945bb72febf2b4c8a5571a100ac
}


async def claim_all(reward_infos):
    account = Account(
        address=MY_ACCOUNT_KEY["address"], client=client, key_pair=KeyPair.from_private_key(MY_ACCOUNT_KEY["private_key"]), chain=StarknetChainId.MAINNET)

    calls = []
    for r in reward_infos:
        # Create contract from contract's address - Contract will download contract's ABI to know its interface.
        claim_contract = await Contract.from_address(address=r["rewardContract"], provider=account)
        call = claim_contract.functions["claim"].prepare_invoke_v3(
            int(r["reward"]), [bytes.fromhex(c.lstrip("0x")) for c in r["proofs"]])
        calls.append(call)

    # transaction_response = await account.execute_v3(
    #    calls = calls,
    #    auto_estimate = True
    # )
    print(calls)

if __name__ == '__main__':
    asyncio.run(claim_all(get_reward_information.get_reward_infos()))
