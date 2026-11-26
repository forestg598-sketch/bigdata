import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#데이터 불러오기
mpg_original = pd.read_csv('mpg.csv')
mpg = mpg_original.copy()

st.title("자동차 데이터 분석입니다.")
print(mpg['manufacturer'].unique())

st.sidebar.title('자동차 연비 데이터 분석')
st.text('1)정해진 리스트에서 검색 값을 가져오기')
st.sidebar.subheader('1)정해진 리스트에서 검색 값을 가져오기')
selected_manufacturer=\
    st.sidebar.selectbox('자동차 회사를 선택하세요',['audi','hyundai'])

#전체 칼럼 조회
result1 = \
    mpg.query('manufacturer == @selected_manufacturer')
#화면에 그리기
st.dataframe(result1)
#일부 칼럼 조회
result2 = mpg.query('manufacturer == @selected_manufacturer')\
    [['manufacturer','model','year']]
#화면에 그리기
st.dataframe(result2)

st.text('2) mpg에서 manufacturer의 unique한 값을 list로 넣기')
st.sidebar.subheader('2) mpg에서 manufacturer의 unique한 값을 list로 넣기')
selected_manufacturer2=\
    st.sidebar.selectbox('자동차 회사를 선택하세요',
                         mpg['manufacturer'].unique().tolist())
result3 = mpg.query('manufacturer == @selected_manufacturer2')
st.dataframe(result3)

st.text('3) multi select 기능')
st.sidebar.subheader('3) multi select 기능')
ms_manuf=st.sidebar.multiselect("자동차 선택(복수 선택)",
                                mpg['manufacturer'].unique().tolist())
result4 = mpg.query('manufacturer in @ms_manuf')
st.dataframe(result4)

st.text('4) chart 그리기')
st.sidebar.subheader('4) chart 그리기')

result5=mpg.groupby('manufacturer',as_index=False)\
            .agg(city_mean = ('cty','mean'))\
            .sort_values('city_mean',ascending=False)\
            .head(5)
st.dataframe(result5)
#그래프 그리기
#그래프 그릴 공간 확보
fig=plt.figure()
#바 그래프 만들기
sns.barplot(data=result5,x="manufacturer",y="city_mean")
#웹에 그래프 그리기
st.pyplot(fig)

st.text('5) selectbox로 값 입력 받고 chart 그리기')
st.sidebar.subheader('5) selectbox로 값 입력 받고 chart 그리기')
#선택 박스 종류
#1, groupby 기준
#2, agg 기준 칼럼
#3, agg 사용 함수
var1 = st.sidebar.selectbox('그룹 선택',
                            ['manufacturer','category','drv'])
var2 = st.sidebar.selectbox('연비 종류',
                            ['cty','hwy'])
var3 = st.sidebar.selectbox('사용 함수',
                            ['mean','count','min','max'])
result6 = mpg.groupby(var1,as_index=False)\
    .agg(value=(var2,var3))\
    .sort_values('value',ascending=False)\
    .head(5)
    
st.dataframe(result6)
fig1=plt.figure()
sns.barplot(data=result6,x=var1,y='value')
st.pyplot(fig1)