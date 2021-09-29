import json
from typing import List
from web3 import Web3

web3 = Web3(Web3.HTTPProvider("https://rpc.moonriver.moonbeam.network"))
proxy_contract_address = "0x75B01902D9297fD381bcF3B155a8cEAC78F5A35E"
with open("abi.json") as f:
    contract_abi = json.load(f)


def get_reference_data(base: str, quote: str) -> None:
    print(f'Making a getReferenceData call to a proxy contract at address: {proxy_contract_address}')

    # Create Contract Instance
    oracle = web3.eth.contract(address=proxy_contract_address, abi=contract_abi)

    # Call Contract
    result = oracle.functions.getReferenceData(base, quote).call()

    print(f'Rate: {result[0]}\nLast updated base: {result[1]}\nLast updated quote: {result[2]}\n')


def get_reference_data_bulk(base: List[str], quote: List[str]) -> None:
    print(f'Making a getReferenceDataBulk call to a proxy contract at address: {proxy_contract_address}')

    # Create Contract Instance
    oracle = web3.eth.contract(address=proxy_contract_address, abi=contract_abi)

    # Call Contract
    results = oracle.functions.getReferenceDataBulk(base, quote).call()

    for result in results:
        print(f'Rate: {result[0]}\nLast updated base: {result[1]}\nLast updated quote: {result[2]}\n')


if __name__ == "__main__":
    get_reference_data("ETH", "DAI")
    get_reference_data_bulk(["BTC", "ETH"], ["USDT", "USDC"])
