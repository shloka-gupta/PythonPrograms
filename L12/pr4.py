try:
	n1=int(input("enter no. "))
	n2=int(input("enter no. "))
	if n2==0:
		raise Exception("2nd number shud not be 0 ")
	ans=n1/n2
except Exception as e:
	print("issue ",e)
else:
	print(ans)