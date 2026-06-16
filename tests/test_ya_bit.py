from pytest import mark  # Импортируем декоратор для маркировки тестов

from utils.btc_response import BTC_RESPONSE  # Импортируем фикстуру с данными по BTC
from utils.eth_response import ETH_RESPONSE  # Импортируем фикстуру с данными по ETH


@mark.btc  # Маркируем тест как относящийся к BTC
def test_yabit_btc_tokenId():
    # Извлекаем список предложений из ответа API
    items = BTC_RESPONSE['result']['items']
    
    # Проверяем КАЖДОЕ предложение в цикле
    for offer in items:
        # Проверка токена и валюты
        assert offer['tokenId'] == 'BTC', \
            f"Неверный токен: {offer['tokenId']}"


@mark.btc
def test_yabit_btc_currencyId():
    items = BTC_RESPONSE['result']['items']
    for offer in items:
        # Проверка валюты
        assert offer['currencyId'] == 'RUB', \
            f"Неверная валюта: {offer['currencyId']}"


@mark.btc
def test_yabit_btc_len_offers():
    items = BTC_RESPONSE['result']['items']
    assert len(items) == 10, f"Выводится {len(items)} предложений"


@mark.btc
def test_yabit_btc_optional_key():
    items = BTC_RESPONSE['result']['items']
    for offer in items:
        # Дополнительные проверки (опционально)
        assert float(offer['price']) > 0, "Цена должна быть положительной"
        assert float(offer['quantity']) > 0, "Количество BTC должно быть > 0"


@mark.eth
def test_yabit_eth_tokenId():
    items = ETH_RESPONSE['result']['items']
    for offer in items:
        # Проверка токена и валюты
        assert offer['tokenId'] == 'ETH', \
            f"Неверный токен: {offer['tokenId']}"


@mark.eth
def test_yabit_eth_currencyId():
    items = ETH_RESPONSE['result']['items']
    for offer in items:
        # Проверка валюты
        assert offer['currencyId'] == 'RUB', \
            f"Неверная валюта: {offer['currencyId']}"


@mark.eth
def test_yabit_eth_len_offers():
    items = ETH_RESPONSE['result']['items']
    assert len(items) == 10, f"Выводится {len(items)} предложений"


@mark.eth
def test_yabit_eth_optional_key():
    items = ETH_RESPONSE['result']['items']
    for offer in items:
        # Дополнительные проверки (опционально)
        assert float(offer['price']) > 0, "Цена должна быть положительной"
        assert float(offer['quantity']) > 0, "Количество ETH должно быть > 0"