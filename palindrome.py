word = input("enter the word to check if it is palindrome ")


if word == word[::-1]:
    print("it is a palindrome")
else:
    print("it is NOT a palindrome")
