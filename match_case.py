def checkVowel(n):
    match n:
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            return "Vowel alphabet"
        case _:
            return "Simple alphabet"

print(checkVowel('a'))
print(checkVowel('m'))
print(checkVowel('o')

