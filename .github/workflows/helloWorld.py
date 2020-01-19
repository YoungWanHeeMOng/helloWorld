
print("Enter a number . Please enter zero(0) to exit")

i=0
sum=0

while i<5:
    sum +=i
    print("Add number sum is ", sum)
    i +=1

A = [0,1,2,3,4,5] # list
B = (0,1,2,3,4,5) # tuple
C = {0,1,2,3,4,5} #set
D = '012345' # string
E = { # dictionay
    "name": 'max',
    "age": 20
}

for key, value in E.items():
    print(key, ' ', value)

def nameoffunction(arg, arg2):
    print(arg, ' ', arg2)

nameoffunction("YoungWan", "Kim")
nameoffunction(123,456)
nameoffunction(234.12,567.23)
nameoffunction("Hello", 1890)


class Hello:
    def __init__(self,name):
        self.name=name
        self.a=10
        self._b=23
        self.__c=54
    def get_color(self):
        return self.__c
      
       
hello=Hello('name')
print(hello.name)
print(hello.a)
print(hello._b)

print(hello.get_color())
