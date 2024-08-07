# count number of vowels

a = input('Enter a string\n')
a = a.lower()
counter = 0
for i in range(len(a)):
    if(a[i] == 'a' or a[i] == 'e' or a[i] == 'i' or a[i] == 'o' or a[i] == 'u'):
        counter += 1

print('Number of vowels in', a,'are :',counter)
