import random
naksh = ""
for i in range(int(raw_input("Enter Number"))):
	x=random.randint(1,100)
	if x%2==0:
		naksh+='['
	else:
		naksh+=']'

print naksh
stack=[]
for i in range(len(naksh)):
	if naksh[i]=='[':
		stack.append("1")
	else:
		if len(stack)==0:
			print "Unbalanced String"
			exit(0)
		else:
			stack.pop()
if len(stack)==0:
	print "balanced string"
else:
	print "unbalanced string"
