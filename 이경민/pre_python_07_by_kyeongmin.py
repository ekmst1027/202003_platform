"""7. 1부터 100까지 수의 합을 계산하고 있다. 
이 때 합이 최초로 1000을 넘게 하는 수가 무엇인지 코드를 만들고 답을 구하시오"""

# version1

# 풀이 의도
# 1부터 100까지의 수의 합을 계산하는 sum과 sum이 최초로 1000을 넘었을 때를 구분하는 flag를 이용하여
# 1000이 넘었을 때부터 flag의 값을 증가시켜 1000을 최초로 넘었을 때의 값을 over_thousand로 할당함
# 그러나 뒷부분에 불필요하게 계속 flag의 값을 증가시키며 계산을 해야하는 불필요함이 있어서 version2로 리팩토링

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

# version2

# 풀이 의도
# flag의 의도에 맞게 boolean값으로 할당하여 불필요한 코드 제거

sum = 0
flag = False
for i in range(101):
    sum += i
    if sum > 1000 and flag == False:
        over_thousand = i
        flag = True

print("최초로 1000을 넘게하는 수 :", over_thousand)
print("1부터100까지의 합 :", sum)
