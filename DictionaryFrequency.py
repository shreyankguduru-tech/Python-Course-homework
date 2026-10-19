test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1}

print(test_dict)

word = input("Enter a wrod: ")

if word in test_dict:
    print("Frequency:", test_dict[word])
else:
    print("Word not fond")

