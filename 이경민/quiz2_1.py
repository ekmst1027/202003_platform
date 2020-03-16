'''
1.
문자열의 역순이 문자열과 동일하면 팰린드롬이라고 한다.
예를 들어, "토마토"는 팰린드롬이지만, "radio"는 팰린드롬이 아니다.
문자열이 주어지면 python 함수를 작성하여 팰린드롬인지 여부를 확인하시오.

테스트코드
<입력>
print(is_palindrome("radio"))
print(is_palindrome("토마토"))

<출력>
False
True
'''

# 풀이의도
# 문자열 배열과 역순의 배열이 일치하면 팰린드롬으로 간주하여 함수를 만들었음.


def is_palindrome(word):
    if word[::] == word[-1::-1]:
        return True
    else:
        return False


print(is_palindrome("radio"))
print(is_palindrome("토마토"))
