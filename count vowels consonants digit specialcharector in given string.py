def count_charectpors(string):
    vowel=consonant=specialchar=digit=0
    string=string.lower()    
    for char in string:
        if char in 'aeiou':
            vowel+=1
        elif char.isalpha():
            consonant+=consonant
        elif char.isdigit():
            digit+=1
        else:
            specialchar+=1
    return vowel, consonsnt, specialchar, digit
inputstring=input()
vowels, consonants, specialchars, digits=count_charectpors(inputstring) 
print("vowel", vowels)
print("consonant",consonants)
print("digit",digits)
print("special",specialchars)
