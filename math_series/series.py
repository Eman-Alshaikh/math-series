""" Create a function called fibonacci.
 The function should have one parameter n.
  The function should return the nth value in the fibonacci series.
   You may implement the function using recursion or iteration. 
   If you are feeling particularly frisky, do both as separate functions.

"""
def fibonacci (n):
    if n==0:
      return [0] 
    elif n==1:
      return [1]

    elif n==2:
        return [0,1]
    elif(n<0) : 
        return  []
    else : 
        x=fibonacci(n-1)

        #this line to sum the last two indexes 
        x.append(sum(x[:-3:-1]))
        return x  
""" add a new function lucas that returns the nth value in the lucas numbers 
Again, you may use recursion or iteration,
 

"""
def lucas (n):
  if n==0:
      return 2 
  elif n==1:
      return 1
  elif n>0:
      return lucas(n-1)+lucas(n-2)

  elif n<0:
   return lucas(n+2)-lucas(n+1)

"""Add a third function called sum_series with one required parameter
 and two optional parameters.
  The required parameter will determine which element in the series to print. 
  The two optional parameters will have default values of 0 and 1
   and will determine the first two values for the series to be produced.

 """
def sum_series(n,a=0,b=1):
  if n==0:
      return a
  elif n==1:
      return b

  else :
        
        
       return sum_series(n-1,a,b)+sum_series(n-2,a,b)