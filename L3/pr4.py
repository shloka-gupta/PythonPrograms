# for palindrome

s1= input("enter a string ")

s2=s1[::-1] #reverse karne keliye by slicing

if(s1==s2):
	print("palindrome")
else:
	print("not a palindrome")

