import torch
from audiocraft.models import musicgen
from audiocraft.data.audio import audio_write

def create_audio(prompt, output_path='outputs//audio'):
    model = musicgen.MusicGen.get_pretrained('medium', device='cuda')
    model.set_generation_params(duration=6)

    audio_output = model.generate([prompt])
    audio_output = audio_output.squeeze(0)

    audio_write(output_path, audio_output.cpu(), 
                model.sample_rate, strategy="loudness")
    return output_path