#TODO:1. Write a recursive python function to print first N natural numbers.

def naturalNumbers(number):
  if number>0:
    naturalNumbers(number-1)
    print(number)
n = int(input('Enter the number:'))
naturalNumbers(n)

#TODO: 2. Write a recursive python function to print first N natural numbers in reverse order

def reversenaturalNaumber(number):
  if number>0:
    print(number)
    reversenaturalNaumber(number-1)
n = int(input('Enter the number:'))
reversenaturalNaumber(n)

#TODO: 3. Write a recursive python function to print first N odd natural numbers

def oddnumbers(n):
  if n>0:
    oddnumbers(n-1)
    if n% 2 !=0:
      print(n)
  
    
number = int(input('Enter the number:'))*2
oddnumbers(number)

#TODO: 4. Write a recursive python function to print first N odd natural numbers in reverse order

def reverseOdd(n):
  if n>0:
    if n % 2 !=0:
      print(n)
    reverseOdd(n-1)
number = int(input('Enter the number:'))*2
reverseOdd(number)

#TODO: 5 Write a recursive python function to print first N even natural numbers.

def evenNumbers(n):
  if n>0:
    evenNumbers(n-1)
    if n % 2 ==0:
      print(n)

number = int(input('Enter the number:'))*2
evenNumbers(number)

#TODO: 6 Write a recursive python function to print first N even natural numbers in reverse order.
def evenNumbers(n):
  if n>0:
    if n % 2 ==0:
      print(n)
    evenNumbers(n-1)

number = int(input('Enter the number:'))*2
evenNumbers(number)

#TODO: 7  Write a recursive python function to print squares of first N natural numbers

def squareNumbers(n):
  if n>0:
    squareNumbers(n-1)
    print(n*n)
number = int(input('Enter the number:'))
squareNumbers(number)

#TODO:8. Write a recursive python function to print cubes of first N natural numbers

def squareNumbers(n):
  if n>0:
    squareNumbers(n-1)
    print(n**3)
number = int(input('Enter the number:'))
squareNumbers(number)


#TODO: 9. Write a recursive python function to print first N multiples of a given number.
def squareNumbers(n):
  if n>0:
    squareNumbers(n-1)
    print(n*5)
number = int(input('Enter the number:'))
squareNumbers(number)


#TODO: 10. Write a recursive python function to print a number in reverse order.

def reverseNumber(n):
  if n>0:
    a = n%10
    b = n//10
    n=b
    print(a, end="")
    reverseNumber(n)
    

number = int(input('Enter the number:'))
reverseNumber(number)