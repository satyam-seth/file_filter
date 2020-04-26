import os,shutil

dict_extensions = {
    'Audio_extensions': ('.mp3','.wma','.aac','wav','.aiff','.flac','.ogg','.alac'),
    'Video_extensions': ('.mp4','.mov','.avi','.mkv','.webm','.wmv','.mpeg','.swf'),
    'Image_extensions': ('.png','.jpg','.jpge','.bmp','.wmf','.svg','.gif','.tiff','.eps'),
    'Document_extensions': ('.txt','.pdf','.docx','.doc','.ppt','.pptx','.ppsx','.xls','.xlsx','xlsm','.csv','.odt','.rtf','.ods'),
    'Programs_extensions':('.c','.cpp','py','.java','.php','.js','.cs','.css','.xml','.jsp','.pl','.rb','html','.htm','.rhtml','.jhtml','.xhtml','.asp','.dll','.cgi','.exe')
}

folder_path = input('Enter folder path:')

def file_finder(folder_path, file_extensions):
    files = []
    for file in os.listdir(folder_path):
        for extension in file_extensions:
            if file.endswith(extension):
                files.append(file)
    return files

i = 1
for extension_type, extension_values in dict_extensions.items():
    folder_name = str(i)+'.'+extension_type.split('_')[0] + ' Files'
    new_folder_path = os.path.join(folder_path, folder_name)
    try:
        os.mkdir(new_folder_path)
    except FileExistsError:
        pass
    i += 1
    for file in file_finder(folder_path, extension_values):
        file_path = os.path.join(folder_path, file)
        file_new_path = os.path.join(new_folder_path, file)
        shutil.move(file_path, file_new_path)
else:
    print('Job Done..')
_=input()