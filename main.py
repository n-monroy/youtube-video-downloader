from pytube import YouTube
import humanize
import datetime
import os

# Set path to download the video
# You can change the path to any directory you want
# If you don't specify the path, the video will be downloaded in the same directory as the script
# Example: path = 'C:/Users/your_user_name/Downloads'
path = './downloads'

# Set the URL of the video
url = 'https://www.youtube.com/watch?v=oIur9NATg-I'


# Create the directory if it doesn't exist
if not os.path.exists(path):
    os.makedirs(path)

# Create a YouTube object
yt = YouTube(url)

# Set the video quality
# You can change the quality to any of the available qualities
# Example: yt.streams.get_by_itag(22)
#           yt.streams.get_highest_resolution()

# Progress bar in the console
def progress(stream, chunk, bytes_remaining):
    contentSize = stream.filesize
    size = contentSize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s] %.2f%%;' % (
        '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)),
        float(size/contentSize*100)), end='')
    

stream = yt.streams.get_highest_resolution()

yt.register_on_progress_callback(progress)
# Show the video title, author, duration, size, resolution, and format
print('Title:', yt.title)
print('Author:', yt.author)
print('Duration:', str(datetime.timedelta(seconds=yt.length)))
print('Size:', humanize.naturalsize(stream.filesize))
print('Resolution:', stream.resolution)
print('Format:', stream.mime_type)


# Download the video
stream.download(output_path=path)

print('\n\n')
print('Video downloaded successfully :)!')
