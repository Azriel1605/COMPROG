import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)

print(uppercase)
print(lowercase)

# uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encode_str(strng, shift):
#     cut = list(strng.split())
#     portion = [0]*5
#     for i in range(len(cut)):
#         i = i%5
#         portion[i] += 1
#     print(portion)
#     pointer = 0
#     for i in range(5):
#         temp = portion[i]
#         portion[i] = ' '.join(cut[pointer:pointer + portion[i]])
#         pointer += temp
#     print(cut)
#     print(portion)
#     # your code
#     encoding = []
#     for word in pointer:
#         encoding.append()
#         for char in word

# def decode(arr):
#     #your code
#     return None

# print(encode_str('I should have known that you would have a perfect answer for me!!!', 1))