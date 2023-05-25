import streamlit as st
import openai

openai.api_key = st.secrets["api_key"]

st.title("ChatGPT recommend Color by Manse Jang")

with st.form("form"):
    user_input = st.text_input("Prompt")
    submit = st.form_submit_button("Submit")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "The assistant's job is to recommend color codes that match what user's describing.",
    }]


    gpt_prompt.append({
        "role": "user",
        "content": user_input + ' hex color'
    })

    with st.spinner("Waiting for chatGPT..."):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    #st.write(prompt)
    for line in prompt.split(' '):
        if '#' in line:
            #st.write(line[:7])
            color = line[:7]
            st.markdown(f'<h1 style="color:{color};font-size:24px;">{color}</h1>', unsafe_allow_html=True)
        else :
            continue
    if '#' not in prompt:
        st.write('GPT does not have a color recommendation, Please enter another prompt.')
