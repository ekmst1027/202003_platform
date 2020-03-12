"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오"""

sum = 0
flag = 0
for i in range(101):
    sum += i
    if(sum > 1000):
        flag += 1
        if(flag == 1):
            over_thousand = i

print("최초로 1000을 넘게하는 수 :", over_thousand)
print("1부터100까지의 합 :", sum)
