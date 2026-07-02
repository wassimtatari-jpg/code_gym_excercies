def repeat(num_times):
    def repeat_funcation(func):
        def wapper(*agre,**kawagre):
            for _ in range(num_times):
                func(*agre,**kawagre)
        return wapper
    return repeat_funcation
@ repeat(num_times=5)
def say_hello(name):
    print(f"hello {name}")
say_hello("wassim")
