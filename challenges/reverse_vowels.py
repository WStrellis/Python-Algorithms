# Write a function that takes a string as input and returns the string with only the vowels reversed.
# Note: The letters "a", "e", "i", "o", and "u" are vowels. The letter "y" is not a vowel.
'''
For s = "hello, world", the output should be
reverseVowelsOfString(s) = "hollo, werld";
For s = "codesignal", the output should be
reverseVowelsOfString(s) = "cadisegnol";
For s = "eIaOyU", the output should be
reverseVowelsOfString(s) = "UOaIye".
'''


def reverse_vowels_of_string(s):
    # get indexes of vowels
    vowel_indexes = [i for i in range(len(s)) if s[i].lower() in [
        'a', 'e', 'i', 'o', 'u']]
    # create stack
    stack = [*vowel_indexes]
    # create a new string and swap vowels
    new_s = ''
    for i in range(len(s)):
        if i in vowel_indexes:
            new_s = new_s + s[stack.pop()]
        else:
            new_s = new_s + s[i]

    return new_s
