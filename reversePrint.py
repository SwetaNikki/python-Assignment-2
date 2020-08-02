
# Write a Python program to reverse a word after accepting the input from the user.
#Input word: ineuron
#Output: norueni

txt = input("Enter any string : ")
print("Input : {}".format(txt))

rev = ""
for i in txt:
    rev = i + rev
    
print("Output : {}".format(rev))
