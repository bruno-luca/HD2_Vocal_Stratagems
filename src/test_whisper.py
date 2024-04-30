import pyaudio
import wave
from faster_whisper import WhisperModel, decode_audio

def record_chunk(p, stream, chunk_file):
    frames = []
    for _ in range(0, int(16000 / 1024 * 2)):
        data = stream.read(1024)
        frames.append(data)

    wf = wave.open(chunk_file, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(16000)
    wf.writeframes(b''.join(frames))
    wf.close()

def transcript_chunk(model, chunk_file):
    audio = decode_audio(chunk_file)
    return model.transcribe(audio)

def main():
    model_size = "small"
    model = WhisperModel(model_size)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)

    while True:
        chunk_file = "tmp.wav"
        record_chunk(p, stream, chunk_file)
        transcription = transcript_chunk(model, chunk_file)
        print(transcription)

if __name__ == '__main__':
    main()