import os
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate

openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    st.error('OpenAI key is empty, please add')

from langchain_openai import ChatOpenAI

# Instantiation

llm = ChatOpenAI(
    model='gpt-4o',
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

prompt = ChatPromptTemplate([
    (
        'system',
        'You are such a wonderful assistant that translates from{input_language} to {output_language}'
    ),
    ('human', '{input}')
]
)
chain = prompt | llm


# Streamlit UI
def main():
    st.title('🌎Language Translator App')
    st.write('Translates from one language to another')
    input_language = st.text_input('Enter language: ')
    output_language = st.text_input('Enter output language: ')
    input_text = st.text_area('Enter the message you want to translate: ')

#  Translate Button
    if st.button('Translate'):
        if not output_language or input_language or input_text:
            st.warning('Please fill all required inputs')
        else:
            with st.spinner('Translating...'):
                try:
                    result = chain.invoke(
                        {
                            'input_language': input_language,
                            'output_language': output_language,
                            'input': input_text,
                        }
                    )
                    st.success('Translation complete!')
                    st.text_area(f'Translation ({output_language}):',
                                 value=result.content, height=200)
                except Exception as e:
                    st.error(f'An error occurred: {e}')

    st.write('Made with 💡 by Reuben Chiadikaobi Ogbaga')

if __name__ == '__main__':
    main()






