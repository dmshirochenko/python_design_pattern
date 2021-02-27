#!/usr/bin/env python3

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, data_type):
        self.data_type = data_type
        self.request_method = 'get'


class EventSet:
    def __init__(self, data_value):
        self.data_value = data_value
        self.request_method = 'set'


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, some_object, event):
        if self.__successor is not None:
            return self.__successor.handle(some_object, event)


class IntHandler(NullHandler):
    def handle(self, some_object, event):
        if event.request_method == 'get':
            if event.data_type is int:
                return some_object.integer_field
            else:
                print(f"Event sent to another handler from Int Handler")
                return super().handle(some_object, event)
        elif event.request_method == 'set':
            if type(event.data_value) is int:
                some_object.integer_field = event.data_value
            else:
                print(f"Event sent to another handler from Int Handler")
                return super().handle(some_object, event)
        else:
            print('Wrong request method')


class FloatHandler(NullHandler):
    def handle(self, some_object, event):
        if event.request_method == 'get':
            if event.data_type is float:
                return some_object.float_field
            else:
                print(f"Event sent to another handler from FloatHandler Handler")
                return super().handle(some_object, event)
        elif event.request_method == 'set':
            if type(event.data_value) is float:
                some_object.float_field = event.data_value
            else:
                print(f"Event sent to another handler from FloatHandler Handler")
                return super().handle(some_object, event)
        else:
            print('Wrong request method')


class StrHandler(NullHandler):
    def handle(self, some_object, event):
        if event.request_method == 'get':
            if event.data_type is str:
                return some_object.string_field
            else:
                print(f"Event sent to another handler from StrHandler Handler")
                return super().handle(some_object, event)
        elif event.request_method == 'set':
            if type(event.data_value) is str:
                some_object.string_field = event.data_value
            else:
                print(f"Event sent to another handler from StrHandler Handler")
                return super().handle(some_object, event)
        else:
            print('Wrong request method')



if __name__ == '__main__':

    obj = SomeObject()
    obj.integer_field = 42
    obj.float_field = 3.14
    obj.string_field = "some text"
    chain = IntHandler(FloatHandler(StrHandler(NullHandler)))

    print(chain.handle(obj, EventGet(int)))
    print(chain.handle(obj, EventGet(float)))
    print(chain.handle(obj, EventGet(str)))

    chain.handle(obj, EventSet(100))
    print(chain.handle(obj, EventGet(int)))

    chain.handle(obj, EventSet(0.5))
    print(chain.handle(obj, EventGet(float)))

    chain.handle(obj, EventSet('new text'))
    print(chain.handle(obj, EventGet(str)))
