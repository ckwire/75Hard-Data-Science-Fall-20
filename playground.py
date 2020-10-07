#Errors & Exceptions

f = open('C:\\Users\\chad\\Desktop\\somefile.txt')
'''
x = -4
if x < 0:
    raise Exception('X should be positive')'''

try:
    a = 5 / 10
#except:
#   print('An error occurred!')
#except Exception as e:
#    print(e)
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('{} {}'.format("Everything is fine! Answer is", a))