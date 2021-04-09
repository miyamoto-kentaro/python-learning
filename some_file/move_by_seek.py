s = """\
AAA
BBB
CCC
DDD
"""
# with open('some_file/somefiles/test.txt','w') as f:
#     f.write(s)

with open('./somefiles/test.txt','r') as f:
    # print(f.read())
    print(f.tell()) #this is now row
    print(f.read(1))
    f.seek(5)
    print(f.read(1))
    f.seek(10)
    print(f.read(1))
    f.seek(15)
    print(f.read(1))