calls = 0

def count_calls():
    global calls
    calls = 4

def string_info(string):
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return length, upper, lower

def is_contains(string, list_to_search):
    for i in list_to_search:
        if string.lower().startswith(i.lower()):
            return True
    return False


print(string_info('Capybara'))
count_calls()
print(string_info('Armageddon'))
count_calls()
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
count_calls()
print(is_contains('cycle', ['recycling', 'cyclic']))
count_calls()
print(calls)
