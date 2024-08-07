# check palindrome string 

x = input('Enter a string\n')
x = x.lower()
if(x==x[::-1]):
    print(x,' is a palindrome string')
else:
    print(x,' is not a palindrome string')
