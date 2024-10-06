def all_variants(text):
    for i in range(len(text)):
        for j in range(len(text) - i):
            yield text[j:j + i + 1]


a = all_variants("abc")
for a in a:
    print(a)
