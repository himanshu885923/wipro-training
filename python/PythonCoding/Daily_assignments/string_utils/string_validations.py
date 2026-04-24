def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

def is_alpha(text):
    return text.isalpha()