arr = list(map(int, input().split()))
key = int(input())
for i in arr:
if i == key:
print("Found")
break
else:
print("Not Found")
