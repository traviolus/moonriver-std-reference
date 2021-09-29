# MoonRiver-std-reference

## Standard Reference Dataset Contract Info

### Data Available

The price data originates from [data requests](https://github.com/bandprotocol/bandchain/wiki/System-Overview#oracle-data-request) made on BandChain and then sent to Band's [StdReferenceBasic](https://moonriver.subscan.io/account/0xe89EA92AcA177B487F9c3502a7Cb9D76Dc5F5d84) contract on MoonRiver then retrieves and stores the results of those requests. Specifically, the following price pairs are available to be read from the [StdReferenceProxy](https://moonriver.subscan.io/account/0x75B01902D9297fD381bcF3B155a8cEAC78F5A35E) contract:

For example

- BTC/USDT
- ETH/USDC

These prices are automatically updated every hour. The [StdReferenceProxy](https://moonriver.subscan.io/account/0x75B01902D9297fD381bcF3B155a8cEAC78F5A35E) itself is currently deployed on MoonRiver at [`0x75B01902D9297fD381bcF3B155a8cEAC78F5A35E`](https://finder.terra.money/tequila-0004/address/terra16xjp4p3n4e29wgkqhjkxv2xn2q9z7jxzqgsyv9).

The prices themselves are the median of the values retrieved by BandChain's validators from many sources including [CoinGecko](https://www.coingecko.com/api/documentations/v3), [CryptoCompare](https://min-api.cryptocompare.com/), [Binance](https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md), [CoinMarketcap](https://coinmarketcap.com/), [HuobiPro](https://www.huobi.vc/en-us/exchange/), [CoinBasePro](https://pro.coinbase.com/), [Kraken](https://www.kraken.com/), [Bitfinex](https://www.bitfinex.com/), [Bittrex](https://global.bittrex.com/), [BITSTAMP](https://www.bitstamp.net/), [OKEX](https://www.okex.com/), [FTX](https://ftx.com/), [HitBTC](https://hitbtc.com/), [ItBit](https://www.itbit.com/), [Bithumb](https://www.bithumb.com/), [CoinOne](https://coinone.co.kr/). The data request is then made by executing Band's aggregator oracle script, the code of which you can view on Band's [mainnet](https://cosmoscan.io/oracle-script/3). Along with the price data, developers will also have access to the latest timestamp the price was updated.

### Standard Reference Dataset Contract Price Update Process

For the ease of development, the Band Foundation will be maintaining and updating the [StdReferenceBasic](https://moonriver.subscan.io/account/0xe89EA92AcA177B487F9c3502a7Cb9D76Dc5F5d84) contract with the latest price data. In the near future, we will be releasing guides on how developers can create similar contracts themselves to retrieve data from Band's oracle.

## List of Band oracle contracts on MoonRiver

| Deployed contracts | Address  |
|--------------------|---|
| StdReferenceProxy  | [0x75B01902D9297fD381bcF3B155a8cEAC78F5A35E](https://moonriver.subscan.io/account/0x75B01902D9297fD381bcF3B155a8cEAC78F5A35E)  |
