import yt_dlp

def download_twitter_video(tweet_url, output_filename):
    ydl_opts = {
        'outtmpl': output_filename,
        'format': 'best',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([tweet_url])

tweet_url = 'https://twitter.com/Dogepay_DRC20/status/1791286483175063586'
output_filename = 'twitter_video.mp4'

download_twitter_video(tweet_url, output_filename)
print(f"Video downloaded as {output_filename}")
