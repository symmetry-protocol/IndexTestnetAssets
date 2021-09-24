# IndexTestnetAssets
List of tokens used for index testnet (public repo)



run ```solana_updater.py``` to add newer tokens into the list



data is stored in the following format:

```python
{
    "BTC": {"symbol": "BTC", "gecko_id": "bitcoin"},
    ... ,
    "TON": {"symbol": "TON", "gecko_id": "tokamak-network"},
    "TON_1": {"symbol": "TON", "gecko_id": "ton-crystal"},
    ...
}
```
So the keys are generally the same as symbols. But when the symbols are ambiguous,
"_<int>" suffix is added to the newer coin - like in the example of "TON"