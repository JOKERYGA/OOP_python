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
        """Сохранять новую запись о расходах"""
        self.records.append(record)

    def get_today_stats(self):
        """Считать, сколько денег потрачено сегодня"""
        today = datetime.datetime.now().date()
        return sum(record.amount for record in self.records if record.date == today)

    def get_week_stats(self):
        """Считать, сколько денег потрачено за последние 7 дней"""
        today = datetime.datetime.now().date()
        week_ago = today - datetime.datetime(days=7)
        return sum(record.amount for record in self.records
                   if week_ago <= record.date <= today)


class CashCalculator(Calculator):
    USD_RATE = 92.55
    EURO_RATE = 99.35


    def get_today_cash_remained(self, currency):
        """Должен определять, сколько ещё денег можно потратить сегодня в рублях,
        долларах или евро"""
        pass


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        """Определять, сколько ещё калорий можно/нужно получить сегодня"""
        today_stats = self.get_today_stats()
        if today_stats < self.limit:
            return "Сегодня можно съесть что-нибудь ещё, но с общей "\
                   f"калорийностью не более {self.limit - today_stats} кКал"
        else:
            return "Хватит есть!"
            




# TESTS
r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
r2 = Record(amount=1568,
            comment='Наполнение потребительской корзины',
            date='09.03.2019')
r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

# для CaloriesCalculator
r4 = Record(amount=1186,
            comment='Кусок тортика. И ещё один.',
            date='24.02.2019')
r5 = Record(amount=84, comment='Йогурт.', date='23.02.2019')
r6 = Record(amount=1140, comment='Баночка чипсов.', date='24.02.2019') 
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