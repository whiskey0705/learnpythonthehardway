# class Parent(object):

#     def __init__(self, hobby):
#         self.hobby = hobby


#     def implicit(self):
#         print('PARENT implicit()')

# class Child(Parent):
#     def implicit(self):
#         print('CHILD implicit()')

# dad = Parent('running')
# print(dad.hobby)
# dad.implicit()

# son = Child('reading')
# son.implicit()
# print(son.hobby)
# print(dad.hobby)

# 子类会继承父类的方法,如果子类有一样的方法则会覆盖父类的


class Parent(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


    def altered(self):
        print('PARENT altered()')

# super()的用法
class Child(Parent):
    def __init__(self, sex, name, age): # 除了新加的参数，还要传入父类的
        self.sex = sex
        super().__init__(name, age) # 如果没有super()，子类就不能调用父类的init

    def altered(self):
        print('CHILD, BEFORE PARENT altered()')
        # super(Child, self).altered()
        super().altered()
        print('CHILD, AFTER PARENT altered()')

# dad = Parent()
son = Child('boy', 'ww', 18)



# dad.altered()
# son.altered()
print(son.sex)
print(son.name)
print(son.age)

# Composition

class Other(object):
    def override(self):
        print('OTHER override()')

    def implicit(self):
        print('OTHER implicit()')

    def altered(self):
        print('OTHER altered()')

class Composition(object):
    def __init__(self):
        self.other = Other()

    def override(self):
        print('COMPOSITION override()')

    def implicit(self):
        self.other.implicit()

    def altered(self):
        self.other.altered()

com = Composition()
com.implicit()
com.override()
com.altered()

