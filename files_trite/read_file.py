s = """\
AAA
BBB
CCC
DDD
"""
with open('some_file/somefiles/test.txt','w') as f:
    f.write(s)

# with open('./somefiles/test.txt','r') as f:
#     # print(f.read())
#     while True:
#         chunk = 2
#         # line = f.readline()
#         line = f.read(chunk)
#         print(line, end='\n')
#         if not line:
#             break