import requests
from core.models import ExchangeRates
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
           "Connection": "keep-alive",
           "Upgrade-Insecure-Requests": "1"}


def monobank_rate():
    UAH_CODE = 980
    EUR_CODE = 978

    request = requests.get("https://api.monobank.ua/bank/currency", headers=HEADERS)
    if request.status_code == 200:
        response = request.json()
    for currency in response:
        if currency['currencyCodeA'] == EUR_CODE and currency['currencyCodeB'] == UAH_CODE:
            bank = 'Monobank'
            rate_buy = currency['rateBuy']
            rate_sell = currency['rateSell']
            ExchangeRates.objects.update_or_create(
                bank=bank,
                defaults={'currency_name_1': 'EUR',
                          'currency_name_2': 'UAH',
                          'rate_buy': rate_buy,
                          'rate_sell': rate_sell,

                          })


def privatbank_rate():
    request = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11", headers=HEADERS)

    if request.status_code == 200:
        response = request.json()
    for currency in response:
        bank = 'Privatbank'
        currency_name = currency['ccy']
        rate_buy = currency['buy']
        rate_sell = currency['sale']
        ExchangeRates.objects.update_or_create(
            bank=bank,
            defaults={'currency_name_1': currency_name,
                      'currency_name_2': 'UAH',
                      'rate_buy': rate_buy,
                      'rate_sell': rate_sell,

                      })


# def vcurse_rate():
#     request = requests.get("hhttps://vkurse.dp.ua/course.json")
#     if request.status_code == 200:
#         response = request.json()['Pln']
#     for currency in response:
#         bank = 'Vcurse'
#         rate_buy = currency['buy']
#         rate_sell = currency['sale']
#         ExchangeRates.objects.update_or_create(
#             bank=bank,
#             defaults={'currency_name_1': 'PLN',
#                       'currency_name_2': 'UAH',
#                       'rate_buy': rate_buy,
#                       'rate_sell': rate_sell,
#                       })


def oshadbank_rate():
    request = requests.get('https://www.oschadbank.ua/currency-rate', headers=HEADERS)

    if request.status_code == 200:
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        rates = soup.select('tbody .heading-block-currency-rate__table-row')
        rate = rates[0].find_all('td')
        if rate[1].text == 'USD':
            bank = 'Oshadbank'
            rate_buy = rate[3].text.replace(',', '.')
            rate_sell = rate[4].text.replace(',', '.')
            ExchangeRates.objects.update_or_create(
                bank=bank,
                defaults={'currency_name_1': 'USD',
                          'currency_name_2': 'UAH',
                          'rate_buy': rate_buy,
                          'rate_sell': rate_sell
                          })


def eximbank_rate():
    request = requests.get(
        'https://www.eximb.com/ua/business/pryvatnym-klientam/pryvatnym-klientam-inshi-poslugy/obmin-valyut/kursy-valyut.html',
        headers=HEADERS)

    if request.status_code == 200:
        content = request.content
        soup = BeautifulSoup(content, 'html.parser')
        rates = soup.select('tbody')
        rate = rates[2].find_all('td')
        if rate[0].text == 'USD':
            bank = 'Pumb'
            rate_buy = rate[2].text.replace(',', '.')
            rate_sell = rate[5].text.replace(',', '.')
            ExchangeRates.objects.update_or_create(
                bank=bank,
                defaults={'currency_name_1': 'USD',
                          'currency_name_2': 'UAH',
                          'rate_buy': rate_buy,
                          'rate_sell': rate_sell
                          })


def add_rates():
    eximbank_rate()
    oshadbank_rate()
    privatbank_rate()
    monobank_rate()
