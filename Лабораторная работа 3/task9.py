salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев
need_money -= salary - spend  # количество денег, чтобы прожить 1 месяц
months_ = 1
# TODO Оформить решение
while months_ != 10:
    spend *= 1.03
    need_money -= salary - spend
    months_ += 1
print(round(need_money))
