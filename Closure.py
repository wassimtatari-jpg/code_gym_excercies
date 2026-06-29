def make_filter(thershold):
    def fuction_filter(value):
        return value>thershold
    return fuction_filter
data=[1,2,3,4,10,20,30,40,100,200,300,400]
filter1=make_filter(2)
filter2=make_filter(50)
filter3=make_filter(350)
result1=list(filter(filter1,data))
result2=list(filter(filter2,data))
result3=list(filter(filter3,data))
print(result1)
print(result2)
print(result3)