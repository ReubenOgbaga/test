import streamlit as st

#
# #  Displaying texts
# st.title('Welcome to my app')
# st.header('This the header')
# st.subheader('`This is the` *subheader*')
# st.text('Standard text document')
# st.markdown('**Bold text**')
# st.markdown('*Italicized text*')
#
#
# st.markdown("<h1 style='text-align: center;'>""Main </h1>", unsafe_allow_html=True)


#  Dataframes
# df= {'Customers': ['Emeka', 'Reuben', 'Prince', 'Rachel']}
#
# st.dataframe(df)
# st.table(df)

# Adding Interactive Widget
st.button('Analyze your data')
st.slider('Select a category',  0, 10)

st.selectbox('Select a category', ['Emeka', 'Reuben', 'Prince', 'Rachel'])
if st.checkbox('Click to show data'):
    st.selectbox('Select category', 'Emeka')
st.radio('Select a category', ['Chris', 'Chuck', 'Blessing', 'Emeka'])
st.radio('Select a category', ['Option 1', 'Option 2'])
st.select_slider('Select from a slider', 1, ['Chuck', 40])



color = ['Joe', 'Trump','Kampala', 'Mr musk']