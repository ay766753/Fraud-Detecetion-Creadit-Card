import streamlit as st
st.title('Hello')

st.header('This Header')
st.subheader('write now anything')
st.markdown('### This is a Markdown')
#checkbox
if st.checkbox('show/hide'):
    st.text('showing the widge')

#radion button
# create a radion button to select gender
status = st.radio('Select Gender:',['Male', 'Female'])

#display the selected option using success message
if status == 'Male':
    st.success('Male')
else:
    st.success('Female')

#selection box
hobby = st.selectbox('Select your hobby:',['Dancing', 'Sports', 'Reading'])

#display the selected hobbys
st.write('Your hobby is:', hobby)

#multi -selection
#create  a multi select box for box for choosing hobbies
hobbies = st.multiselect('select your hobbies:', ['dancing', 'reading', 'sports'])


#display the number of selected hobbies
st.write('you selected',len(hobbies),'hobbies')


#button
st.button("click")

if st.button("About"):
    st.text("Welcome to streamlit")


#Text Input
name= st.text_input("Enter your name:")


if st.button("Submit"):
    result=name.title()
    st.success(result)



# slider
level =st.slider("Choose a level",min_value=1,max_value=5)

st.write(f"selected level:{level}")