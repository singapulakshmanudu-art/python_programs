text=input("enter string:")
count=0
in_word=false
for char in text:
if char!=" " and not in_word:
count=count+1
in_word=true
elif char==" ":
in_word=false
printf("Number of words:",count)
