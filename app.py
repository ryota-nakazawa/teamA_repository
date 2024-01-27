import streamlit as st
import base64
from PIL import Image
import speech_recognition as sr
from chatgpt_speaking import vv_call

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        st.text("🎙️Say something:")
        recognizer.adjust_for_ambient_noise(source)  # マイクのノイズ対策
        audio = recognizer.listen(source, timeout=5)  # 最大で5秒間音声を収集

    try:
        text = recognizer.recognize_google(audio, language="ja-JP")
        st.image(image_me, width=50)
        st.text("You said: " + text)
        vv_call(text)
    except sr.UnknownValueError:
        st.text("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        st.text("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    st.title("Speech Recognition with Streamlit")
  
    # 動画のファイルパス
    # video_path = './movie/output1_video.mp4'

    image_ai = Image.open("./movie/testimage1.png")

    image_me = Image.open("./movie/image_me.jpg")

    # Streamlitで動画を表示
    # st.video(video_path)
    
    st.image(image_ai, caption="AI アイドル", width=200)

    if st.button("Start Recording"):
        recognize_speech()
