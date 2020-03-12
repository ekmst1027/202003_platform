"""19. 다음 리스트에서 알파벳 개수가 7개인 단어를 출력하시오
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
 """

# 풀이 의도
# list comprehension을 사용하여 단어의 길이가 7인 단어만 출력

a = ['alpha', 'bravo', 'charlie', 'delta',
     'echo', 'foxtrot', 'golf', 'hotel', 'india']

new_a = [word for word in a if len(word) == 7]

print(new_a)
