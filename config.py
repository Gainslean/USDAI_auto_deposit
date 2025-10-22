import json

chain_name = {
    'Arbitrum': "Arbitrum",
    'Optimism': "Optimism",
    'Base': "Base",
    'Polygon': "Polygon",
    'Ethereum': "Ethereum",
    'Avalance': "Avalance",
    'Zora': "Zora",
    'Berachain': "Berachain",
    'BNB': "BNB",
    'Scroll': "Scroll",
    'Abstract': "Abstract",
    'Karak': "Karak"
}

rpc_url = {
    'Arbitrum': "https://rpc.ankr.com/arbitrum/",
    'Optimism': "https://rpc.ankr.com/optimism/",
    'Base': "https://rpc.ankr.com/base/",
    'Polygon': "https://rpc.ankr.com/polygon/",
    'Ethereum': "https://rpc.ankr.com/eth/",
    'Avalance': "https://rpc.ankr.com/avalanche/",
    'Scroll': "https://rpc.ankr.com/scroll/",
    'Abstract': "https://api.mainnet.abs.xyz",
    'Mantle': "https://rpc.ankr.com/mantle/",
    'Berachain': "https://berachain.leakedrpc.com",
    'BNB': "https://rpc.ankr.com/bsc/",
    'Zora': "wss://zora.drpc.org",
    'Karak': "https://rpc.karak.network"
}

explorer_url = {
    'Arbitrum': "https://arbiscan.io/",
    'Optimism': "https://optimistic.etherscan.io/",
    'Base': "https://basescan.org/",
    'Scroll': "https://scrollscan.org/",
    'Polygon': "https://polygonscan.com/",
    'Ethereum': "https://etherscan.io/",
    'Avalance': "https://www.oklink.com/ru/avax/",
    'Mantle': "https://explorer.mantle.xyz/",
    'Abstract': "https://abscan.org/",
    'Berachain': "https://berachain.leakedrpc.com",
    'BNB': "https://api.mainnet.abs.xyz",
    'Zora': "https://zora.drpc.org",
    'Karak': "https://explorer.karak.network "
}

Chain_id = {
    'Ethereum': 1,
    'Optimism': 10,
    'Arbitrum': 42161,
    'Base': 8453,
    'Polygon': 137,
    'Linea': 59144,
    'Blast': 81457,
    'Mantle': 5000,
    'Avalance': 43114,
    'Abstract': 2741,
    'Scroll': 534352,
    'Berachain': 80094,
    'BNB': 56,
    'Zora': 7777777,
    'Karak': 2410
    }


ETH_MASK = "0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE"
ZERO_ADDRESS = "0x0000000000000000000000000000000000000000"


USDC = {
    'Arbitrum': "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
    'Optimism': "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
    'Base': "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    'Polygon': "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
    'Ethereum': "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
    'Avalance': "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E"
    }



with open('abis/abi.json') as file:
    ERC20_ABI = json.load(file)


with open('abis/usdai.json') as file:
    USDAI = json.load(file)


