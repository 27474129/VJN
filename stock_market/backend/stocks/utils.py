import logging
from typing import Dict

import finnhub

from stock_market.backend.config import FINNHUB_API_TOKEN


logger = logging.getLogger(__name__)


def get_stock(symbol: str) -> Dict[str, float]:
    """Функция получения текущей информации об акциях определенной компании.

    :param symbol - название акций компании.
    """
    finnhub_client = finnhub.Client(api_key=FINNHUB_API_TOKEN)
    current_info = finnhub_client.quote(symbol)
    logger.info(f'Получена акция компании: {symbol}')
    # Парсим ответ от финхаба, чтобы убрать лишние поля и добавить более
    # понятную аннотацию
    parsed_current_info: Dict = {}
    parsed_current_info['current_price'] = current_info['c']
    parsed_current_info['delta'] = current_info['d']
    parsed_current_info['percent_delta'] = current_info['dp']
    parsed_current_info['high_daily_price'] = current_info['h']
    parsed_current_info['low_daily_price'] = current_info['l']
    return parsed_current_info
