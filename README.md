# wishRockFor2ndCritic
2차 심사 제출 작품

from tkinter import Tk, Canvas, Text, Button, PhotoImage, font
from elevenlabs import play
from pydantic import BaseModel, ConfigDict
from elevenlabs.client import ElevenLabs
from pathlib import Path

# 경고 해결을 위한 pydantic 설정
class SpeechHistoryItemResponse(BaseModel):
    model_id: str
    model_config = ConfigDict(protected_namespaces=())

class Model(BaseModel):
    model_id: str
    model_config = ConfigDict(protected_namespaces=())

# 경로 설정
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\yesju\OneDrive\바탕 화면\wishU")

# Initialize ElevenLabs client
client = ElevenLabs(
    api_key="sk_c4e012b0f5bca4111c1ee2fb1db327a581e2a3475150f5ee",  # Defaults to ELEVEN_API_KEY
)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# 목소리 생성 함수
def generate_voice():
    text = entry_1.get("1.0", "end-1c")  # 입력된 텍스트 가져오기
    if text.strip():  # 공백이 아닌 경우에만 실행
        audio = client.generate(
            text=text,
            voice="Kp8K3ZlvqyVzkQBQ2IXJ",  # 원하는 목소리 ID 입력 (나 Jinie)
            model="eleven_multilingual_v2"
        )
        play(audio)  # 생성된 오디오 재생

# 창 설정
window = Tk()
window.geometry("1280x720")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=720,
    width=1280,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# 배경 이미지 추가
image_image_1 = PhotoImage(
    file=relative_to_assets("sc17_Back.png"))
canvas.create_image(
    640.0,
    360.0,
    image=image_image_1
)

# 텍스트 입력 안내
canvas.create_text(
    448.0,
    666.0,
    anchor="nw",
    text="               제가 들려드릴게요. 직접 적어보세요.",
    fill="#000000",
    font=("RobotoRoman SemiBold", 14 * -1)
)

# 버튼 생성 (목소리 생성 버튼)
generate_button_image = PhotoImage(
    file=relative_to_assets("sc17_Button.png"))
generate_button = Button(
    image=generate_button_image,
    borderwidth=0,
    highlightthickness=0,
    command=generate_voice,
    relief="flat"
)
generate_button.place(
    x=189.0,
    y=400.0,
    width=875.0,
    height=84.0
)

# 텍스트 입력 박스 추가
entry_image_1 = PhotoImage(
    file=relative_to_assets("sc17_TextArea.png"))
entry_bg_1 = canvas.create_image(
    640.0,
    360.0,
    image=entry_image_1
)

# 입력 필드
entry_1 = Text(
    bd=0,
    bg="#E5D9CD",  # 투명하게 만들고 싶다면 배경을 이미지처럼 설정 가능
    fg="#000000",
    highlightthickness=0
)
entry_1.place(
    x=189.0,
    y=316.0,
    width=875.0,
    height=84.0
)

# 창 크기 고정
window.resizable(False, False)
window.mainloop()



# SCENE

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
