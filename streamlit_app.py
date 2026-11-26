#터미널에서 'conda list' 설치된 패키지 리스트를 확인 가능
#만약 streamlit 패키지가 없다면
#pip install streamlit 설치 진행하기

import streamlit as st
from datetime import date,time

st.title("13주차 streamlit 예제")

st.title("제목")
st.text('일반 텍스트')
st.write("일반 텍스트")
st.caption('작은 글씨,설명용')
st.header("header")
st.subheader("subheader")
st.markdown("## markdown 헤더")
st.text_area('여러 줄 입력 칸')

st.title('message box 예제')
st.success('성공')
st.warning('경고')
st.info('정보')
st.error('에러')



st.title('input 예제')
name=st.text_input("이름을 입력해주세요")
if name != "":
    st.write(f"안녕하세요, {name}님!")
    st.subheader(name+"님 환영합니다~")

bio = st.text_area('자기소개를 작성해주세요.')
age=st.number_input('나이를 입력하세요.',min_value=0,max_value=150,value=50, step=1)
password = st.text_input('비밀번호를 입력하세요', type="password")
birth_date=st.date_input('생년월일 선택',date.today())
birth_time=st.time_input('시간 선택',value=time(hour=12,minute=0))

if st.button('회원가입'):
    st.write(f"이름 : {name}")
    st.write(f"자기소개: {bio}")
    st.write(f"나이 : {age}")
    st.write(f"비밀번호 : {'*' * len(password)}")
    st.write(f"생년월일 : {birth_date}")
    st.write(f"탄생시간 : {birth_time}")
    
st.title("image 예제")
st.image('puppy.jpg',caption='강아지입니다.')
st.image("https://www.korea.kr/goNewsRes/attaches/innods/images/000300/_OO_4507-11.jpg")

st.title("video 예제")
st.video("https://www.youtube.com/watch?v=uim6xB61G14&list=RDuim6xB61G14&start_radio=1")

st.title("tab 예제")
tabA, tabB, tabC = st.tabs(['탭 A', '탭 B','탭 C'])

with tabA:
    st.header("탭 A")
    st.write("탭 A입니다.")
    st.image('puppy.jpg', caption="탭 A 이미지")
    
with tabB:
    st.header("탭 B")
    st.write("탭 B입니다.")
    st.image('fox.jpg', caption="탭 B 이미지")
      
with tabC:
    st.header("탭 C")
    st.write("탭 C입니다.")
    st.image('https://www.korea.kr/goNewsRes/attaches/innods/images/000300/_OO_4507-11.jpg', caption="탭 C 이미지")
    
    
    
    
st.title("column 예제")
#컬럼 생성
col1, col2 = st.columns([2,5])
#컬럼 내용 추가
with col1:
    st.title('col1 입니다')
    st.header("header col1")
    st.subheader("sub col1")
    st.image('puppy.jpg')
    
with col2:
    st.title('col2 입니다')
    st.header("header col2")
    st.subheader("sub col2")
    st.image('fox.jpg')
col1.title('밖에서 쓰기')
col2.title("밖에서 쓰기")

