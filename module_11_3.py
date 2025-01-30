def introspection_info(obj):
    result = {}

    # Определение типа объекта
    result['type'] = type(obj).__name__

    # Получение атрибутов объекта
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    result['attributes'] = attributes

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    result['methods'] = methods

    # Определение модуля, к которому принадлежит объект
    try:
        module = obj.__module__
    except AttributeError:
        module = None
    result['module'] = module

    # Дополнительные свойства (например, документация)
    if hasattr(obj, '__doc__') and obj.__doc__:
        result['documentation'] = obj.__doc__.strip()
    else:
        result['documentation'] = None

    return result


# Пример использования функции с различными объектами
number_info = introspection_info(42)
print("Introspection of number 42:")
print(number_info)


# Создание собственного класса и его объекта для интроспекции
class MyClass:
    """Это документация для MyClass."""
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        self.instance_attribute = value

    def some_method(self):
        """Это документация для my_method."""
        print("Hello from my_method!")


# Создание объекта класса
my_object = MyClass(10)

# Интроспекция объекта класса
object_info = introspection_info(my_object)
print("\nIntrospection of MyClass instance:")
print(object_info)