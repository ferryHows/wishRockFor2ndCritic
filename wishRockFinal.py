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

# 텍스트 입력 처리 함수 (scene 9)
def handle_input(event=None):
    global input_text, scene_num
    input_text = text_area.get()
    text_area.delete(0, 'end')  # 입력창 초기화
    next_scene()  # 다음 장면으로 전환

# scene 17에서 음성 출력 함수
def play_voice(event=None):
    global input_text
    if input_text.strip():
        generate_voice(input_text)

# 텍스트 입력 필드 추가 (scene 9, scene 17에서만 사용)
def create_text_input(scene_num):
    global text_area
    if scene_num == 9:
        input_image = PhotoImage(file=f"C:/Users/yesju/OneDrive/바탕 화면/wishU/scene_9_Text_Input.png")  # scene 9용 텍스트 입력 배경
        canvas.create_image(300, 600, anchor="nw", image=input_image)  # 배경 이미지 추가
        canvas.input_image = input_image  # 이미지가 유지되도록 참조 유지
    elif scene_num == 17:
        input_image = PhotoImage(file=f"C:/Users/yesju/OneDrive/바탕 화면/wishU/scene_17_Text_Input.png")  # scene 17용 텍스트 입력 배경
        canvas.create_image(300, 600, anchor="nw", image=input_image)  # 배경 이미지 추가
        canvas.input_image = input_image  # 이미지가 유지되도록 참조 유지

    text_area = Entry(window, font=("Arial", 14), bd=0, highlightthickness=0, bg="#FFFFFF")
    text_area.place(x=300, y=600, width=600, height=50)
    if scene_num == 9:
        text_area.bind("<Return>", handle_input)  # scene 9에서 엔터 키 입력 시 다음 장면으로 전환
    elif scene_num == 17:
        text_area.bind("<Return>", play_voice)  # scene 17에서 엔터 키 입력 시 음성 출력

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