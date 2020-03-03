# what if good_function() could either add an element to the list or not,
# and None was a valid element to add? In this case,
# you can define a class specifically for use as a default,
# while being distinct from None


class DontAppend: pass


def valid_none(new_element=DontAppend, starter_list=None):
    if starter_list is None:
        starter_list = []
    if new_element is not DontAppend:
        starter_list.append(new_element)
    return starter_list

# Here, the class DontAppend serves as the signal not to append,
# so you don’t need None for that.
# That frees you to add None when you want.
my_list = [1, 2, 3, 4, ]
print(valid_none(starter_list=my_list))
print(valid_none(new_element=None, starter_list=my_list))
