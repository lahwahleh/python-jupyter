#one.py

def func():
	print("fun() in one.py")


print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
	print("ONE.py is being run directly")
else:
	print("ONE.PY HAS BEEN IMPORTED")