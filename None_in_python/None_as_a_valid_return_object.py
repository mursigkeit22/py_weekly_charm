#You can use this technique when None is a possibility for return values, too.
# For instance, dict.get returns None by default
# if a key is not found in the dictionary.
# If None was a valid value in your dictionary,
# then you could call dict.get like this:


class KeyNotFound: pass


my_dict = {'a':3, 'b':None}
for key in ['a', 'b', 'c']:
    value = my_dict.get(key, KeyNotFound)
    if value is not KeyNotFound:
        print(f"{key}: {value}")
# Here you’ve defined a custom class KeyNotFound.
# Now, instead of returning None when a key isn’t in the dictionary,
# you can return KeyNotFound.
# That frees you to return None when that’s the actual value in the dictionary.
