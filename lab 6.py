
def func1(n):
    sum = 0
    x = lambda n: (n - 3) / n ** 2
    for i in range(1, num + 1):
        sum += x(i)
        myList.append(x(i))
    return sum



var = 0
multip = 1 # values will be multiplied with this variable
myList2 =[] # to see what the values are at each step

def func2(n):
    global var
    global multip
    var = n
    var = (var / (var + 2)) - 10 # operating what defined function does
    multip = multip*var # multiplication of values
    myList2.append(multip)

    if  n==1:  # if the value n = 1 stop the recursion (base condition)
        print(multip)
    else:
        func2(n-1) # recursive part




myList = []
num = int(input("Please enter n value: "))

print(func1(num))
print(myList)
func2(num)
print(myList2)