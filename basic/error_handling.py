l = [1,2,3]
i = 5
# del l
try:
    l[i]
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print("Don't worry: {}".format(ex))
except Exception as ex:
    print("Don't worry: {}".format(ex))
else:
    print('done')
finally:
    print('clean up')