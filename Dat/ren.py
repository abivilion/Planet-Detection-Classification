import os, fnmatch

file_path = 'D:\\\Machine Learning\\Project\\Image Classification\\Mercury\\'

files_to_rename = fnmatch.filter(os.listdir(file_path), '*.jfif')

new_name = 'image'

for i, file_name in enumerate(files_to_rename):
    print(i)
    print(file_name)


    new_file_name = new_name + str(i) + ".jpg"

    
    os.rename(file_path + file_name, 
          file_path + new_file_name)