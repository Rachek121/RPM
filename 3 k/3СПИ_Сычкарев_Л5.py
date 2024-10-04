class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Необходимо переопределить способ оплаты")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата с кредитной карты."


class EWalletPayment(PaymentMethod):
    def pay(self, amount):
        return f"Оплата через электронный кошелек."


class PaymentPlatform:
    def __init__(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def set_payment_method(self, payment_method: PaymentMethod):
        self._payment_method = payment_method

    def execute_payment(self, amount):
        return self._payment_method.pay(amount)


class MobileAppPlatform(PaymentPlatform):
    def execute_payment(self, amount):
        return f"Мобильное приложение: {super().execute_payment(amount)}"


class WebPlatform(PaymentPlatform):
    def execute_payment(self, amount):
        return f"Веб-сайт: {super().execute_payment(amount)}"


def main():
    amount = 100

    print("Выберите способ оплаты:")
    print("1. Кредитная карта")
    print("2. Электронный кошелек")
    payment_choice = input("Введите номер способа оплаты: ")

    if payment_choice == "1":
        payment_method = CreditCardPayment()
    elif payment_choice == "2":
        payment_method = EWalletPayment()
    else:
        print("Неверный выбор!")
        return

    print("Выберите платформу:")
    print("1. Мобильное приложение")
    print("2. Веб-сайт")
    platform_choice = input("Введите номер платформы: ")

    if platform_choice == "1":
        platform = MobileAppPlatform(payment_method)
    elif platform_choice == "2":
        platform = WebPlatform(payment_method)
    else:
        print("Неверный выбор!")
        return

    result = platform.execute_payment(amount)
    print(result)


if __name__ == "__main__":
    main()
