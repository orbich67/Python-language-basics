from requests import get
from decimal import Decimal


def currency_rates(code):
    code = str.upper(code)
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    currency_code = []
    for el in content.split('<CharCode>')[1:]:
        currency_code.append(el.split('</CharCode>')[0])
    currency_value = []
    for el in content.split('<Value>')[1:]:
        currency_value.append(Decimal(float(el.split('</Value>')[0].replace(',', '.'))).quantize(Decimal('1.00')))
    code_value = dict(zip(currency_code, currency_value))
    return code_value.get(code)


print(currency_rates("USD"))
print(currency_rates("EUR"))
print(currency_rates("XXX"))
