from moviepy.editor import VideoFileClip, AudioFileClip

def combine(video_path = 'outputs//video.mp4', audio_path = 'outputs//audio.wav', output_path = 'final_video.mp4'):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    video = video.set_audio(audio)
    video.write_videofile(output_path)
    return output_path