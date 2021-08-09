a = input('Enter first number: ')
b = input('Enter second number: ')
c = input('Enter + or -: ')
#a => число; => x; x = a (но уже число)
a = int(a)
b = int(b)

if c == "+": #если
	print(a+b)
if c == "-": #если
	print(a-b)
else: #но если не одно из условий више не выполнилось
        print('Uncorrect!')

input()
