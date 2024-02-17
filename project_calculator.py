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
        self.limit = limit
        self.record = []
    
    def add_record(self):
        """Сохранять новую запись о расходах"""
        

    def get_today_stats():
        """Считать, сколько денег потрачено сегодня"""
        pass

    def get_week_stats(self):
        """Считать, сколько денег потрачено за последние 7 дней"""
        pass


class CashCalculator(Calculator):
    def add_record():
        """Сохранять новую запись о расходах"""
        pass

    def get_today_stats():
        """Считать, сколько денег потрачено сегодня"""
        pass

    def get_today_cash_remained(self, currency):
        """Определять, сколько ещё денег можно потратить сегодня в рублях,
        долларах или евро"""
        pass

    def get_week_stats(self):
        """Считать, сколько денег потрачено за последние 7 дней"""
        pass


class CaloriesCalculator(Calculator):
    def get_today_stats():
        """Считать, сколько денег потрачено сегодня"""
        pass

    def get_calories_remained(self):
        """Определять, сколько ещё денег можно потратить сегодня в рублях,
        долларах или евро"""
        pass

    def get_week_stats(self):
        """Считать, сколько денег потрачено за последние 7 дней"""
        pass