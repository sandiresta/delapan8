import streamlit as st

st.title("About Our Group")
st.write("Meet the amazing members of our group!")

group_members = [
    {"Name": "Ruddi Sutomi", "Role": "FMU Leader", "Email": "ruddi.sutomi@michelin.com", "Image": r"C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\WhatsApp Image 2024-12-13 at 21.05.38_b1b3ada7.jpg"},
    {"Name": "Sandi Resta", "Role": "DM ZP Leader", "Email": "sandi.resta@michelin.com", "Image": r"C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\20220822_211922.jpg"},
    {"Name": "Raden Asep Ahmad Fadillah", "Role": "2W BU Leader", "Email": "raden.fadillah@michelin.com", "Image": r"C:\Users\LENOVO\Documents\ImageProcessingApp - Group 8 - Add Logo and Photo\assets\WhatsApp Image 2024-12-13 at 21.06.02_107ccee3.jpg"},
]

for member in group_members:
    st.subheader(member["Name"])
    st.image(member["Image"], caption=f"{member['Name']} - {member['Role']}", width=150)
    st.write(f"**Role:** {member['Role']}")
    st.write(f"**Email:** {member['Email']}")
    st.write("---")

