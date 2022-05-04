prices = [7,1,5,3,6,4]

min_day = prices[0]
answer = 0
for i in range(1, len(prices)):
  if min_day > prices[i]:
    min_day = prices[i]
    continue

  answer = max(answer, prices[i] - min_day)

print(answer)