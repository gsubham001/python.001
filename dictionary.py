# for addition of new item in dictionary

my_dict = {'a':1,'b':2,'c' :3}
print(my_dict) # before add

my_dict['d'] ='4'
print(my_dict) # after add

# for removing of item in dictionary

my_dict = {'a':1,'b':2,'c':3}
print(my_dict) # before remove

my_dict.pop('c')
print(my_dict)

#updating the value in specific key

my_dict = {'a':1,'b':2,'c':3}
print(my_dict) #before update

my_dict['b']=4 # after update
print(my_dict)

# key exist

my_dict = {'a':1,'b':2,'c':3}
print(check_key(my_dict))

# for keys

my_dict = {'a':1,'b':2,'c':3}
print_key(my_dict)

