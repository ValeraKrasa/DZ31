##import os
##
##print(os.getcwd())


#File reading
# 3 stages of work with files
# 1. Opening
# 2. Reading/Recording
# 3. Closing

#f = open(file_name, access_mode)


f = open('text.txt', 'r')
print(f.name)
print(f.mode)
print(f.encoding)
print(*f)
