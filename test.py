password=input("Enter your Password: ")

def length(password):
	if len(password) < 8:
  		 print("The password must be 8 Characters long")

def uppercase(password):
	for char in password:
		if char.isupper():
			return True
	return False
length(password)
#hello//
