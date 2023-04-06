from typing import Dict

import finnhub

from stock_market.config import FINNHUB_API_TOKEN


def get_stock(symbol: str) -> Dict[str, float]:
    """Метод получения текущей информации об акциях определенной компании.

    symbol - название акций компании.
    """
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_TOKEN)
    current_info = finnhub_client.quote(symbol)
    # Парсим ответ от финхаба, чтобы убрать лишние поля и добавить более
    # понятную аннотацию
    parsed_current_info: Dict = {}
    parsed_current_info['current_price'] = current_info['c']
    parsed_current_info['delta'] = current_info['d']
    parsed_current_info['percent_delta'] = current_info['dp']
    parsed_current_info['high_daily_price'] = current_info['h']
    parsed_current_info['low_daily_price'] = current_info['l']
    return parsed_current_info
