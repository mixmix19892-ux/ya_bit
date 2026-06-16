import pytest

@pytest.fixture(params=[
    ('BTC', 'BTC_RESPONSE'),  # Первый набор параметров
    ('ETH', 'ETH_RESPONSE')   # Второй набор параметров
], ids=['BTC', 'ETH'])        # Человекочитаемые имена
def crypto_data(request):
    """Фикстура возвращает данные для разных криптовалют"""
    token, response_name = request.param

    if response_name == 'BTC_RESPONSE':
        from utils.btc_response import BTC_RESPONSE
        response_data = BTC_RESPONSE
    else:
        from utils.eth_response import ETH_RESPONSE  
        response_data = ETH_RESPONSE

    return {
        'token': token,                      # 'BTC' или 'ETH'
        'response': response_data,           # Полный ответ API
        'items': response_data['result']['items']  # Список ордеров
    }