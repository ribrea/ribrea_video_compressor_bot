### Video Compression

##### using ffmpeg as a library 

### Build and Deploy
#### 0. Go to [Bot Father](https://t.me/botfather) and add it to `main.py` 
````python
"""
Add your Token
"""
Token: str = "<Token>"
````

#### 1. Install Docker on your machine
#### 2. Build the Docker image
````bash
docker build -t video-compression .
````
#### 3. Run the Docker image
````bash
docker run video-compression
````


