'''
Error handlings:
----------------

try block: the try block , test the block of code for an error.


except block : the except block let hand if the code contain errors.

else block : this will be excuted , if the try block has no error in the code.

finally block : this will be execute either try block contains error or not.

#1
try :
    print(3/0)

except:
    print("This will handle zerodivisionerror")
------------------------------------
#2
try :
    a = int("sravya")
    print(a)

except:
    print("an int error occur")
------------------------------------
#3    
try :
    a = "sravya"
    print(a)

except:
    print("an int error occur")

else:
    print("no error")

    
------------------------------------
#4
try :
    print(5+"asf")
    
except NameError:
    print("This will handle NameError")
    
else:
    print("no error")
-----------------------------
#note -->>

try :
    print(a)
    
    print(5+"asf")

except TypeError:
    print("This will handle TypeError")
     
except NameError:
    print("This will handle NameError")
    
else:
    print("no error")
    
-------------------------------------------------------------------------------------------

try :
    print(a)
    print("Hai")

except :
    print("error")

else :
    print("no error")

finally :
    print("the end")
    


























    
    
