'''
Ассимптотика О(n * n * k)
Память О(n * k)
таблица с данными должна лежать в одной папке с программой
чтобы программа быстрее посчитала ответ можно ограничить размер массива price после считывания
'''

import csv

date = []
price = []


def date_from_str(s):
    return s[0:4] + '.' + s[4:6] + '.' + s[6:8]


with open('new.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    l = 0
    for row in csv_reader:
        if l == 0:
            l += 1
            continue
        date.append((row[1]))
        price.append(float(row[3]))



#price = price[0:1000]
k = 2
n = len(price)
money = 100000
dp = [[(-1, -1) for j in range(k + 1)] for i in range(n + 1)]
for i in range(k + 1):
    dp[0][i] = (money, -1)

for i in range(1, n + 1):
    for j in range(k + 1):
        dp[i][j] = dp[i - 1][j]
        dp[i][j] = (dp[i][j][0], -1)
        if j:
            dp[i][j] = max(dp[i][j], dp[i][j - 1])
            for fr in range(1, i):
                prvmoney = dp[fr][j - 1][0]
                dp[i][j] = max(dp[i][j], (prvmoney % price[fr - 1] + price[i - 1] * (prvmoney // price[fr - 1]), fr))


def restore(i, j):
    if i == 0:
        return []
    if dp[i][j][1] == -1:
        return restore(i - 1, j)
    return restore(dp[i][j][1] - 1, j - 1) + [(dp[i][j][1], i)]


otv = restore(n, k)
crmoney = money
ind = 0
print('текущий капитал: ' + str(crmoney))
for i in otv:
    ind += 1
    print()
    print('Транзакция #' + str(ind) + ':')
    print("дата / стоимость покупки: " + date_from_str(date[i[0] - 1]) + ' / ' + str(price[i[0] - 1]))
    print("дата / стоимость продажи: " + date_from_str(date[i[1] - 1]) + ' / ' + str(price[i[1] - 1]))
    purchased = crmoney // price[i[0] - 1]
    delta = price[i[1] - 1] - price[i[0] - 1]
    print('купленно ' + str(purchased) + ' акций на сумму ' + str(price[i[0] - 1] * purchased))
    print('акции подорожали на ' + str(delta))
    print('итоговая прибыль от транзакции ' + str(delta * purchased))
    crmoney += delta * purchased
    print('текущий капитал ' +  str(crmoney))
