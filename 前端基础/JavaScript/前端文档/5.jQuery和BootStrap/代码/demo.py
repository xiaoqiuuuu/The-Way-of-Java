
name = "alvin"

s = "hello name"




class A(object):


    def foo(self):
        print("foo...")
        return self

    def bar(self):
        print("bar...")
        return self

a = A()
a.foo().bar()