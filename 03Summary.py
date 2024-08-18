import openai
import streamlit as st
import pandas as pd

def gptopenai(system_prompt, user_prompt) :
  type_model = "gpt-3.5-turbo"
   # 주석 단축키 Ctrl + /
  # system_prompt = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
  # user_prompt = "Compose a poem that explains the concept of recursion in programming."
  message_prompt = [
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_prompt}
    ]
  completion = openai.chat.completions.create(model=type_model, messages=message_prompt)
  getResponse = completion.choices[0].message.content
  return getResponse

def main():
  st.set_page_config(
    page_title="ChatGPT 요약 프로그램"
  )
  
  # Using "with" notation
  with st.sidebar:
   
    #st.metric(label="Temperature", value="70 °F", delta="1.2 °F")
  
    # col1, col2 = st.columns(2)
    # col1.metric("온도", "70 °", "1.2 °")
    # col2.metric("습도", "86%", "4%")
    # st.markdown('---')
    
    openai_api_key = st.text_input(label=':key: :red[OpenAI API Key]', value='', placeholder='OpenAI API 키를 입력해 주세요', type='password')
    if openai_api_key:
      openai.openai_api_key=openai_api_key
    st.markdown('---')

  # 이모티콘 : https://share.streamlit.io/streamlit/emoji-shortcodes
  
  st.header('ChatGPT *요약* :orange[프로그램] :memo:', divider='rainbow')
  st.markdown("*ChatGPT* **요약** :orange[프롬그램]은 정말 멋진 :blue-background[프로그램] 입니다. :thumbsup:")  
  
  system_prompt = st.text_area(label='시스템 프롬프트', value='''- You are an expert assistant that summarizes text into **Korean language**.
- Your task is to summarize the **text** sentences in **Korean language**.
- Your summaries should include the following :
    - Omit duplicate content, but increase the summary weight of duplicate content.
    - Summarize by emphasizing concepts and arguments rather than case evidence.
    - Summarize in 3 lines.
    - Use the format of a bullet point.''')
  # 당신은 텍스트를 **한국어**로 요약하는 전문 어시스턴트입니다.
  # - 당신의 임무는 **text** 문장을 **한국어**로 요약하는 것입니다.
  # - 요약 내용에는 다음이 포함되어야 합니다:
  # - 중복된 내용은 생략하되 중복된 내용의 요약 가중치를 늘립니다.
  # - 사례 증거보다는 개념과 주장을 강조하여 요약합니다.
  # - 세 줄로 요약합니다.
  # - 블릿 포인트 형식을 사용해서 작성합니다.
  user_prompt= st.text_area(label='요약하고자 하는 내용', placeholder='요약했으면 하는 내용을 입력해 주세요')
  
  st.divider()
  st.write(f"You wrote {len(system_prompt)+len(user_prompt)}+ characters.")
  
  if st.button("요약하기") :
    st.info(gptopenai(system_prompt, user_prompt))
  
  st.divider()

  # gpt_response = {
  #   "id": "chatcmpl-123",
  #   "object": "chat.completion",
  #   "created": 1677652288,
  #   "model": "gpt-4o-mini",
  #   "system_fingerprint": "fp_44709d6fcb",
  #   "choices": [{
  #     "index": 0,
  #     "message": {
  #       "role": "assistant",
  #       "content": "\n\nHello there, how may I assist you today?",
  #     },
  #     "logprobs": null,
  #     "finish_reason": "stop"
  #   }],
  #   "usage": {
  #     "prompt_tokens": 9,
  #     "completion_tokens": 12,
  #     "total_tokens": 21
  #   }
  # }
  # st.json(gpt_response)

  # st.divider()

  # code = '''def gptopenai(system_prompt, user_prompt) :
  # type_model = "gpt-3.5-turbo"
  # # system_prompt = "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."
  # # user_prompt = "Compose a poem that explains the concept of recursion in programming."
  # message_prompt = [
  #     {"role": "system", "content": system_prompt},
  #     {"role": "user", "content": user_prompt}
  #   ]
  # completion = openai.chat.completions.create(model=type_model, messages=message_prompt)
  # getResponse = completion.choices[0].message.content
  # return getResponse'''
  # st.code(code, language='python')

  # st.divider()


  # col_left, col_right = st.columns(2)
  # with col_left:  
  #   # https://medium.com/@nandeda.narayan/list/master-python-pandas-100-examples-with-code-8de0c6e063c6
  #   # https://www.statology.org/pandas-column-width/
    
  #   with st.container(height=300):
  #     st.write("딕셔러리에서 데이터 읽어 오기")
  #     data = {'이름': ['홍길동', '김영희', '박철수'],
  #           '나이': [25, 30, 35],
  #           '도시': ['서울시', '경기도', '충청도']}
  #     df = pd.DataFrame(data)
  #     st.dataframe(df)
 
  #   with st.container(height=300):
  #     st.write("데이터 읽기오기 - 특정 항목")
  #     selected_columns = df[['이름', '도시']]
  #     st.dataframe(selected_columns)
    
  #   with st.container(height=300):   
  #     st.write("데이터 읽기오기 - 특정 항목 연산")
  #     df['만나이'] = df['나이'].apply(lambda x: x-1)
  #     st.dataframe(df) 
  
  # with col_right :
  #   with st.container(height=300):
  #     st.write("CSV 파일에서 데이터 읽어 오기") 
  #     df = pd.read_csv('pandas_example01.csv')
  #     st.dataframe(df)
  
  #   with st.container(height=300):
  #     st.write("데이터 읽기오기 - 특정 항목 조건")
  #     filtered_df = df[df['나이'] > 30]
  #     st.dataframe(filtered_df)
   
  #   with st.container(height=300):
  #     st.write("데이터 읽기오기 - 특정 항목 평균")
  #     grouped_df = df.groupby('성별')['나이'].mean()
  #     st.dataframe(grouped_df)

if __name__ == "__main__":
 main()