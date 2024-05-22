import os

list_files = []
new_list_files = []

path_to_dir = input('Введите путь к файлам - ')
path_to_new_dir = input('Введите путь к новой папке - ')
shablon_name_file = input('Введите шаблон имени нового файла - ')

if not os.path.isdir(path_to_new_dir):
    os.mkdir(path_to_new_dir)

tempa = os.listdir(path_to_dir)

for file in tempa:
    if file.endswith('.7z'):
        list_files.append(file)
        file_name, file_ext = os.path.splitext(file)
        new_file_name = f"{shablon_name_file}{file_name[8:]}{file_ext}"
        new_list_files.append(new_file_name)

for i in range(len(list_files)):
    path_to_file = os.path.join(path_to_dir, list_files[i])
    path_to_new_file = os.path.join(path_to_new_dir, new_list_files[i])
    os.rename(path_to_file, path_to_new_file)

answer = input('Удалить старую папку? (Y/n) - ')
if answer.lower() == 'y':
    os.rmdir(path_to_dir)

print('Работа завершена.')
