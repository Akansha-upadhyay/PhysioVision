import streamlit as st
import sys
import os

# Add project root to Python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.database_manager import DatabaseManager

db = DatabaseManager()

st.title("🏥 Patient Registration")

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=20
)

condition = st.text_input(
    "Medical Condition"
)

if st.button("Register Patient"):

    if name.strip() == "":
        st.error("Please enter patient name")

    else:
        db.add_patient(
            name,
            age,
            condition
        )

        st.success(
            f"{name} registered successfully!"
        )