x="global"

def outer():
    x="enclosing"
    def inner():
        x="local"
        print("inner:",x)
    inner()
    print("outer:",x)
outer()
print("global:",x)
