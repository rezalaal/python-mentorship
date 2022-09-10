# String as List

text = "Hello World"
print(text[0]) # H
print(text[6]) # W
print(text[5]) # space
# print(text[11]) # IndexError: string index out of range
print(text[-1]) # d
print(text[-7]) # space

print(text[0:5]) # Hello
print(text[6:11]) # World
print(text[3:]) # lo World
print(text[:5]) # Hello
print(text[:]) # Hello World
print(text[-5:]) # World
print(text[:-6]) # Hello
print(text[1:10:2]) # el ol
