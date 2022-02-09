FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt
RUN apt update && apt install -y python3-pip
RUN apt install ffmpeg

CMD ["python3", "main.py"]