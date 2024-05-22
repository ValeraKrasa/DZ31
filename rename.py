import os

list_files = []
new_list_files = []


path_to_dir = input('Введіть шлях до файлів - ')
path_to_new_dir = input('Введіть шлях до нової папки - ')
shablon_name_file = input('Введіть шаблон імені нового файлу - ')

if not os.path.isdir(path_to_new_dir):
    os.mkdir(path_to_new_dir)

tempa = os.listdir(path_to_dir)

for file in tempa:
    if file.endswith('.7z'):
        list_files.append(file)
        new_list_files.append(shablon_name_file + file[-5:])

for i in range(len(list_files)):
    path_to_file = path_to_dir + '\\' + list_files[i]
    path_to_new_file = path_to_new_dir + '\\' + new_list_files[i]
    os.rename(path_to_file, path_to_new_file)
    
answer = input('Видалити стару папку? (Y/n) - ')
if answer.lower() == 'y':
    os.rmdir(path_to_dir)

print('Робота завершена. До зустрічі мій любий користувач ))))')
