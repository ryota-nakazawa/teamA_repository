import openai
from voicevox_speaking import Voicevox
from PIL import Image
import streamlit as st

# openai.api_key = 'Your API key'
# もしくはexport OPENAI_API_KEY="Your secret key"で一時的にターミナルに保存して実行可能

def speak_voicevox(text):
    vv = Voicevox()
    vv.speak(text = text)
  
def vv_call(input_prompt):
    input_to_chatgpt = input_prompt
    image_ai = Image.open("./movie/testimage1.png")
    
    messages = [
        {"role": "user", "content": input_to_chatgpt}
    ]
    
    res = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages,
        max_tokens = 70
    )
    
    response_chatgpt = res['choices'][0]['message']['content']
    print(response_chatgpt)
    st.image(image_ai, width=50)
    st.text("AI said: " + response_chatgpt)
    speak_voicevox(response_chatgpt)
    
    return response_chatgpt


# if __name__ == "__main__":
#     user_input = input('入力: ')
#     vv_call(input_prompt = user_input)
