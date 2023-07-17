# generate_videos_with_music
This project involves two key processes. 
Firstly, video is generated using the model available at [link](https://huggingface.co/cerspense/zeroscope_v2_576w). Secondly, audio is generated using the model from [lnk](https://github.com/facebookresearch/audiocraft/tree/main). 
These two components are then combined to produce a final output of video with synchronized audio.

https://github.com/JRogulski/generate_videos_with_music/assets/106926091/316bab4b-c368-4554-a4f2-db390aec30e4

How to run this project
```shell
python -m venv venv
venv\Scripts\activate //inside project directory
pip install -r requirements.txt
python main.py
```
