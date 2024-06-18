import whisperx
import json
import torch
import torchaudio

device = "cpu" 
audio_file = "file.mp3"
batch_size = 16 # reduce if low on GPU mem
compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)

model_a, metadata = whisperx.load_align_model(language_code="en", device="cpu")

pipeline_type = "torchaudio"
bundle = torchaudio.pipelines.__dict__["VOXPOPULI_ASR_BASE_10K_IT"]
align_model = bundle.get_model().to(device)
labels = bundle.get_labels()
torch.save(align_model, "alignmodels/fullalignmodel_it.pt")


# File path to save JSON data
file_path = "alignmodels/metadata_it.json"

# Writing dictionary to JSON file
with open(file_path, 'w') as json_file:
    json.dump(metadata, json_file)


#result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)