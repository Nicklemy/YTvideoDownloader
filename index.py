#coding:utf-8
import cgi 

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

        .login-container {
            background-color: #ccc;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 300px;
            text-align: center;
            
        }

        input {
            font-family: "Overpass Mono", monospace;
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
        }

        button {
            font-family: "Overpass Mono", monospace;
            background-color: black;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Youtube Video Downloader</h2>
        <form method="post" action="result.py">
            <label>video Link :</label>
            <input name="videoLink" required>

            <button type="submit">Download</button>
        </form>
        <p>By Nick-Lemy.K</p>
    </div>
</body>
</html>

"""

print(html)