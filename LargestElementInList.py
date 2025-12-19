arr = list(map(int, input("Enter List:").split()))
max_val = arr[0]
for i in arr:
if i > max_val:
max_val = i
print("Maximum Value is:",max_val)
