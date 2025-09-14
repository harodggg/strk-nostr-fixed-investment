import requests


NOSTRA_API = "https://api.nostra.finance//query/find"


def get_reward_period():
    json = {"database": "prod-a-nostra-db", "collection": "rewardPeriods"}
    req = requests.post(NOSTRA_API, json=json)
    return [c for c in req.json()["documents"] if c["rewardType"] == "LEND" and 'defiSpringRewardsDistributor' in c]


def get_proof():
    json = {"database": "prod-a-nostra-db", "collection": "rewardProofs", "filter": {
        "account": "0x0729373f0e1e4e9ba6f8923d0e089a63625258ec8d0649ad4456b1c6f4b417b9"}}
    req = requests.post(NOSTRA_API, json=json)
    return [c for c in req.json()["documents"]]


def get_reward_infos():
    reward_contracts = [{"rewardId": c["start"]+"_" + c["end"] + "_" +
                         c["rewardType"], "rewardContract": c["defiSpringRewardsDistributor"]} for c in get_reward_period()]

    proof_infos = [{"rewardId": c["rewardId"],
                    "account": c["account"], "proofs": c["proofs"], "reward": c["reward"]}for c in get_proof()]

    reward_infos = []

    for r in reward_contracts:
        for p in proof_infos:
            if r["rewardId"] == p["rewardId"]:
                reward_infos.append(r | p)
    return reward_infos
