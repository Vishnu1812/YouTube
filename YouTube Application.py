# Simple YouTube Application
from pytube import YouTube, Playlist
from datetime import timedelta
from pathlib import Path

directory = str(Path.home() / "Downloads")
try:
    with open("YouTube Data.txt", "r"):
        pass

except IOError:
    with open("YouTube Data.txt", "a") as file:
        file.write(":::::::::::::::::::::::::::::::::YouTube Playlist Data::::::::::::::::::::::::::::::::::::::::::::")


def file_summary():
    def video_summary():
        print("\nPlease wait, pulling data from YouTube...".upper())
        print("Video File Summary:")
        print(f"Video File Name : {link.title}")
        print(f"Audio File Size : {round(link.streams.get_audio_only().filesize / 1048576, 2)} Mb")
        print(f"Video File Size : {round(link.streams.get_highest_resolution().filesize / 1048576, 2)} Mb")

    def audio_download():
        print("Audio File Download Started...")
        link.streams.get_audio_only().download(directory)
        print("File Download Completed.")
        print(f"Downloaded Files Found Here : {directory}")

    def video_download():
        print("Video File Download Started...")
        link.streams.get_highest_resolution().download(directory)
        print("File Download Completed.")
        print(f"Downloaded Files Found Here : {directory}")

    while True:
        url = input("\nEnter Video Link or 'Quit' To Cancel: ")
        if len(url) >= 28:
            break
        if len(url) < 28 and url.lower() != 'quit':
            print("Please check and enter proper URL!".upper())
        if url.lower() == 'quit':
            print("Task Cancelled!".upper())
            print("Good Bye")
            quit()

    link = YouTube(url)
    video_summary()

    option = input("\nDo you want to download this file? (Yes or No): ")
    if option.lower() == 'yes':
        choice = input("\nEnter Audio or Video: ")
        if choice.lower() == 'audio':
            audio_download()

        if choice.lower() == 'video':
            video_download()

        if choice.lower() not in ['audio', 'video']:
            print("\nInvalid Entry. Enter Only 'Audio' or 'Video'!")

    if option.lower() == 'no':
        print("\nFile download canceled...".upper())

    if option.lower() not in ['yes', 'no']:
        print("\nInvalid Entry. Enter Only 'Yes' or 'No'!")


def playlist_summary():
    link = input("\nEnter Playlist Link: ")
    print("\nPlease wait, pulling data from YouTube...\n".title())
    yt_playlist = Playlist(link)

    temp_data = []

    total_playlist_duration = 0
    total_audio_file_size = 0
    total_video_file_size = 0

    for video in yt_playlist.videos:
        file_link = video.watch_url
        file_name = video.title

        file_length = f"{timedelta(seconds=int(video.length))}"
        total_playlist_duration = total_playlist_duration + int(video.length)

        audio_file = round(video.streams.get_audio_only().filesize / (1024 * 1024), 2)
        total_audio_file_size = total_audio_file_size + audio_file

        video_file = round(video.streams.get_highest_resolution().filesize / (1024 * 1024), 2)
        total_video_file_size = total_video_file_size + video_file
        print()
        print(f"File Name             : {file_name}")
        print(f"URL                   : {file_link}")
        print(f"File Length           : {file_length}")
        print(f"Audio File Size In Mb : {audio_file}")
        print(f"Video File Size In Mb : {video_file}")

        file_data = [file_name, file_link, file_length, audio_file, video_file]
        temp_data.append(file_data)
    print()
    print(f"Total Videos In Playlist                 : {len(yt_playlist)}")
    print(f"Total Playlist Duration (HH:HH:HH)       : {timedelta(seconds=total_playlist_duration)}")
    print(f"Total Playlist Audio Files Download Size : {total_audio_file_size}")
    print(f"Total Playlist Video Files Download Size : {total_video_file_size}")

    back_up = input("\nDo you want to backup this playlist(Y or N): ".title())

    if back_up.lower() == "y":
        for item in temp_data:
            with open("YouTube Data.txt", "a") as f:
                f.write(f"Name       : {item[0]}\n")
                f.write(f"Link       : {item[1]}\n")
                f.write(f"Duration   : {item[2]}\n")
                f.write(f"Audio Size : {item[3]}\n")
                f.write(f"Video Size : {item[4]}\n")

    if back_up.lower() == 'n' and back_up.lower() not in ['y', 'n']:
        print("Ok Fine...")


def playlist_download():
    playlist = Playlist(input("\nEnter Playlist Link: "))

    print(f"\nTotal Files In Playlist: {len(playlist)}")

    def audio_playlist():
        print("\nAudio Playlist Download Started...")
        count = 0
        for f in playlist.videos:
            count = count + 1
            f.streams.get_audio_only().download(directory)
            print(f"{count} of {len(playlist)} downloaded...")
        print("Playlist Download Completed.")
        print(f"Downloaded Files Found Here : {directory}")

    def video_playlist():
        print("\nVideo Playlist Download Started...")
        count = 0
        for f in playlist.videos:
            count = count + 1
            f.streams.get_highest_resolution().download(directory)
            print(f"{count} of {len(playlist)} downloaded...")
        print("Playlist Download Completed.")
        print(f"Check for files here: {directory}")

    print("\nDownload Options:")
    choice = input("Audio or Video: ")

    if choice.lower() == 'audio':
        audio_playlist()

    if choice.lower() == 'video':
        video_playlist()


def read_data():
    with open("YouTube Data.txt", "r") as f:
        read_list = []
        for line in f:
            read_list.append(line.strip())
    print(f"\n{read_list[0]}\n")
    read_list.pop(0)
    count = 0
    for item in read_list:
        print(item)
        count += 1
        if count == 5:
            print()
            count = 0


def clear_file():
    with open("YouTube Data.txt", "r+") as f:
        line_length = len(f.readline())
        f.seek(line_length)
        f.truncate()
        print("\nData cleared!".upper())
        print("!!!!!!!!!!!!!!!")


def user_choice():
    print("\nPlease choose From Below:")
    print("1. Download Single YouTube File")
    print("2. Get YouTube Playlist Summary")
    print("3. YouTube Playlist Download")
    print("4. Read Data File")
    print("5. Clear Data From File")
    print("6. Quit Application")
    choice = int(input("\nChoose 1, 2, 3, 4, 5, 6: "))

    if choice == 1:
        file_summary()
    if choice == 2:
        playlist_summary()
    if choice == 3:
        playlist_download()
    if choice == 4:
        read_data()
    if choice == 5:
        clear_file()
    if choice == 6:
        print("\nGood Bye!")
        quit()
    if choice not in [1, 2, 3, 4, 5, 6]:
        print("Invalid Entry!".upper())
        print("Good Bye")


while True:
    user_choice()
