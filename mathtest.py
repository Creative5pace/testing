
def myotherfuntion(myparam):
    return "My other function is returning this new value from Shawon" + myparam

def myfunction(w, x, y, z):
    print(myotherfuntion(z))



    #
    # d = sys.argv[2]
    # print("my text is "+d)
    #
    # c = a + b
    # print(c)
    #
    #
    # c += a
    # print(c)
    #
    # c *= a
    # print(c)
    #
    # c /= a
    # print(c)
    #
    # c = 2
    # c %= a
    # print(c)
    #
    # c = 10
    # c **= a
    # print(c)
    #
    # c //= a
    # print(c)
    #

    return w + x + y

import sys
import spellingtest

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = sys.argv[4]
e = sys.argv[5]
result = myfunction(a, b, c, d)
print("This is printing the functions return value outside of my function " + str(result))
mymisspelledtext = spellingtest.spellcheck(e)
print(mymisspelledtext)
