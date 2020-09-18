def solution(x):
    import string


    y =""
    alphabet = "abcdefghijklmnopqrstuvwxyz"


    for letter in x:
        if letter.islower():
            y += alphabet[len(alphabet)-1-alphabet.index(letter)]
        else:
            y += letter

    return y


print(solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?"))