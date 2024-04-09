while(1):
	s=str(input("Enter a string:"))
	if(s==None or s==""):
		print("Invalid output")
		continue
	n=len(s)
	Palindrome=True
	for i in range(n):
		if(s[i]!=s[n-1-i]):
			Palindrome=False
			break
	print(Palindrome)
	break
