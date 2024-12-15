import streamlit as st

st.title("About Our Group")
st.write("Meet the amazing members of our group!")

group_members = [
    {"Name": "Ruddi Sutomi", "Role": "FMU Leader", "Email": "ruddi.sutomi@michelin.com", "Image": r"assets/ruddi_sutomi.jpg"},
    {"Name": "Sandi Resta", "Role": "DM ZP Leader", "Email": "sandi.resta@michelin.com", "Image": r"assets/sandi_resta.jpg"},
    {"Name": "Raden Asep Ahmad Fadillah", "Role": "2W BU Leader", "Email": "raden.fadillah@michelin.com", "Image": r"assets/raden_asep.jpg"},
]

for member in group_members:
    st.subheader(member["Name"])
    st.image(member["Image"], caption=f"{member['Name']} - {member['Role']}", width=150)
    st.write(f"**Role:** {member['Role']}")
    st.write(f"**Email:** {member['Email']}")
    st.write("---")

