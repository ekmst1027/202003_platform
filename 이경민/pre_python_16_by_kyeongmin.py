"""16. 1부터 50 까지의 숫자 중에서 3의 배수를 공백으로 구분하여 출력하시오."""

# 풀이 의도
# 1부터 50까지의 수를 출력하며 3으로 나누었을때 나머지가 0이 되는 경우 공백으로 출력

for i in range(1, 51):
    if(i % 3 == 0):
        print()
    else:
        print(i)
