# Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문를 반환하시오. 만약 그런 문자가 없다면 _를 반환하시오.
# ("abadabac" !반복되지 않는 문자는 d,c가 있지만, "첫번째" 문자니까 d를 반환해주면 됩니다.)

input = "abadabac"

def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26
    
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
        print(alphabet_occurrence_array[arr_index])
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alpabet_occurance = alphabet_occurrence_array[index]
        if alpabet_occurance == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
    
    for char in string:
        if char in not_repeating_character_array:
            return char
    return "-"

result = find_not_repeating_character(input)
print(result)