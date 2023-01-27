per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

total_cents = list(per_cent.values())

money = int(input("Введите сумму вклада:"))

deposit_1 = int(money//100*total_cents[0])
res_1 = int((money//100*total_cents[0])+money)

deposit_2 = int(money//100*total_cents[1])
res_2 = int((money//100*total_cents[1])+money)

deposit_3 = int(money//100*total_cents[2])
res_3 = int((money//100*total_cents[2])+money)

deposit_4 = int(money//100*total_cents[3])
res_4 = int((money//100*total_cents[3])+money)

print("Ваш чистый доход при вкладке в ТКБ: ", deposit_1, "|",
      "Итоговая сумма: ", res_1)
print("Ваш чистый доход при вкладке в СКБ: ", deposit_2, "|",
      "Итоговая сумма: ", res_2)
print("Ваш чистый доход при вкладке в ВТБ: ", deposit_3, "|",
      "Итоговая сумма: ", res_3)
print("Ваш чистый доход при вкладке в СБЕР: ", deposit_4, "|",
      "Итоговая сумма: ", res_4)

deposit = [deposit_1, deposit_2, deposit_3, deposit_4]
deposit = max(deposit)

print("Максимальная сумма, которую вы можете заработать -", deposit)