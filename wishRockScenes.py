import tkinter as tk
from tkinter import PhotoImage, Entry, Tk, Canvas, Text, Button, font
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from pathlib import Path
import os

# ElevenLabs 클라이언트 초기화
client = ElevenLabs(api_key="sk_23aefcd8dffc6d2b6f063c88ad331a67a0035ac565e67844")

# 음성을 생성하고 재생하는 함수
def generate_voice(text):
    if text.strip():
        audio = client.generate(
            text=text,
            voice="Kp8K3ZlvqyVzkQBQ2IXJ",  # Jinie 목소리
            model="eleven_multilingual_v2"
        )
        play(audio)

# Tkinter 윈도우 설정
window = tk.Tk()
window.title("WishRock")
window.geometry("1280x720")
window.minsize(640, 360)  # 최소 크기 설정
window.configure(bg="#FFFFFF")

# 기본 변수들 설정
scene_num = 1
input_text = ""
scenes = [f"scene_{i}.png" for i in range(1, 18)]  # 장면 파일 리스트

# 캔버스 설정
canvas = tk.Canvas(window, bg="#FFFFFF", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
canvas.pack(fill="both", expand=True)

# 이미지 로드 함수
def load_scene(scene_name):
    image_path = f"C:/Users/yesju/OneDrive/바탕 화면/wishU/{scene_name}"
    try:
        image = PhotoImage(file=image_path)
        canvas.create_image(0, 0, anchor="nw", image=image)
        canvas.image = image  # 이미지 참조 유지
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")

# 장면 전환 함수
def next_scene(event=None):
    global scene_num
    if scene_num < 17:
        scene_num += 1
        if scene_num == 9:
            load_scene("scene_9.png")
            create_text_input(scene_num)  # scene 9에서 텍스트 입력 필드 생성
        elif scene_num == 17:
            load_scene("scene_17.png")
            create_text_input(scene_num)  # scene 17에서 텍스트 입력 필드 생성
        else:
            load_scene(f"scene_{scene_num}.png")
    elif scene_num == 17:
        play_voice()  # 마지막 장면에서 음성 출력

# 첫 장면 로드
load_scene(scenes[0])

# 클릭 시 다음 장면으로 이동
window.bind("<Button-1>", next_scene)

# 메인 루프 실행
window.mainloop()