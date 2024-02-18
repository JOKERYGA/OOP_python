import datetime


class Record:
    def __init__(self, amount, comment, date=None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = datetime.datetime.now().date()
        else:
            self.date = datetime.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit: int) -> None:
        self.limit = limit # дневной лимит трат/калорий
        self.records = []

    def add_record(self, record):
        """Сохраняет новую запись о расходах"""
        self.records.append(record)

    def get_today_stats(self):
        """Считает, сколько денег потрачено сегодня"""
        today = datetime.datetime.now().date()
        return sum(record.amount for record in self.records
                   if record.date == today)

    def get_week_stats(self):
        """Считает, сколько денег потрачено за последние 7 дней"""
        today = datetime.datetime.now().date()
        week_ago = today - datetime.datetime(days=7)
        return sum(record.amount for record in self.records
                   if week_ago <= record.date <= today)


class CashCalculator(Calculator):
    USD_RATE = 92.55
    EURO_RATE = 99.35

    def get_today_cash_remained(self, currency):
        """Должен определять, сколько ещё денег можно потратить сегодня
        в рублях,долларах или евро"""
        today_stats = self.get_today_stats()

        currencies_dict = {
            'rub': (1, 'руб'),
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EURO_RATE, 'Euro')
        }
        rate, currency_name = currencies_dict[currency]
        cash_remained = round((self.limit - today_stats) / rate, 2)

        if cash_remained > 0:
            return f"На сегодня осталось  {cash_remained} {currency_name}"
        elif cash_remained == 0:
            return 'Денег нет, держись'
        else:
            return f"Денег нет, держись: твой долг - {abs(cash_remained)}"\
                    f"{currency_name}"


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        """Определяет, сколько ещё калорий можно/нужно получить сегодня"""
        today_stats = self.get_today_stats()
        if today_stats < self.limit:
            return "Сегодня можно съесть что-нибудь ещё, но с общей "\
                   f"калорийностью не более {self.limit - today_stats} кКал"
        else:
            return "Хватит есть!"

# TESTS
# создадим калькулятор денег с дневным лимитом 1000
cash_calculator = CashCalculator(1000)

# дата в параметрах не указана,
# так что по умолчанию к записи
# должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment='кофе'))
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000,
                                  comment='бар в Танин др',
                                  date='08.11.2019'))

print(cash_calculator.get_today_cash_remained('rub'))
# должно напечататься
# На сегодня осталось 555 руб