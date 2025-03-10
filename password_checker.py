import streamlit as st
import random as red
import string as str
import re
st.title("Analyzing your Password strength & generate password")
st.markdown("put your password to check whether your password is strong")

password = st.text_input("Enter your password ") 


def check_password_strength(password):
   feedback = []

   has_lower = bool(re.search(r"[a-z]", password))
   has_upper = bool(re.search(r"[A-Z]", password))
   has_digit = bool(re.search(r"\d", password))
   has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))


   if len(password) < 8:
      st.write("Length must be equal to 8 characters.")
   
   if not has_upper:
      feedback.append("Add at least one Upper case letter (A-Z)")

   if not has_lower:
      feedback.append("Add at least one lower case letter (a-z)")

   if not has_digit:
        feedback.append("Include at least one number (0-9).")

   if not has_special:
        feedback.append("Use at least one special character (!@#$%^&* etc.).")

   strength = "Weak"
   if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        strength = "Strong"
   elif len(password) == 8  and not ((has_upper and has_lower) or (has_digit and has_special)):
        strength = "Medium"

   return strength, feedback
        

if st.button("check-strength"):

   if password:
       strength, feedback = check_password_strength(password)
       
       st.subheader(f"password strength is: {strength}")


       if feedback:
           st.warning("suggestions to improve")

           for tip in feedback:
               st.write(tip)
               
       else:
           st.success(f"your password is {strength}")
           st.write(f"Notice: strong password must have integer, Alphabets in lowercase , uppercase and special characters")



def generate_password(length, add_digits, add_specialchar):
    characters = str.ascii_letters

    if add_digits:
        characters += str.digits
    if add_specialchar:
        characters += str.punctuation

    return "".join(red.choice(characters) for _ in range (length))

st.title("Generate password")
length = st.slider("select password length", min_value=4, max_value=60)


add_digits = st.checkbox("Include digits")
add_specialchar = st.checkbox("Include special characters")

if st.button ("Generate Password"):
    password = generate_password(length, add_digits, add_specialchar)
    st.write(f"Generated password:     {password}")