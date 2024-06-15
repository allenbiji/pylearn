def master_yoda(text):
   new=text.split()
   return " ".join(new[::-1])





# Check
print(master_yoda('I am home'))
# Check
master_yoda('We are ready')