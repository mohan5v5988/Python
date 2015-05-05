import os

def fun(pa) :
	#print(pa)
	os.chdir(pa)
	allD = os.listdir(pa)
	print(allD)
	for f in allD :
		if os.path.isdir(f) :
			print(f)
			np = os.path.join(f)
			fun(np)
		else :
			#os.chdir("..")
			print("no")

path = input("path : ")
fun(path)








