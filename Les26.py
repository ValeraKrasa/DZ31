# Задачка 1
# У пользователя получаем путь в папке. И затем
# необходимо сформировать список файлов и папок
# по этому пути...


# import os

# def tempa(path):
#     global files_pdf
#     objects = os.listdir(path)
#     for obj in objects:
#         new_path = path + '\\' + obj
#         if os.path.isfile(new_path):
#             if str(obj).endswith('.pdf'):
#                 files_pdf.append(obj[:obj.rindex('.')])
#         else:
#             # опращуем новый путь на файлы
#             new_objects = os.listdir(new_path)
#             for new_obj in new_objects:
#                 if str(new_obj).endswith('.pdf'):
#                     files_pdf.append(new_obj[:new_obj.rindex('.')])
                

# files_pdf = []

# path = input('Введите путь... - ')
# if os.path.isdir(path):
#     tempa(path)
# else:
#     print('Ошибка. Проверьте путь к папке...')

# for file in files_pdf:
#     print(file)

import os

def save_list_pdf_to_text():
    global files_pdf

    with open('list pdf.txt', 'a', encoding = 'utf_8') as f:
        for name_file in  files_pdf:
            f.write(str(name_file + '\n'))


def add_pdf_to_list(file):
    global files_pdf
    files_pdf.append(file)

def add_folder_to_list(folder):
    global embedded_folder
    embedded_folder.append(folder)

def list_dir(path):
    global embedded_folder
    objects = os.listdir(path)
    for obj in objects:
        new_path = path + '//' + obj
        if os.path.isfile(new_path): #file -> True
            new_obj = obj.lower()
            if str(obj).endswith('.pdf'):
                add_pdf_to_list(obj)
        else:
            add_folder_to_list(new_path)

if __name__ == '__main__':
    embedded_folder = []
    files_pdf = []

    path_to_dir = input('Enter a path to the folder - ')
    list_dir(path_to_dir)
    while len(embedded_folder) > 0:
        list_dir(embedded_folder[0])
        embedded_folder.remove(embedded_folder[0])

    print('Creation of the list ended')
    save_list_pdf_to_text()
    # print(files_pdf)
    # print(embedded_folder)

# if len(embedded_folder) == 0:
#     print('Creation of the list ended')
#     save_list_pdf_to_text()
# else: 
#     for name_folder in embedded_folder:
#        list_dir(name_folder)
#     embedded_folder.pop(0)














