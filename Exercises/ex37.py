#KEYWORDS
#and (True and False == False)
#as (part of with-as statement) (with X as y : pass)
#assert (to ensure something is true) (assert False, "Error!")
#break (stop the loop) (while True: break)
#class (define a class) (class Person(object))
#continue (dont process more of the loop, do it again) (while True : continue)
#def (define a function) (def X(): pass)
#del (delete from dictionary)( del X[Y})
#elif (else if condition) (if: X; elif:Y; else:J)
#else (else condition) (if:X; elif:Y; else:J)
#except (if an exception happens, do this)(except ValueError, e: print e)
#exec (run a string as python)(exec 'print Hello')
#finally (exceptions or not, do this)(finally:pass)
#for (loop over a collection)(for X in Y: pass)
#from (importing a specific modular part)(import X from Y)
#global (declare that you want a global variable)(global X)
#if (if condition)(if: X; elif: Y; else: J)
#import (import a module into this one)(import os)
#in (part of for-loops. also in a test of X in Y)(for X in Y:pass OR 1 in [1] == True)
#is (like == to test equality)(1 is 1 == True)
#lambda (create a short anonymous function)(s = lambda y: y**y; s(3))
#not (logical not)(not True == False)
#or (logical or)(True or False == True)
#pass (this block is empty)(def empty(): pass)
#print (print this)(print 'this string')
#raise (raise an exception when things go wrong)(raise Value Error("No")
#return (exist the function with a return value)(def X(): return Y)
#try (try this block and, if an exception, go to except)(try : pass)
#while (while loop)(While X : pass)
#with (with an expression as a variable do)(with X as Y:pass)
#yield (pause here and return to caller)(def X(): yield Y; X().next())


#STRING ESCAPE SEQUENCES
# \\ backslash
# \' single quote
# \" double quote
# \a Bell
# \b backspace
# \f Formfeed
# \n newline
# \r carriage
# \t tab
# \v vertical tab


#STRING FORMATS
# %d (decimal integers not floats)("%d" % 45 == '45')
# %i (same as %d) ("%i" % 45 == '45')
# %o (octal number) ("%o" % 1000 == '1750')
# %u (unsigned decimal) ("%u" % -1000 == '-1000')
# %x (hexadecimal lowercase) ("%x" % 1000 == '3e8')
# %X (hexadecimal uppercase)("%X" % 1000 == '3E8')
# %f (floating point number) ("%f" % 10.34 == '10.340000')
# %F (same as %f)
# %g (either %f or %e whichever is shorter)("%g" % 10.34 == '10.34')
# %G (same as G but uppercase)
# %c (character format) ("%c" % 34 == '"')
# %r (repr format for debugging) ("%r" % int == "<type 'int'>")
# %s (string format) ("%s there" % 'hi' == 'hi there')
# %% (percent sign) ("%g%%" % 10.34 == '10.34%')

#TAKING NOTES ON PYTHON CODE
#1 Find functions and figure out what they do
#2 Where each variables is first given a value
#3 Any variables with the same name in later parts of the program
#4 Any if-statements without else clauses and if they are right
#5 Any while-loops that might not end
#6 Any parts of code that you can't understand for whatever reason


