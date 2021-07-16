import streamlit as st

st.title('Text Generator')

keyword = st.text_input('Enter a keyword')

generate = False
if keyword:       
    generate = st.button("generate suggestions")

    suggestions = []
    if generate :
        st.write("todo : call generate keywords methode")
        suggestions = ["roller","roller derby","roller derby match"]

        selection = ""
        if len(suggestions)>0:
            suggestions.insert(0,"")
            selection = st.selectbox("Suggestions: ", suggestions)
            if selection:
                st.write("you select: "+selection)
