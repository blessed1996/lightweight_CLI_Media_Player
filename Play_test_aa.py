import subprocess

subprocess.run(
    ["mplayer", "-really-quiet", "-vo", "aa:driver=curses", "/Users/Dave/Projektbsrn/30285.mp4"],
    check=True
)
