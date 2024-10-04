from abc import ABC, abstractmethod


class CurrencyConversionStrategy(ABC):
    @abstractmethod
    def convert(self, amount, rate):
        pass


class FixedRateConversion(CurrencyConversionStrategy):
    def convert(self, amount, rate):
        return amount * rate


class MarketRateConversion(CurrencyConversionStrategy):
    def convert(self, amount, rate):
        return amount * (rate * 0.95)


class CentralBankRateConversion(CurrencyConversionStrategy):
    def convert(self, amount, rate):
        return amount * (rate + 0.01)


class CurrencyConverterContext:
    def __init__(self, strategy: CurrencyConversionStrategy):
        self.strategy = strategy

    def convert_currency(self, amount, rate):
        return self.strategy.convert(amount, rate)


def main():
    print("Выберите стратегию конвертации:")
    print("1. Фиксированный курс")
    print("2. Курс биржи")
    print("3. Курс центрального банка")

    choice = int(input("Введите номер стратегии (1/2/3): "))
    amount = float(input("Введите сумму для конвертации: "))
    rate = float(input("Введите обменный курс: "))

    if choice == 1:
        strategy = FixedRateConversion()
    elif choice == 2:
        strategy = MarketRateConversion()
    elif choice == 3:
        strategy = CentralBankRateConversion()
    else:
        print("Некорректный выбор.")
        return

    context = CurrencyConverterContext(strategy)
    result = context.convert_currency(amount, rate)
    print(f"Результат конвертации: {result:.2f}")
