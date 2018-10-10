def gcd(a,b):
	print(str(a)+" : "+ str(b))
	if(b==0):
		return a
	else:
		gcd(b,(a%b))

gcd(14,21)