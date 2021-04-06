class Date:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f'{self.data}'

    @classmethod
    def extract_numbers(cls, data):
        day, month, year = [int(number) for number in data.split('-')]
        data = [day, month, year]
        return cls(data)

    @staticmethod
    def validator_date(data):
        day, month, year = [int(number) for number in data.split('-')]
        if not 1 <= day <= 31:
            raise ValueError(f'Day invalid')
        if not 1 <= month <= 12:
            raise ValueError(f'Month invalid')
        if not 0 <= year <= 9999:
            raise ValueError('Year invalid')
        return [day, month, year]


if __name__ == '__main__':
    print(Date.extract_numbers('01-01-2021'))
    print(Date.validator_date('01-01-2021'))
