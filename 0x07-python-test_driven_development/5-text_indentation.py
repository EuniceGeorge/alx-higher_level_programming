#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = ""
    for words in text:
        result += words
        if words in (".", "?", ":"):
            result += "\n\n"
    print(result)

