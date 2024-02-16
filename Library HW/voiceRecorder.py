import sounddevice as sd
import soundfile as sf

filename = "recorded_audio.wav"
duration = 5


print("Recording...")
audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
sd.wait()


sf.write(filename, audio_data, 44100)

print(f"Audio recorded and saved to {filename}")
