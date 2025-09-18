from pytube import YouTube
import os

def download_video():
    print("==== YouTube Video Downloader ====")
    url = input("Enter YouTube video URL: ")

    try:
        yt = YouTube(url)
        print(f"\nTitle: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Views: {yt.views}")

        # Show available streams
        print("\nAvailable Streams:")
        streams = streams = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc()
        for i, stream in enumerate(streams):
            print(f"{i+1}. {stream.resolution} ({stream.mime_type}, {round(stream.filesize / 1024 / 1024, 2)} MB)")

        choice = int(input("\nEnter choice (number): "))
        selected_stream = streams[choice - 1]

        # Download path
        path = input("Enter download path (press Enter for current folder): ").strip()
        if not path:
            path = os.getcwd()

        print("\nDownloading...")
        selected_stream.download(path)
        print(f"✅ Download completed! Saved to: {path}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    download_video()
