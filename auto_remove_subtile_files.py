import os


def reomve_files(base_path=None,file_types=None):
    """
    This function takes 2 parameters. \nbase_path(as string) and \nfile_types(as string seperated by ',' if you want to delete multiple file types)\n
    function gets into all the subdirectories and deletes all the specified file types from the subdirectories including the base_path directory.\n
    if base_path is not specified then it sets the base_path as current working directory returned from\n
    os.getcwd()
    """
    #setting the current directory as base_path is base_path doesn't exist
    if not base_path:
        base_path = os.getcwd()

    #getting all the nested directories including the current directory
    paths = [x for x in os.walk(base_path)]

    #if file type is not passed then setting all the file types for the subtitles
    default_file_types = 'srt,vtt,ssa,ttml,sbv,dfxp' 
    if not file_types:
       file_types = default_file_types

    #seperating the file types by comma(',') from the file_types parameter
    file_types = file_types.split(',')

    #getting into all the directories and delleting the target file_types
    for i in range(1,len(paths)):
        if paths[i][2]:
            print(f'Deleting subtitles from dir : {paths[i][0]}')
            os.chdir(paths[i][0])
            for file_type in file_types:
                os.system(f'del *.{file_type}')
        print('\n\n')

print('You can keep input fields empty if you want to use default parameters')
print('Current working driectory :',os.getcwd())
print('Defalut file types are : srt,vtt,ssa,ttml,sbv,dfxp\n')

base_path = input("Enter the path of the directory you want to delete subtitles from.\n")
file_types = input("Specify the file types you want to delete.\nNote: seperate mutiple file types by comma(',')\n")

reomve_files(base_path,file_types)
print('Successfully deleted all the specified file types')
input('press enter to exit\n')