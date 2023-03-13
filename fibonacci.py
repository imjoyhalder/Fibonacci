def fibo(n):
	a = 0
	b = 1
	if n == 0:
		print(n)
	else:
		for i in range(2,n+1):
			c = a+b
			a = b
			b = c
		print(c)
fibo(int(input()))