# Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'X' 혹은 '+'연산자를 넣어 결과적으로 가장 큰 수를 구하는 프그램을 작성하시오.
# 단, '+'보다 'X'를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.

import numbers


input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    multiply_sum = 0
    for item in array:
        if item <= 1 or multiply_sum <= 1:
            multiply_sum += item
        else:
            multiply_sum *= item
    return multiply_sum

result = find_max_plus_or_multiply(input)
print(result)
