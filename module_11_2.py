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
    for i in b:
        if callable(i) == True:
            methods.append(i)
        if callable(i) == False:
            attributes.append(i)
    d = inspect.getmodule(item)
    print(f'Тип объекта: {a}')
    print(f'Атрибуты объекта: {attributes}')
    print(f'Методы объекта: {methods}')
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




