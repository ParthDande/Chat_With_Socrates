import streamlit as st
from PIL import Image
import openai

# Set up the OpenAI API key
openai.api_key = "Enter Your API KEY"

# Define the Socrates image
socrates_image = Image.open("socrates.jpg")

# Streamlit app
st.set_page_config(page_title="Socrates Speaks")
st.image(socrates_image,caption='Socrates',width=400)
st.title("Socrates Speaks")
st.write("""
    Talk with Socrates Himself!! Ask the great Greek philosopher a question,
    and he will share his wisdom with you.
""")

# User input
user_question = st.text_area("Your question:", height=100)

if st.button("Ask Socrates"):
    # Generate the response using the OpenAI API
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Socrates, the great Greek philosopher. You have been transported to the present day to share your wisdom and insights with the people of this technological age."},
            {"role": "user", "content": user_question}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    socrates_response = response.choices[0].message.content 
    cartoon_socrates_image = 'cartoon_socrates.png'
    # Display the Socrates image and response
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(cartoon_socrates_image, caption="Socrates", width=200)
    with col2:
        st.markdown(f"<div class='speech-bubble'><p><strong>Socrates says:</strong> {socrates_response}</p></div>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .speech-bubble {
        position: relative;
        background: #fff;
        border-radius: 0.4em;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    .speech-bubble:after {
        content: '';
        position: absolute;
        top: 0;
        left: 100%;
        width: 0;
        height: 0;
        border: 10px solid transparent;
        border-right-color: #fff;
        border-left: 0;
        border-top: 0;
        margin-top: -5px;
        margin-left: -10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)