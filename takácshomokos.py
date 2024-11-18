import unicodedata

# Példa szavak listája
words = ["állat", "alma", "érzés", "ér", "zöld", "csillag"]
sorted_words = sort_words(words)

print("ABC sorrendben, ékezetek nélkül:")
for word in sorted_words:
    print(word)
