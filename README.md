# YoutubDownloader

Description:
This project utilizes the pytube library in Python to provide a simple way to download video resources from YouTube. It offers a user-friendly command-line interface that allows you to specify the URL of the video you want to download and save it locally. Whether you want to download a single video or an entire playlist, this project has got you covered. By leveraging the functionality of the pytube library, the project makes downloading videos from YouTube easy and efficient. With just a few lines of code, you can effortlessly access your favorite YouTube videos.

这个项目使用Python的pytube库，为你提供了一个简单的方式来下载YouTube上的视频资源。它提供了一个用户友好的命令行界面，让你能够指定要下载的视频的URL，并将其保存到本地。无论你是想下载单个视频还是整个播放列表，这个项目都能满足你的需求。通过利用pytube库的功能，该项目使得从YouTube下载视频变得简单而高效。只需几行代码，你就可以轻松获取你喜爱的YouTube视频。

# Usage
usage: YoutubeDownloader.py [-h] [-playList PLAYLIST] [-output OUTPUT] [-video VIDEO]  
  
options:  
  -h, --help          show this help message and exit  
  -playList PLAYLIST  URL of the playlist  
  -output OUTPUT      Output directory  
  -video VIDEO        Video url  
  
  ```shell
  python3 ./YoutubeDownloader.py -video https://www.youtube.com/watch\?v\=xxxx -output /path/to/your/destination
