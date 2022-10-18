money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
money_capital -= 6000  # подушка безопасности к первому месяцу
month = 0  # количество месяцев, которое можно прожить

while money_capital > 0:
    spend *= 1.05
    money_capital += salary - spend
    month += 1
print(month)
