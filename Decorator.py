def log_decorater(fun):
    def wapper():
        print("before")
        fun()
        print("after")
    return wapper
@log_decorater
def greetin():
    print("hello")
greetin()