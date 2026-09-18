import sqlite3
from datetime import datetime


class DatabaseManager:

    def __init__(self):

        self.conn = sqlite3.connect(
            "database/physiovision.db"
        )

        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (

            session_id INTEGER PRIMARY KEY AUTOINCREMENT,

            patient_name TEXT NOT NULL,

            exercise TEXT NOT NULL,

            reps INTEGER NOT NULL,

            accuracy REAL NOT NULL,

            session_date TEXT NOT NULL

        )
        """)

        self.conn.commit()

    def save_session(
        self,
        patient_name,
        exercise,
        reps,
        accuracy
    ):

        self.cursor.execute("""
        INSERT INTO sessions (
            patient_name,
            exercise,
            reps,
            accuracy,
            session_date
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            patient_name,
            exercise,
            reps,
            accuracy,
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )
        ))

        self.conn.commit()

    def get_all_sessions(self):

        self.cursor.execute("""
        SELECT *
        FROM sessions
        ORDER BY session_id DESC
        """)

        return self.cursor.fetchall()

    def get_patient_sessions(
        self,
        patient_name
    ):

        self.cursor.execute("""
        SELECT *
        FROM sessions
        WHERE patient_name = ?
        ORDER BY session_id DESC
        """,
        (patient_name,)
        )

        return self.cursor.fetchall()

    def delete_all_sessions(self):

        self.cursor.execute("""
        DELETE FROM sessions
        """)

        self.conn.commit()

    def close(self):

        self.conn.close()