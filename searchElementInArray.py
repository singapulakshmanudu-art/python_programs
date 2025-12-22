arr = [10, 20, 30, 40, 50]
key = int(input("Enter element in array: "))
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print("Element found in array")
        found = True
        break
if not found:
    print("Element not found in array")
