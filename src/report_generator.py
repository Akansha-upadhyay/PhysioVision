from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class ReportGenerator:

    @staticmethod
    def generate_report(
        patient_name,
        sessions,
        filename="report.pdf"
    ):

        pdf = SimpleDocTemplate(
            filename
        )

        styles = getSampleStyleSheet()

        content = []

        title = Paragraph(
            f"PhysioVision Report - {patient_name}",
            styles["Title"]
        )

        content.append(title)

        content.append(
            Spacer(1, 20)
        )

        for session in sessions:

            text = f"""
            Session ID: {session[0]}<br/>
            Exercise: {session[2]}<br/>
            Reps: {session[3]}<br/>
            Accuracy: {session[4]}%<br/>
            Date: {session[5]}<br/>
            """

            content.append(
                Paragraph(
                    text,
                    styles["Normal"]
                )
            )

            content.append(
                Spacer(1, 10)
            )

        pdf.build(content)

        return filename