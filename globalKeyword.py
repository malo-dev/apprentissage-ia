x="hello malod"
def myfunc():
    global x
    x="hello world"
    print("inside function:",x)
myfunc()
print("outside function:",x)