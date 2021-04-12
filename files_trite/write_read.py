s = """\
AAA
BBB
CCC
DDD
"""

# with open('some_file/somefiles/test.txt','w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

with open('./somefiles/test.txt','r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)