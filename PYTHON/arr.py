arr=[1,3,2,6,5,4]

arr.append(7)   # append operation

arr.sort()      # sort operation
print(arr)

arr.pop()
print(arr)
 
arr.reverse()
print(arr)

arr.insert(2,10)
print(arr)

### Getting a new array from the user 
num=[]
n=int(input("Enter the number of elements in the array: "))
for i in range(n):
    num.append(int(input(" ")))
print(num)


###finding the largest and smallest on the array
largest=max(num)
smallest=min(num)
print("Largest element:", largest)
print("Smallest element:", smallest)
###manual finding of largest
large=num[0]
small=num[0]
for i in range (len(num)):
    if num[i]<small:
        small=num[i]
    if num[i]>large:
        large=num[i]
print("Largest element (manual):", large)
print("Smallest element (manual):", small)


###finding the count of the nos in array
count=0
even_count=0    #finding the even count
odd_count=0 #finding the odd count
for i in range(len(num)):
    count+=1
    if num[i]%2==0:
        print (num[i],"is even")    # printing the even numbers 
        even_count+=1
    else:
        print(num[i],"is odd")  #printing the odd numbers
        odd_count+=1
print("Total elements:", count)
print("Even elements:", even_count)
print("Odd elements:", odd_count)


###sum of all elements in the array
sum=0
for i in range(len(num)):
    sum+=num[i]
print("Sum of all elements:", sum)
###finding average of the array elements
print("average: ",sum/len(num))

###copy an array to another array
new_arr=[]
for i in range(len(num)):
    new_arr.append(num[i])
print("Copied array:", new_arr)

###check if the array is sorted or not
for i in range(len(num)-1):
    if (num[i]<num[i+1]):
        print(" the above array is sorted")
        break
    else:
        print("the array is not sorted")

###check the array contains duplicate or not
dup_arr=[]
for i in range(len(num)):
    if num[i] not in dup_arr:
        dup_arr.append(num[i])
print("Array without duplicates:", dup_arr)

###move all the zero to the end of the array
result=[]
for i in range(len(num)):
    if num[i]!=0:
        result.append(num[i])
no_zeros=len(num)-len(result)
for i in range(len(num)):
    if num[i]==0:
        result.append(num[i])
print("Array with zeros at the end:", result)





























































































