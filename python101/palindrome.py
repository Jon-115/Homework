word = input("Enter a word. ")
half = len(word)/2
half = int(half)
# print(word[0:half+1])
# print(word[len(word):half-1:-1])

if word[0:half+1] == word[len(word):half-1:-1]:
    print("It is a palindrome. ")
else:
    print("Not a palindrome. ")