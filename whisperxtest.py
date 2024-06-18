import time
import whisperx


device = "cpu" 
audio_file = "file.mp3"
batch_size = 16 # reduce if low on GPU mem
compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)


model = whisperx.load_model(whisper_arch="faster-whisper-tiny", device=device, compute_type=compute_type)

# save model to local path (optional)
# model_dir = "/path/"
# model = whisperx.load_model("large-v2", device, compute_type=compute_type, download_root=model_dir)

audio = whisperx.load_audio(audio_file)
result = model.transcribe(audio, batch_size=batch_size)
print(result["segments"]) # before alignment

# 2. Align whisper output
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device, model_name="alignmodels/wav2vec2_en.pth")
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)

print(result["segments"]) # after alignment


