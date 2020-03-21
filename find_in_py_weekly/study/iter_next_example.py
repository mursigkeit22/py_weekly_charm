mylist = ['qw', 'we', 'qw', 'wae', 'qw', 'we', 'qbw', 'hop', 'qw', 'we', 'qw', 'we', ]
myiterlist = iter(mylist)
print(type(myiterlist))
count = 0
for el in myiterlist:
    print(el)
    if 'a' in el:
        while True:
            count += 1
            print(count)
            el = next(myiterlist)
            if 'b' in el:
                break
