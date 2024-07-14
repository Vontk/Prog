def slice_simple():
    text = "Awesome"
    first_three = text[:3].lower()
    print(first_three)
    middle_char = len(text) // 2
    middle_txt = text[middle_char-1:middle_char+2]
    print(middle_txt)
    length=len(text)
    print(text[:4].lower() +text[length-3:].lower())


slice_simple()