def all_variants(text):
    length = 1
    while length != len(text)+1:
        for fn in range(len(text)):
            for ln in range(len(text)):
                if 0 < len(text[fn:ln+1]) == length:
                    yield text[fn:ln+1]
        else:
            length += 1

a = all_variants("apple")
print(a)
for i in a:
    print(i)