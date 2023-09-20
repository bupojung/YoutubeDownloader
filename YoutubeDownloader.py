from pytube import YouTube
from pytube import Playlist
import argparse

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    print(f"Downloading... {percentage:.2f}%")
def downloadPlayList(playlist_url, output):
    print("Start download Playlist")
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        print("Downloading url: " + video_url)
        yt = YouTube(video_url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        video.download(output_path=output)
def downloadVideo(video_url, output):
    print("Start download video")
    print("Downloading url: " + video_url)
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video = yt.streams.get_highest_resolution()
    video.download(output_path=output)

# 创建解析器对象
parser = argparse.ArgumentParser()
# 添加 `-playList` 选项和参数
parser.add_argument('-playList', help='URL of the playlist')
# 添加 `-output` 选项和参数
parser.add_argument('-output', help='Output directory')
# 添加 `-video` 选项和参数
parser.add_argument('-video', help='Video url')

# 解析命令行参数
args = parser.parse_args()

# 获取 `-playList` 参数的值
playlist_url = args.playList

# 获取 `-output` 参数的值
output_directory = args.output

# 获取 `-video` 参数的值
video_url = args.video

if args.playList and args.output:
    print('Playlist URL is provided:', args.playList)
    print('Play list will save to derectory: ', args.output)
    downloadPlayList(args.playList, args.output)
elif args.video and args.output:
    print('Video URL is provided:', args.video)
    print('Video will save to derectory: ', args.output)
    downloadVideo(args.video, args.output)
else:
    parser.print_help()




