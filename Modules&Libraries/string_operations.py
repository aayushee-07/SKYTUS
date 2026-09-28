def reverse_string(text):
    return text[::-1]


def count_vowels(text):
    count = 0

    for char in text:
        if char in "aeiou":
            count += 1

    return count