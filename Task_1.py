import re


def email_parse(email_address):
    valid_address = r'[A-Za-z0-9_-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}'
    if re.findall(valid_address, email_address):
        result = re.search(r'(?P<username>[A-Za-z0-9_-]+)@'
                           r'(?P<domain>[A-Za-z0-9-]+\.[A-Za-z]{2,})', email_address)
        return result.groupdict()
    raise ValueError(f'wrong email: {email_address}')


if __name__ == '__main__':
    print(email_parse('someone@geekbrains.ru'))
