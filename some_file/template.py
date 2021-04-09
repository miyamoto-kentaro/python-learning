import string

with open('./somefiles/template.txt','r') as f:
    print(f.read(),'\n##################')
    f.seek(0)
    t = string.Template(f.read())

contents = t.substitute(name='Mike', contents='How are you?')
print(contents)