# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

from ccxt.base.exchange import Exchange
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import PermissionDenied
from ccxt.base.errors import AccountSuspended
from ccxt.base.errors import BadRequest
from ccxt.base.errors import BadSymbol
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import CancelPending
from ccxt.base.errors import RateLimitExceeded
from ccxt.base.errors import OnMaintenance
from ccxt.base.decimal_to_precision import TRUNCATE


class novadax(Exchange):

    def describe(self):
        return self.deep_extend(super(novadax, self).describe(), {
            'id': 'novadax',
            'name': 'NovaDAX',
            'countries': ['BR'],  # Brazil
            'rateLimit': 50,
            'version': 'v1',
            # new metainfo interface
            'has': {
                'CORS': False,
                'cancelOrder': True,
                'createOrder': True,
                'fetchAccounts': True,
                'fetchBalance': True,
                'fetchClosedOrders': True,
                'fetchMarkets': True,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrders': True,
                'fetchOrderTrades': True,
                'fetchOrderBook': True,
                'fetchTicker': True,
                'fetchTickers': True,
                'fetchTime': True,
                'fetchTrades': True,
                'withdraw': True,
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/1294454/92337550-2b085500-f0b3-11ea-98e7-5794fb07dd3b.jpg',
                'api': {
                    'public': 'https://api.novadax.com',
                    'private': 'https://api.novadax.com',
                },
                'www': 'https://www.novadax.com.br',
                'doc': [
                    'https://doc.novadax.com/pt-BR/',
                ],
                'fees': 'https://www.novadax.com.br/fees-and-limits',
                'referral': 'https://www.novadax.com.br/?s=ccxt',
            },
            'api': {
                'public': {
                    'get': [
                        'common/symbol',
                        'common/symbols',
                        'common/timestamp',
                        'market/tickers',
                        'market/ticker',
                        'market/depth',
                        'market/trades',
                    ],
                },
                'private': {
                    'get': [
                        'orders/get',
                        'orders/list',
                        'orders/fill',
                        'account/getBalance',
                        'account/subs',
                        'account/subs/balance',
                        'account/subs/transfer/record',
                    ],
                    'post': [
                        'orders/create',
                        'orders/cancel',
                        'account/withdraw/coin',
                        'account/subs/transfer',
                    ],
                },
            },
            'fees': {
                'trading': {
                    'tierBased': False,
                    'percentage': True,
                    'taker': 0.5 / 100,
                    'maker': 0.3 / 100,
                },
            },
            'requiredCredentials': {
                'apiKey': True,
                'secret': True,
            },
            'exceptions': {
                'exact': {
                    'A99999': ExchangeError,  # 500 Failed Internal error
                    # 'A10000': ExchangeError,  # 200 Success Successful request
                    'A10001': BadRequest,  # 400 Params error Parameter is invalid
                    'A10002': ExchangeError,  # 404 Api not found API used is irrelevant
                    'A10003': AuthenticationError,  # 403 Authentication failed Authentication is failed
                    'A10004': RateLimitExceeded,  # 429 Too many requests Too many requests are made
                    'A10005': PermissionDenied,  # 403 Kyc required Need to complete KYC firstly
                    'A10006': AccountSuspended,  # 403 Customer canceled Account is canceled
                    'A10007': BadRequest,  # 400 Account not exist Sub account does not exist
                    'A10011': BadSymbol,  # 400 Symbol not exist Trading symbol does not exist
                    'A10012': BadSymbol,  # 400 Symbol not trading Trading symbol is temporarily not available
                    'A10013': OnMaintenance,  # 503 Symbol maintain Trading symbol is in maintain
                    'A30001': OrderNotFound,  # 400 Order not found Queried order is not found
                    'A30002': InvalidOrder,  # 400 Order amount is too small Order amount is too small
                    'A30003': InvalidOrder,  # 400 Order amount is invalid Order amount is invalid
                    'A30004': InvalidOrder,  # 400 Order value is too small Order value is too small
                    'A30005': InvalidOrder,  # 400 Order value is invalid Order value is invalid
                    'A30006': InvalidOrder,  # 400 Order price is invalid Order price is invalid
                    'A30007': InsufficientFunds,  # 400 Insufficient balance The balance is insufficient
                    'A30008': InvalidOrder,  # 400 Order was closed The order has been executed
                    'A30009': InvalidOrder,  # 400 Order canceled The order has been cancelled
                    'A30010': CancelPending,  # 400 Order cancelling The order is being cancelled
                    'A30011': InvalidOrder,  # 400 Order price too high The order price is too high
                    'A30012': InvalidOrder,  # 400 Order price too low The order price is too low
                },
                'broad': {
                },
            },
            'commonCurrencies': {
            },
        })

    def fetch_time(self, params={}):
        response = self.publicGetCommonTimestamp(params)
        #
        #     {
        #         "code":"A10000",
        #         "data":1599090512080,
        #         "message":"Success"
        #     }
        #
        return self.safe_integer(response, 'data')

    def fetch_markets(self, params={}):
        response = self.publicGetCommonSymbols(params)
        #
        #     {
        #         "code":"A10000",
        #         "data":[
        #             {
        #                 "amountPrecision":8,
        #                 "baseCurrency":"BTC",
        #                 "minOrderAmount":"0.001",
        #                 "minOrderValue":"25",
        #                 "pricePrecision":2,
        #                 "quoteCurrency":"BRL",
        #                 "status":"ONLINE",
        #                 "symbol":"BTC_BRL",
        #                 "valuePrecision":2
        #             },
        #         ],
        #         "message":"Success"
        #     }
        #
        result = []
        data = self.safe_value(response, 'data', [])
        for i in range(0, len(data)):
            market = data[i]
            baseId = self.safe_string(market, 'baseCurrency')
            quoteId = self.safe_string(market, 'quoteCurrency')
            id = self.safe_string(market, 'symbol')
            base = self.safe_currency_code(baseId)
            quote = self.safe_currency_code(quoteId)
            symbol = base + '/' + quote
            precision = {
                'amount': self.safe_integer(market, 'amountPrecision'),
                'price': self.safe_integer(market, 'pricePrecision'),
                'cost': self.safe_integer(market, 'valuePrecision'),
            }
            limits = {
                'amount': {
                    'min': self.safe_float(market, 'minOrderAmount'),
                    'max': None,
                },
                'price': {
                    'min': None,
                    'max': None,
                },
                'cost': {
                    'min': self.safe_float(market, 'minOrderValue'),
                    'max': None,
                },
            }
            status = self.safe_string(market, 'status')
            active = (status == 'ONLINE')
            result.append({
                'id': id,
                'symbol': symbol,
                'base': base,
                'quote': quote,
                'baseId': baseId,
                'quoteId': quoteId,
                'precision': precision,
                'limits': limits,
                'info': market,
                'active': active,
            })
        return result

    def parse_ticker(self, ticker, market=None):
        #
        # fetchTicker, fetchTickers
        #
        #     {
        #         "ask":"61946.1",
        #         "baseVolume24h":"164.41930186",
        #         "bid":"61815",
        #         "high24h":"64930.72",
        #         "lastPrice":"61928.41",
        #         "low24h":"61156.32",
        #         "open24h":"64512.46",
        #         "quoteVolume24h":"10308157.95",
        #         "symbol":"BTC_BRL",
        #         "timestamp":1599091115090
        #     }
        #
        timestamp = self.safe_integer(ticker, 'timestamp')
        marketId = self.safe_string(ticker, 'symbol')
        symbol = None
        if marketId is not None:
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
            elif marketId is not None:
                baseId, quoteId = marketId.split('_')
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                symbol = base + '/' + quote
        if (symbol is None) and (market is not None):
            symbol = market['symbol']
        open = self.safe_float(ticker, 'open24h')
        last = self.safe_float(ticker, 'lastPrice')
        percentage = None
        change = None
        average = None
        if (last is not None) and (open is not None):
            change = last - open
            percentage = change / open * 100
            average = self.sum(last, open) / 2
        baseVolume = self.safe_float(ticker, 'baseVolume24h')
        quoteVolume = self.safe_float(ticker, 'quoteVolume24h')
        vwap = self.vwap(baseVolume, quoteVolume)
        return {
            'symbol': symbol,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'high': self.safe_float(ticker, 'high24h'),
            'low': self.safe_float(ticker, 'low24h'),
            'bid': self.safe_float(ticker, 'bid'),
            'bidVolume': None,
            'ask': self.safe_float(ticker, 'ask'),
            'askVolume': None,
            'vwap': vwap,
            'open': open,
            'close': last,
            'last': last,
            'previousClose': None,
            'change': change,
            'percentage': percentage,
            'average': average,
            'baseVolume': baseVolume,
            'quoteVolume': quoteVolume,
            'info': ticker,
        }

    def fetch_ticker(self, symbol, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        response = self.publicGetMarketTicker(self.extend(request, params))
        #
        #     {
        #         "code":"A10000",
        #         "data":{
        #             "ask":"61946.1",
        #             "baseVolume24h":"164.41930186",
        #             "bid":"61815",
        #             "high24h":"64930.72",
        #             "lastPrice":"61928.41",
        #             "low24h":"61156.32",
        #             "open24h":"64512.46",
        #             "quoteVolume24h":"10308157.95",
        #             "symbol":"BTC_BRL",
        #             "timestamp":1599091115090
        #         },
        #         "message":"Success"
        #     }
        #
        data = self.safe_value(response, 'data', {})
        return self.parse_ticker(data, market)

    def fetch_tickers(self, symbols=None, params={}):
        self.load_markets()
        response = self.publicGetMarketTickers(params)
        #
        #     {
        #         "code":"A10000",
        #         "data":[
        #             {
        #                 "ask":"61879.36",
        #                 "baseVolume24h":"164.40955092",
        #                 "bid":"61815",
        #                 "high24h":"64930.72",
        #                 "lastPrice":"61820.04",
        #                 "low24h":"61156.32",
        #                 "open24h":"64624.19",
        #                 "quoteVolume24h":"10307493.92",
        #                 "symbol":"BTC_BRL",
        #                 "timestamp":1599091291083
        #             },
        #         ],
        #         "message":"Success"
        #     }
        #
        data = self.safe_value(response, 'data', [])
        result = {}
        for i in range(0, len(data)):
            ticker = self.parse_ticker(data[i])
            symbol = ticker['symbol']
            result[symbol] = ticker
        return self.filter_by_array(result, 'symbol', symbols)

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        request = {
            'symbol': self.market_id(symbol),
        }
        if limit is not None:
            request['limit'] = limit  # default 10, max 20
        response = self.publicGetMarketDepth(self.extend(request, params))
        #
        #     {
        #         "code":"A10000",
        #         "data":{
        #             "asks":[
        #                 ["0.037159","0.3741"],
        #                 ["0.037215","0.2706"],
        #                 ["0.037222","1.8459"],
        #             ],
        #             "bids":[
        #                 ["0.037053","0.3857"],
        #                 ["0.036969","0.8101"],
        #                 ["0.036953","1.5226"],
        #             ],
        #             "timestamp":1599280414448
        #         },
        #         "message":"Success"
        #     }
        #
        data = self.safe_value(response, 'data', {})
        timestamp = self.safe_integer(data, 'timestamp')
        return self.parse_order_book(data, timestamp, 'bids', 'asks')

    def parse_trade(self, trade, market=None):
        #
        # public fetchTrades
        #
        #     {
        #         "amount":"0.0632",
        #         "price":"0.037288",
        #         "side":"BUY",
        #         "timestamp":1599279694576
        #     }
        #
        # private fetchOrderTrades
        #
        #     {
        #         "id": "608717046691139584",
        #         "orderId": "608716957545402368",
        #         "symbol": "BTC_BRL",
        #         "side": "BUY",
        #         "amount": "0.0988",
        #         "price": "45514.76",
        #         "fee": "0.0000988 BTC",
        #         "role": "MAKER",
        #         "timestamp": 1565171053345
        #     }
        #
        id = self.safe_string(trade, 'id')
        orderId = self.safe_string(trade, 'orderId')
        timestamp = self.safe_integer(trade, 'timestamp')
        side = self.safe_string_lower(trade, 'side')
        price = self.safe_float(trade, 'price')
        amount = self.safe_float(trade, 'amount')
        cost = self.safe_float(trade, 'volume')
        if (cost is None) and (amount is not None) and (price is not None):
            cost = amount * price
        marketId = self.safe_string(trade, 'symbol')
        symbol = None
        if marketId is not None:
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
                symbol = market['symbol']
            else:
                baseId, quoteId = marketId.split('_')
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                symbol = base + '/' + quote
        if (market is not None) and (symbol is None):
            symbol = market['symbol']
        takerOrMaker = self.safe_string_lower(trade, 'role')
        feeString = self.safe_string(trade, 'fee')
        fee = None
        if feeString is not None:
            parts = feeString.split(' ')
            feeCurrencyId = self.safe_string(parts, 1)
            feeCurrencyCode = self.safe_currency_code(feeCurrencyId)
            fee = {
                'cost': self.safe_float(parts, 0),
                'currency': feeCurrencyCode,
            }
        return {
            'id': id,
            'order': orderId,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': symbol,
            'type': None,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'takerOrMaker': takerOrMaker,
            'fee': fee,
            'info': trade,
        }

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        request = {
            'symbol': market['id'],
        }
        if limit is not None:
            request['limit'] = limit  # default 100
        response = self.publicGetMarketTrades(self.extend(request, params))
        #
        #     {
        #         "code":"A10000",
        #         "data":[
        #             {"amount":"0.0632","price":"0.037288","side":"BUY","timestamp":1599279694576},
        #             {"amount":"0.0052","price":"0.03715","side":"SELL","timestamp":1599276606852},
        #             {"amount":"0.0058","price":"0.037188","side":"SELL","timestamp":1599275187812},
        #         ],
        #         "message":"Success"
        #     }
        #
        data = self.safe_value(response, 'data', [])
        return self.parse_trades(data, market, since, limit)

    def fetch_balance(self, params={}):
        self.load_markets()
        response = self.privateGetAccountGetBalance(params)
        #
        #     {
        #         "code": "A10000",
        #         "data": [
        #             {
        #                 "available": "1.23",
        #                 "balance": "0.23",
        #                 "currency": "BTC",
        #                 "hold": "1"
        #             }
        #         ],
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data', [])
        result = {'info': response}
        for i in range(0, len(data)):
            balance = data[i]
            currencyId = self.safe_string(balance, 'currency')
            code = self.safe_currency_code(currencyId)
            account = self.account()
            account['total'] = self.safe_float(balance, 'available')
            account['free'] = self.safe_float(balance, 'balance')
            account['used'] = self.safe_float(balance, 'hold')
            result[code] = account
        return self.parse_balance(result)

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        uppercaseType = type.upper()
        uppercaseSide = side.upper()
        request = {
            'symbol': market['id'],
            'type': uppercaseType,  # LIMIT, MARKET
            'side': uppercaseSide,  # or SELL
            # 'accountId': '...',  # subaccount id, optional
            # 'amount': self.amount_to_precision(symbol, amount),
            # "price": "1234.5678",  # required for LIMIT and STOP orders
        }
        if uppercaseType == 'LIMIT':
            request['price'] = self.price_to_precision(symbol, price)
            request['amount'] = self.amount_to_precision(symbol, amount)
        elif uppercaseType == 'MARKET':
            if uppercaseSide == 'SELL':
                request['amount'] = self.amount_to_precision(symbol, amount)
            elif uppercaseSide == 'BUY':
                value = self.safe_float(params, 'value')
                createMarketBuyOrderRequiresPrice = self.safe_value(self.options, 'createMarketBuyOrderRequiresPrice', True)
                if createMarketBuyOrderRequiresPrice:
                    if price is not None:
                        if value is None:
                            value = amount * price
                    elif value is None:
                        raise InvalidOrder(self.id + " createOrder() requires the price argument with market buy orders to calculate total order cost(amount to spend), where cost = amount * price. Supply a price argument to createOrder() call if you want the cost to be calculated for you from price and amount, or, alternatively, add .options['createMarketBuyOrderRequiresPrice'] = False and supply the total cost value in the 'amount' argument or in the 'value' extra parameter(the exchange-specific behaviour)")
                else:
                    value = amount if (value is None) else value
                precision = market['precision']['price']
                request['value'] = self.decimal_to_precision(value, TRUNCATE, precision, self.precisionMode)
        response = self.privatePostOrdersCreate(self.extend(request, params))
        #
        #     {
        #         "code": "A10000",
        #         "data": {
        #             "amount": "0.001",
        #             "averagePrice": null,
        #             "filledAmount": "0",
        #             "filledFee": "0",
        #             "filledValue": "0",
        #             "id": "633679992971251712",
        #             "price": "35000",
        #             "side": "BUY",
        #             "status": "PROCESSING",
        #             "symbol": "BTC_BRL",
        #             "timestamp": 1571122683535,
        #             "type": "LIMIT",
        #             "value": "35"
        #         },
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data', {})
        return self.parse_order(data, market)

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'id': id,
        }
        response = self.privatePostOrdersCancel(self.extend(request, params))
        #
        #     {
        #         "code": "A10000",
        #         "data": {
        #             "result": True
        #         },
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data', {})
        return self.parse_order(data)

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        request = {
            'id': id,
        }
        response = self.privateGetOrdersGet(self.extend(request, params))
        #
        #     {
        #         "code": "A10000",
        #         "data": {
        #             "id": "608695623247466496",
        #             "symbol": "BTC_BRL",
        #             "type": "MARKET",
        #             "side": "SELL",
        #             "price": null,
        #             "averagePrice": "0",
        #             "amount": "0.123",
        #             "filledAmount": "0",
        #             "value": null,
        #             "filledValue": "0",
        #             "filledFee": "0",
        #             "status": "REJECTED",
        #             "timestamp": 1565165945588
        #         },
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data', {})
        return self.parse_order(data)

    def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {
            # 'symbol': market['id'],
            # 'status': 'SUBMITTED,PROCESSING',  # SUBMITTED, PROCESSING, PARTIAL_FILLED, CANCELING, FILLED, CANCELED, REJECTED
            # 'fromId': '...',  # order id to begin with
            # 'toId': '...',  # order id to end up with
            # 'fromTimestamp': since,
            # 'toTimestamp': self.milliseconds(),
            # 'limit': limit,  # default 100, max 100
        }
        market = None
        if symbol is not None:
            market = self.market(symbol)
            request['symbol'] = market['id']
        if limit is not None:
            request['limit'] = limit  # default 100, max 100
        if since is not None:
            request['fromTimestamp'] = since
        response = self.privateGetOrdersList(self.extend(request, params))
        #
        #     {
        #         "code": "A10000",
        #         "data": [
        #             {
        #                 "id": "608695678650028032",
        #                 "symbol": "BTC_BRL",
        #                 "type": "MARKET",
        #                 "side": "SELL",
        #                 "price": null,
        #                 "averagePrice": "0",
        #                 "amount": "0.123",
        #                 "filledAmount": "0",
        #                 "value": null,
        #                 "filledValue": "0",
        #                 "filledFee": "0",
        #                 "status": "REJECTED",
        #                 "timestamp": 1565165958796
        #             },
        #         ],
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data', [])
        return self.parse_orders(data, market, since, limit)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        request = {
            'status': 'SUBMITTED,PROCESSING,PARTIAL_FILLED,CANCELING',
        }
        return self.fetch_orders(symbol, since, limit, self.extend(request, params))

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        request = {
            'status': 'FILLED,CANCELED,REJECTED',
        }
        return self.fetch_orders(symbol, since, limit, self.extend(request, params))

    def fetch_order_trades(self, id, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        request = {
            'id': id,
        }
        response = self.privateGetOrdersFill(self.extend(request, params))
        market = None
        if symbol is not None:
            market = self.market(symbol)
        data = self.safe_value(response, 'data', [])
        #
        #     {
        #         "code": "A10000",
        #         "data": [
        #             {
        #                 "id": "608717046691139584",
        #                 "orderId": "608716957545402368",
        #                 "symbol": "BTC_BRL",
        #                 "side": "BUY",
        #                 "amount": "0.0988",
        #                 "price": "45514.76",
        #                 "fee": "0.0000988 BTC",
        #                 "role": "MAKER",
        #                 "timestamp": 1565171053345
        #             },
        #         ],
        #         "message": "Success"
        #     }
        #
        return self.parse_trades(data, market, since, limit)

    def parse_order_status(self, status):
        statuses = {
            'SUBMITTED': 'open',
            'PROCESSING': 'open',
            'PARTIAL_FILLED': 'open',
            'CANCELING': 'open',
            'FILLED': 'closed',
            'CANCELED': 'canceled',
            'REJECTED': 'rejected',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        #
        # createOrder, fetchOrders, fetchOrder
        #
        #     {
        #         "amount": "0.001",
        #         "averagePrice": null,
        #         "filledAmount": "0",
        #         "filledFee": "0",
        #         "filledValue": "0",
        #         "id": "633679992971251712",
        #         "price": "35000",
        #         "side": "BUY",
        #         "status": "PROCESSING",
        #         "symbol": "BTC_BRL",
        #         "timestamp": 1571122683535,
        #         "type": "LIMIT",
        #         "value": "35"
        #     }
        #
        # cancelOrder
        #
        #     {
        #         "result": True
        #     }
        #
        id = self.safe_string(order, 'id')
        amount = self.safe_float(order, 'amount')
        price = self.safe_float(order, 'price')
        cost = self.safe_float(order, 'filledValue')
        type = self.safe_string_lower(order, 'type')
        side = self.safe_string_lower(order, 'side')
        status = self.parse_order_status(self.safe_string(order, 'status'))
        timestamp = self.safe_integer(order, 'timestamp')
        average = self.safe_float(order, 'averagePrice')
        filled = self.safe_float(order, 'filledAmount')
        remaining = None
        if (amount is not None) and (filled is not None):
            remaining = max(0, amount - filled)
        fee = None
        feeCost = self.safe_float(order, 'filledFee')
        if feeCost is not None:
            fee = {
                'cost': feeCost,
                'currency': None,
            }
        symbol = None
        marketId = self.safe_string(order, 'marketId')
        if marketId is not None:
            if marketId in self.markets_by_id:
                market = self.markets_by_id[marketId]
            else:
                baseId, quoteId = marketId.split('_')
                base = self.safe_currency_code(baseId)
                quote = self.safe_currency_code(quoteId)
                symbol = base + '/' + quote
        if (symbol is None) and (market is not None):
            symbol = market['symbol']
        return {
            'id': id,
            'clientOrderId': None,
            'info': order,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'lastTradeTimestamp': None,
            'symbol': symbol,
            'type': type,
            'side': side,
            'price': price,
            'amount': amount,
            'cost': cost,
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': status,
            'fee': fee,
            'trades': None,
        }

    def withdraw(self, code, amount, address, tag=None, params={}):
        self.load_markets()
        currency = self.currency(code)
        request = {
            'code': currency['id'],
            'amount': self.currency_to_precision(code, amount),
            'wallet': address,
        }
        if tag is not None:
            request['tag'] = tag
        response = self.privatePostAccountWithdrawCoin(self.extend(request, params))
        #
        #     {
        #         "code":"A10000",
        #         "data": "DR123",
        #         "message":"Success"
        #     }
        #
        return self.parse_transaction(response, currency)

    def parse_transaction(self, transaction, currency=None):
        #
        # withdraw
        #
        #     {
        #         "code":"A10000",
        #         "data": "DR123",
        #         "message":"Success"
        #     }
        #
        id = self.safe_string(transaction, 'data')
        code = None
        if currency is not None:
            code = currency['code']
        return {
            'info': transaction,
            'id': id,
            'currency': code,
            'amount': None,
            'address': None,
            'addressFrom': None,
            'addressTo': None,
            'tag': None,
            'tagFrom': None,
            'tagTo': None,
            'status': None,
            'type': None,
            'updated': None,
            'txid': None,
            'timestamp': None,
            'datetime': None,
            'fee': None,
        }

    def fetch_accounts(self, params={}):
        response = self.privateGetAccountSubs(params)
        #
        #     {
        #         "code": "A10000",
        #         "data": [
        #             {
        #                 "subId": "CA648856083527372800",
        #                 "state": "Normal",
        #                 "subAccount": "003",
        #                 "subIdentify": "003"
        #             }
        #         ],
        #         "message": "Success"
        #     }
        #
        data = self.safe_value(response, 'data', [])
        result = []
        for i in range(0, len(data)):
            account = data[i]
            accountId = self.safe_string(account, 'subId')
            type = self.safe_string(account, 'subAccount')
            result.append({
                'id': accountId,
                'type': type,
                'currency': None,
                'info': account,
            })
        return result

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        request = '/' + self.version + '/' + self.implode_params(path, params)
        url = self.urls['api'][api] + request
        query = self.omit(params, self.extract_params(path))
        if api == 'public':
            if query:
                url += '?' + self.urlencode(query)
        elif api == 'private':
            self.check_required_credentials()
            timestamp = str(self.milliseconds())
            headers = {
                'X-Nova-Access-Key': self.apiKey,
                'X-Nova-Timestamp': timestamp,
            }
            queryString = None
            if method == 'POST':
                body = self.json(query)
                queryString = self.hash(body, 'md5')
                headers['Content-Type'] = 'application/json'
            else:
                if query:
                    url += '?' + self.urlencode(query)
                queryString = self.urlencode(self.keysort(query))
            auth = method + "\n" + request + "\n" + queryString + "\n" + timestamp  # eslint-disable-line quotes
            headers['X-Nova-Signature'] = self.hmac(self.encode(auth), self.encode(self.secret))
        return {'url': url, 'method': method, 'body': body, 'headers': headers}

    def handle_errors(self, code, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if response is None:
            return
        #
        #     {"code":"A10003","data":[],"message":"Authentication failed, Invalid accessKey."}
        #
        errorCode = self.safe_string(response, 'code')
        if errorCode != 'A10000':
            message = self.safe_string(response, 'message')
            feedback = self.id + ' ' + body
            self.throw_exactly_matched_exception(self.exceptions['exact'], errorCode, feedback)
            self.throw_broadly_matched_exception(self.exceptions['broad'], message, feedback)
            raise ExchangeError(feedback)  # unknown message
