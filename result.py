#coding:utf-8
import cgi
import cgitb
from pytube import YouTube

def download_youtube_video(video_url, output_path=""):
    try:
        youtube = YouTube(video_url)
        video_stream = youtube.streams.get_highest_resolution()
        video_stream.download(output_path)
        print(f"Video downloaded successfully to {output_path}")

    except Exception as e:
        print(f"Error: {e}")



cgitb.enable()
form = cgi.FieldStorage()

if form.getvalue("videoLink"):
    videoLink = form.getvalue("videoLink")
    download_youtube_video(videoLink)
    
    print("Content-type: text/html; charset=utf-8\n")

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>YT video downloader</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Overpass+Mono:wght@300..700&display=swap');
            body{
                font-family: "Overpass Mono", monospace;
                background-color: #381260;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                }

            .result {
                font-family: "Overpass Mono", monospace;
                padding: 20px;
                color:White;
            }
        </style>
    </head>
    <body>
        <div class="result">
           <h1>Thank you for !</h1>
        </div>
    </body>
    </html>

    """

    print(html)

else:
    raise Exception("Pseudo non transmis")
