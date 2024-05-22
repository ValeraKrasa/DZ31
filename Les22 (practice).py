

##import os
##
##
##files = []
##files_pdf = []
##
##path = input('Enter a path  - ')
##
##if os.path.isdir(path):
##    files = os.listdir(path)
##    for obj in files:
##        if str(obj).endswith('.pdf'):
##            #option 1
##            #files_pdf.append(str(obj).replace('.pdf',''))
##            #option 2
##            files_pdf.append(str(obj)[:obj.rindex('.')])
##           
##        else:
##            continue
##
##else:
##    print("Please double check")
##
##for file in files_pdf:
##    print(file)
##
###os.listdir(path)
##
##
##
##def tempa(path):
##    global files_pdf
##    objects = os.listdir(path)
##    for obj in objects:
##        new_path = path + '//' +obj
##        if os.path.isfile(new_path):
##             if str(obj).endswith('.pdf'):
##                 files_pdf.append(str(obj)[:obj.rindex('.')])
##        else:
##            new_objects = os.listdir(new_path)
##            for new_obj in new objects:
##                if os.path.isfile(new_path):
##                    if str
##            
##
##files_pdf = []
##
##path = input('Enter path - ')
##
##if os.path.isdir(path):
##    tempa(path)





def cars(num1, num2, num3):
    pass


































