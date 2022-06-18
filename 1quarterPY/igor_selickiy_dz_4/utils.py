from requests import get, utils
from decimal import Decimal
from datetime import datetime

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
content = response.content.decode(encoding=utils.get_encoding_from_headers(response.headers))


def currency_rates(code, cool_vision=False, site=content):
    date_site_2 = site[site.find('Date="') + len('Date="'):site.find('" name="Foreign')]
    date_site = datetime.strptime(date_site_2, '%d.%m.%Y').date()
    for s in site.split('<CharCode>'):
        if code.upper() == s[0:3]:
            nominal = s[s.rfind('<Nominal>') + len('<Nominal>'):s.find('</Nominal>')]
            name = s[s.rfind('<Name>') + len('<Name>'):s.find('</Name>')]
            value = Decimal(s[s.rfind('<Value>') + len('<Value>'):s.find('</Value>')].replace(',', '.')).quantize(Decimal('1.00'))
            if cool_vision is False:
                return f'{value} {date_site}'
            else:
                return f'Получите {nominal} {name} за {value} руб на {date_site}'