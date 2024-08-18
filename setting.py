# 화면 크기, fps, 이미지 경로 등 설정 값 저장 
import os

screen_width = 800
screen_height = 600
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, "image")
map_length = 10000