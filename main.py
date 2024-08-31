import night_crow_parser
import json
from tabulate import tabulate
class Token:
    #vDIA fee to create token
    _token_fee = {}
    
    #amount of resources to create 1 token
    __token_resource_amount = {
        'CROW': 0,
        'MORION': 10,
        'GEAR': 1,
        'PROMOTE': 1,
        'TEAR': 1,
        'FEATHER': 1,
        'PAPYRUS': 10
    }
    #avg price in dimond per 1 resource
    _resources_avg_price = {}

    night_crow_parser = night_crow_parser.NightCrowToken()

    def __init__(self) -> None:
        self.night_crow_tokens = self.night_crow_parser.parse_token_info()

        with open('token_fee.json') as file:
            self._token_fee = json.load(file)
        with open('item_avg_price.json') as file:
            self._resources_avg_price = json.load(file)



    def calculate_token_price(self):
        result = []
        usd_token_price = self.night_crow_tokens['CROW']['close']


        for token in self.night_crow_tokens:
            token_data = self.night_crow_tokens[token]\
            
            token_name = token_data['symbol']
            last_crow_price = 1
            
            if token_name != 'CROW':
                last_crow_price = token_data['close']

            result.append(
                {
                    'token_name': token_name,
                    'dimond_price_per_token': self.__token_resource_amount[token_name] * self._resources_avg_price[token_name] + self._token_fee[token_name],
                    'crow_price_per_token': 0 if token_name == 'CROW' else last_crow_price,
                    'usd_token_price': usd_token_price * last_crow_price
                }
            )

        print(tabulate(result, headers='keys', tablefmt='psql'))
token = Token()
token.calculate_token_price()


