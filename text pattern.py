def locate(sub, main):
    size_main = len(main)
    size_sub = len(sub)
    print("search string:", sub)
    print("-----")
    found_any = False
    index = 0

    while index <= size_main - size_sub:
        k = 0
        while k < size_sub:
            if main[index + k] != sub[k]:
                break
            k += 1
        if k == size_sub:  # full match found
            print("substring exists at position", index)
            found_any = True
        index += 1

    if not found_any:
        print("substring not found in given string")


full_text = "AABAACAADAABAABA"
search_text = "AABA"
locate(search_text, full_text)