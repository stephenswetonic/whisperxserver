docker build --platform linux/amd64 -t ytpaiwhisperx .

docker tag ytpaiwhisperx:latest 097603745328.dkr.ecr.us-east-1.amazonaws.com/ytpaiwhisperx:latest

docker push 097603745328.dkr.ecr.us-east-1.amazonaws.com/ytpaiwhisperx:latest

aws lambda update-function-code --function-name ytpaiwhisperx --image-uri 097603745328.dkr.ecr.us-east-1.amazonaws.com/ytpaiwhisperx:latest --no-cli-pager
