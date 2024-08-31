import requests

class NightCrowToken:
    def __init__(self) -> None:
        pass
    
    def get_tokens_info(self):
        url = 'https://www.nightcrows.com/nftapi/v1/main/token/ncgl'
        return requests.get(url).json()
    
    def parse_token_info(self) -> list:
        tokens_data_result = {}
        tokens_data = self.get_tokens_info().get('data', {})

        tokens_data_result['CROW'] = tokens_data['CROW']

        for token in tokens_data['list']:
            tokens_data_result[token] = tokens_data['list'][token]

        return tokens_data_result


