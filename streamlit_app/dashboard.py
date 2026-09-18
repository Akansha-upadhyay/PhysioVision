import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(
    page_title="PhysioVision Dashboard",
    layout="wide"
)

st.title("🏥 PhysioVision Physiotherapy Dashboard")

# Database Connection
conn = sqlite3.connect(
    "database/physiovision.db"
)

query = """
SELECT *
FROM sessions
"""

df = pd.read_sql_query(
    query,
    conn
)

conn.close()

if df.empty:

    st.warning(
        "No session data available."
    )

else:

    # KPIs
    total_sessions = len(df)

    total_reps = df["reps"].sum()

    avg_accuracy = round(
        df["accuracy"].mean(),
        2
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Sessions",
            total_sessions
        )

    with col2:
        st.metric(
            "Total Repetitions",
            total_reps
        )

    with col3:
        st.metric(
            "Average Accuracy",
            f"{avg_accuracy}%"
        )

    st.divider()

    # Exercise Distribution
    st.subheader(
        "📊 Exercise Distribution"
    )

    exercise_counts = (
        df["exercise"]
        .value_counts()
    )

    st.bar_chart(
        exercise_counts
    )

    st.divider()

    # Patient Filter
    st.subheader(
        "🔍 Filters"
    )

    patient_list = [
        "All"
    ] + sorted(
        df["patient_name"]
        .unique()
        .tolist()
    )

    exercise_list = [
        "All"
    ] + sorted(
        df["exercise"]
        .unique()
        .tolist()
    )

    col1, col2 = st.columns(2)

    with col1:
        selected_patient = st.selectbox(
            "Patient",
            patient_list
        )

    with col2:
        selected_exercise = st.selectbox(
            "Exercise",
            exercise_list
        )

    filtered_df = df.copy()

    if selected_patient != "All":
        filtered_df = filtered_df[
            filtered_df["patient_name"]
            == selected_patient
        ]

    if selected_exercise != "All":
        filtered_df = filtered_df[
            filtered_df["exercise"]
            == selected_exercise
        ]

    st.divider()

    # Session Table
    st.subheader(
        "📋 Session History"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    st.divider()

    # Repetition Trend
    st.subheader(
        "📈 Repetition Trend"
    )

    st.line_chart(
        filtered_df["reps"]
    )

    st.divider()

    # Accuracy Trend
    st.subheader(
        "🎯 Accuracy Trend"
    )

    st.line_chart(
        filtered_df["accuracy"]
    )

    st.divider()

    # Top Performer
    st.subheader(
        "🏆 Best Session"
    )

    best_session = filtered_df.loc[
        filtered_df["accuracy"].idxmax()
    ]

    st.success(
        f"""
        Patient: {best_session['patient_name']}

        Exercise: {best_session['exercise']}

        Accuracy: {best_session['accuracy']}%

        Reps: {best_session['reps']}
        """
    )