def my_func(**myvar):
    print("arguments as a type : ", type(myvar))
    print("name:", myvar["name"])
    print("age:", myvar["age"])
    print("all data:", myvar)
my_func(name="devyani", age=20, city="pune")
