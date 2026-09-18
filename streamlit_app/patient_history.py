import streamlit as st
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from src.database_manager import DatabaseManager
from src.report_generator import ReportGenerator

st.title(
    "📋 Patient History"
)

db = DatabaseManager()

patient_name = st.text_input(
    "Enter Patient Name"
)

if st.button(
    "Load History"
):

    sessions = db.get_patient_sessions(
        patient_name
    )

    if len(sessions) == 0:

        st.warning(
            "No sessions found"
        )

    else:

        st.success(
            f"{len(sessions)} sessions found"
        )

        st.write(sessions)

        if st.button(
            "Generate PDF Report"
        ):

            filename = ReportGenerator.generate_report(
                patient_name,
                sessions
            )

            with open(
                filename,
                "rb"
            ) as file:

                st.download_button(
                    label="Download Report",
                    data=file,
                    file_name=filename,
                    mime="application/pdf"
                )