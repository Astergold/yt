import subprocess

VBR = "2500k"
FPS = "30"
QUAL = "medium"
YOUTUBE_URL = "rtmp://a.rtmp.youtube.com/live2"
SOURCE = "test.mp4"
KEY = "8hjc-0pvx-bwzk-4brb-50p3"

command = [
    "ffmpeg",
    "-stream_loop", "-1", "-i", SOURCE, "-deinterlace",
    "-vcodec", "libx264", "-pix_fmt", "yuv420p", "-preset", QUAL, "-r", FPS, "-g", str(int(FPS) * 2), "-b:v", VBR,
    "-acodec", "libmp3lame", "-ar", "44100", "-threads", "6", "-qscale", "3", "-b:a", "712000", "-bufsize", "512k",
    "-f", "flv", f"{YOUTUBE_URL}/{KEY}"
]

subprocess.run(command)