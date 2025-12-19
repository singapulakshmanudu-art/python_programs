text=input("enter  a string:")
result=" "
for ch in text:
duplicate=false
for r in result:
if ch==r:
duplicate=true
break
if not duplicate:
result=result+ch
print("string without duplicate:",result)
