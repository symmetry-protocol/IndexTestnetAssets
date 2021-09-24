


# updates the list with new solana ecosystem tokens

from main import get_solana, combine_with_assets

print('getting solana coins and combining them to the json dict')
coins = get_solana()
combine_with_assets(coins)