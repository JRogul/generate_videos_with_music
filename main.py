from combine import combine
from generate_audio import create_audio
from generate_video import create_video

video_prompt = input('Write a prompt for a video')
audio_prompt = input('write a prompt for audio')
video_path = create_video(video_prompt)
audio_path = create_audio(audio_prompt)
output_path = combine()
