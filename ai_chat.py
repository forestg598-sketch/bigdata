import streamlit as st
from openai import OpenAI
import os

api_key=os.environ["OPENAI_API_KEY"]
print(api_key)

#streamlit run ai_chat.py
#python -m streamlit run ai_chat.py

st.title("Streamlit 생성형 AI 예제")

client = OpenAI()

#대화 기록 초기화(세션 공간 활용)
if "messages" not in st.session_state:
    st.session_state.messages =[]
    
#기존 대화 출력
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
    
#사용자 입력
prompt=st.chat_input("질문을 입력하세요.")

if prompt:
    # 사용자 질문 화면 출력
    with st.chat_message("user"):
        st.write(prompt)

    #대화 내용 저장
    st.session_state.messages.append({"role":"user","content": prompt})

    #OpenAi에 요청 전달(전체 대화 내용)
    response=client.responses.create(
        model="gpt-5.6-luna",
        input=st.session_state.messages
    )

    #응답 추출
    answer=response.output_text

    #AI 응답화면 출력
    with st.chat_messages("assistant"):
        st.write(answer)
        
        st.write(f"입력 비용: "
                f"${response.usage.input_tokens * 0.20 /1_000_000:6.f}")
        st.write(f"출력 비용: "
                f"${response.usage.output_tokens * 1.20 / 1_000_000:6.f}")
    
if st.button("대화 초기화"):
    st.session_state.messages=[]
    st.rerun()