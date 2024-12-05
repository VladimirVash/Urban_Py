calls = 0

def string_info(string):
    count_calls(calls)
    res = tuple([len(string), string.upper(), string.lower()])
    return res

def is_contains(string, list_to_search):
     count_calls(calls)
     for s in list_to_search:
         if string.lower() in s.lower():
             return True
     else:
         return False

def count_calls(call):
    global calls
    calls += 1



print(string_info('Capybara'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(string_info('Armageddon'))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)