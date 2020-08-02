import moviepy.editor as mp

clip=mp.VideoFileClip(r"D:\automation\My.mp4")

clip.audio.write_audiofile(r"D:\DATA\media\music\check.mp3")