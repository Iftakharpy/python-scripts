import os
import moviepy.editor as movie

# # Create an object by passing the location as a string
# video = movie.VideoFileClip(r"D:\Programs\useful python scripts\1. Introduction to the Course\1. What is Machine Learning.mp4")
# # Contains the duration of the video in terms of seconds
# video_duration = video.duration


class Convert_Time:
    def __init__(self, seconds):
        self.seconds = seconds
        self.minutes = self.seconds//60
        self.hours = self.minutes//60
        self.days = self.hours//24

    def conversions(self):
        return f"days:{self.days}\nhours:{self.hours}\nminutes:{self.minutes}\nseconds:{self.seconds}"

    def __repr__(self):
        seconds = self.seconds % 60
        minutes = (self.seconds//60) % 60
        hours = (self.seconds//(60*60)) % 24
        days = (self.seconds//(60*60))//24
        return f"days:{days}, hours:{hours}, minutes:{minutes}, seconds:{seconds}"


def get_video_files(base_path=None, file_types=None, seperator=','):
    """
    This function takes 2 parameters. \nbase_path(as string) and \nfile_types(as string seperated by ',' if you want to delete multiple file types)\n
    function gets into all the subdirectories and deletes all the specified file types from the subdirectories including the base_path directory.\n
    if base_path is not specified then it sets the base_path as current working directory returned from\n
    os.getcwd()
    """
    # setting the current directory as base_path is base_path doesn't exist
    if not base_path:
        base_path = os.getcwd()

    # getting all the nested directories including the current directory
    # paths = [x for x in os.walk(base_path)]

    # if file type is not passed then setting all the file types for the videos
    default_file_types = ['3g2', '3gp', '3gp2', '3gpp', '3gpp2', 'OP-Atom', 'OP1a', 'aaf', 'asf', 'avchd', 'avi', 'drc', 'f4a', 'f4b', 'f4p', 'f4v', 'flv', 'gxf', 'lxf', 'm2v', 'm4a', 'm4b', 'm4p', 'm4r', 'm4v',
                        'mkv', 'mng', 'mov', 'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv', 'mxf', 'nsv', 'oga', 'ogg', 'ogv', 'ogx', 'qt', 'rm', 'rmvb', 'roq', 'svi', 'ts', 'tsa', 'tsv', 'vob', 'wav', 'wave', 'webm', 'wma', 'wmv', 'yuv']
    if not file_types:
        file_types = default_file_types

    # seperating the file types by seperator from the file_types parameter
    if type(file_types)==str:
        file_types = [f_type.strip() for f_type in file_types.split(seperator)]
    if not file_types:
        raise ValueError("You haven't specified any file type")
    # getting into all the directories and delleting the target file_types
    files = []
    for details in os.walk(base_path):
        for file_name in details[2]:
            if file_name.split('.')[-1] in default_file_types:
                files.append(os.path.abspath(os.path.join(details[0],file_name)))
    # for file in files:
    #     print(file)
    return files

def get_total_duration(video_files):
    """
    Gets the duration of the files in the video_files_parameter and returns length of the videos in seconds
    """
    # Video duration in Seconds
    total_duration = 0
    for video in video_files:
        try:
            vid_duration = movie.VideoFileClip(video).duration
            total_duration += vid_duration
        except OSError as e:
            print('Error:',e,'\n\n')
            continue
        if vid_duration:
            del(vid_duration)

    return total_duration
print()
try:
    time = Convert_Time(get_total_duration(get_video_files()))
    print(time)
    print(time.conversions())
except OSError:
    pass

input('')