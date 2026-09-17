def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Обчислює кінцеву ціну товару з урахуванням знижки.
    :param price: Початкова ціна
    :param discount_percent: Відсоток знижки
    :return: Ціна зі знижкою
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Ціна та знижка не можуть бути від'ємними")
    return price * (1 - discount_percent / 100)