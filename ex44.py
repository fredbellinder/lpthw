# inheriting a parent method

# class Parent (object):
#     def implicit(self):
#         print("PARENT implicit()")


# class Child(Parent):
#     pass


# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()


'''
ex44b.py
explicitly overriding a parent method
'''

# class Parent (object):

#     def override(self):
#         print("PARENT override()")


# class Child(Parent):

#     def override(self):
#         print("CHILD override()")


# dad = Parent()
# son = Child()

# dad.override()
# son.override()


'''
ex44b.py
alter the parent method, override but still call parent method with super()
'''


# class Parent (object):

#     def altered(self):
#         print("PARENT altered() even though overridden")


# class Child(Parent):

#     def altered(self):
#         print("CHILD before PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD after PARENT altered()")


# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()


'''
    implicit, override and alter, altogether
'''

# class Parent(object):

#     def override(self):

#         print("PARENT override()")

#     def implicit(self):

#         print("PARENT implicit()")

#     def altered(self):

#         print("PARENT altered()")


# class Child(Parent):

#     def override(self):
#         print("CHILD override()")

#     def altered(self):
#         print("CHILD before PARENT altered()")
#         super(Child, self).altered()
#         print("CHILD after PARENT altered()")


# dad = Parent()
# son = Child()

# # both of the below will run the implicit() implemented in Parent()
# dad.implicit()
# son.implicit()

# # will run the override() in the parent class
# dad.override()
# # will run the childs overriding override()
# son.override()

# # will run the altered() in the parent class
# dad.altered()
# # will run the childs overriding method with the super() call for the parent method that was overridden
# son.altered()

'''
    Composition
'''


class Other(object):

    def override(self):
        print("OTHER override")

    def implicit(self):
        print("OTHER implicit")

    def altered(self):
        print("OTHER altered")


class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD AFTER OTHER altered()")


son = Child()

son.implicit()
son.override()
son.altered()
