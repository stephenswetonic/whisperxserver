import time

import json
import boto3
import os

if not os.path.exists("/tmp/cache/"):
    os.makedirs("/tmp/cache/", mode=0o755)
os.environ['TRANSFORMERS_CACHE'] = '/tmp/cache/'

import whisperx
from torch import load

s3 = boto3.client('s3')

print("before handler")

def handler(event, context):
    print("in handler")
    device = "cpu" 
    batch_size = 16 # reduce if low on GPU mem
    compute_type = "int8" # change to "int8" if low on GPU mem (may reduce accuracy)

    bucket = "sam-app-s3uploadbucket-qkgqfgtltuzq"

    # sessionKey = str(event['sessionKey'])
    # isVideo = event['isVideo']
    # lang = event['lang']

    # # Create temp file path
    # tempSourcePath = ''
    # if isVideo:
    #     tempSourcePath = '/tmp/' + sessionKey + '.mp4'
    # else:
    #     tempSourcePath = '/tmp/' + sessionKey + '.wav'
        
    # # Download from S3
    # try:
    #     download_file_from_s3(bucket, sessionKey, tempSourcePath)
    # except Exception as e:
    #     print(f"Error occurred while downloading source.. {e}")
    
    # print("loaded source")

    try: 
        # print("loading model...")
        # model = whisperx.load_model(whisper_arch="faster-whisper-tiny/", device=device, compute_type=compute_type)

        # audio = whisperx.load_audio(tempSourcePath)
        # result = model.transcribe(audio, batch_size=batch_size)

        # # Will need to match these models to lang later
        # pretrained_model_path = 'alignmodels/fullalignmodel_en.pt'
        # align_model = load(pretrained_model_path)

        # metadata = open("alignmodels/metadata_en.json", "r")
        # metadata = json.load(metadata)

        # #model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)

        # segments = whisperx.align(result["segments"], align_model, metadata, audio, device, return_char_alignments=False)
        # wordsJson = []
        # counter = 0
        # for segment in segments:
        #     for word in segment.words:
        #         wordsJson.append({"id": str(counter), "start": word.start, "end": word.end, "word": word.word.strip()})
        #         counter += 1
        # print(wordsJson)

        return {
            'statusCode': 200,
            'body': json.dumps({"message": "Audio is processing"})
        }
    
    except Exception as e:
        print("Error processing or saving...")
        print(e)
        return {
            'statusCode': 500,
            'error': str(e)
        }

def download_file_from_s3(bucket_name, object_key, local_file_path):
    # Download the file from S3
    s3.download_file(bucket_name, object_key, local_file_path)
