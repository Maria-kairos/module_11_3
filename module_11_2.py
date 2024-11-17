import inspect

class Class1():
    at = 1
    def test(x):
        pass

def introspection_info(item):
    a = type(item)
    b = dir(item)
    attributes = []
    methods = []
    ignore_list = ["__class__", "__dir__", "__init__", "__module__", "__weakref__", "__dict__"]
    for i in b:
        attr = getattr(item, i)
        if i in ignore_list:
            methods.append(i)
        else:
            attributes.append(i)
    d = inspect.getmodule(item)
    print(f'Тип объекта: {a}')
    print(f'Атрибуты объекта: {b}')
    print(f'Методы объекта: ')
    print(f'Модуль объекта: {d}')

number_info = introspection_info(42)
print(number_info)

number_info = introspection_info(introspection_info)
print(number_info)

number_info = introspection_info(Class1)
print(number_info)

number_info = Class1()
numbe = introspection_info(number_info)
print(numbe)




