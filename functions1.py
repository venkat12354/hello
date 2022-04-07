##
##def max_of_three( x, y, z ):
##    return max_of_two( x, max_of_two( y, z ) )
##print(max_of_three(3, 6, -5))
##
##o/p: 6
##
###s=[8,2,3,0,7]
##def fun1(*param):
##    sum=0
##    for item in param:
##        sum += item
##    return sum
##print(fun1(8,2,3,0,7))
##
##o/p: 20

#s=(5,54,56,6)


##
##def str_rev(str1):
##    str1= ''
##    index = len(str1)
##    while index > 0:
##        str1 += str1[ index - 1 ]
##        index -= 1
##    return str1
##print(str_rev('1234abcd'))


##def factorial(n):
##    if n == 0:
##        return 1
##    else:
##        return n * factorial(n-1)
##n=int(input("factorial of a number is : "))
##print(factorial(n))

##def test_range(n):
##    if n in range(3,9):
##        print( " %s is in the range"%str(n))
##    else :
##        print("The number is outside the given range.")
##test_range(5)



##def string_test(param):
##    upper_case=0
##    lower_case=0
##    for item in param:
##        if item.isupper():
##           upper_case +=1
##        elif item.islower():
##           lower_case +=1
##        else:
##           pass
##    print ("Original String : ", param)
##    print ("No. of Upper case characters : ", upper_case)
##    print ("No. of Lower case Characters : ", lower_case)
##
##string_test('HESfdshdudUYTUUKGFhjhgfhydf')


##
##def unique_list(l):
##  x = []
##  for a in l:
##    if a not in x:
##      x.append(a)
##  return x
##
##print(unique_list([1,2,3,3,3,3,4,5])) 
##


##def test_prime(n):
##    if (n==1):
##        return False
##    elif (n==2):
##        return True;
##    else:
##        for x in range(2,n):
##            if(n % x==0):
##                return False
##        return True             
##print(test_prime(9))

##
##def fun1(n):
##    b=[]
##    for a in range(1,n):
##        if a%2==0:
##            b.append(a)
##    return b
##print(fun1(20))
##


def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('hello')) 


















4
