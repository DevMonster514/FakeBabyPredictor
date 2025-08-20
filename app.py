import streamlit as st
from datetime import date
def predict_child_gender(mother_dob, baby_dob):
   mother_birth = date(*mother_dob)
   baby_birth = date(*baby_dob)
   # Calculate age
   age = baby_birth.year - mother_birth.year
   if (baby_birth.month, baby_birth.day) < (mother_birth.month, mother_birth.day):
       age -= 1
   # Odd-even rule
   return "Girl" if age % 2 == 0 else "Boy"
st.set_page_config(
    page_title="Lemme Guess Your Gender 👶",  # Browser tab title
    page_icon="🔮",                           # Favicon (here a crystal ball emoji)
    layout="centered"
)
st.title("Guess Your Gender")
mother_dob = st.date_input("Mother's Date of Birth",min_value=date(1800,1,1),max_value="today")
baby_dob = st.date_input("Your Date of Birth",min_value=date(1800,1,1),max_value=date(2030,1,1))
if st.button("Predict"):
   result = predict_child_gender(
       (mother_dob.year, mother_dob.month, mother_dob.day),
       (baby_dob.year, baby_dob.month, baby_dob.day)
   )
   # Change background color
   if result == "Boy":
       st.markdown(
           """
<style>
           .stApp {background-color: #89CFF0;}
</style>
           """,
           unsafe_allow_html=True
       )
   else:
       st.markdown(
           """
<style>
           .stApp {background-color: #FFB6C1;}
</style>
           """,
           unsafe_allow_html=True
       )
   st.success(f"Prediction: {result} 👶")

st.markdown(
   """
<hr>
<p style="text-align:center; color:gray;">
   Prediction by Aj Baba
</p>
   """,
   unsafe_allow_html=True
)
