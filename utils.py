from requests import get
from decimal import Decimal


def currency_rates(code):
    code = str.upper(code)
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)
    date = ''
    for el in content.split(' Date="')[1:]:
        date = el.split('" name="')[0]
        date = date[6:] + '-' + date[3:5] + '-' + date[0:2]
    currency_code = []
    for el in content.split('<CharCode>')[1:]:
        currency_code.append(el.split('</CharCode>')[0])
    currency_value = []
    for el in content.split('<Value>')[1:]:
        currency_value.append(Decimal(float(el.split('</Value>')[0].replace(',', '.'))).quantize(Decimal('1.00')))
    code_value = dict(zip(currency_code, currency_value))
    if code_value.get(code):
        code_value_date = str(code_value.get(code)) + ', ' + date
        return code_value_date
    return code_value.get(code)
