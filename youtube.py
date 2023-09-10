from pytube import YouTube
link = "https://www.youtube.com/watch?v=-mJFZp84TIY&list=PLu0W_9lII9agx66oZnT6IyhcMIbUMNMdt&index=1"

SAVE_PATH = "C:/Users/ShanuPC/OneDrive/Desktop/UMESH/C++ & DSA"

try:
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution')[-1].download(SAVE_PATH)
    print('Video Downloaded!')
except Exception as e:
    print("Error occurred!\n", e)

print("Ended")