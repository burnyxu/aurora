	
import sys
	
def Fuc(para):
	str = 'hello2 ' + para
	#print("hello", para, str)
	return  str
     
if __name__ == "__main__":
	result = Fuc(sys.argv[1])
	print(result)