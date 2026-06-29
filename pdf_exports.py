from fpdf import FPDF

def generate_pdf(profile, data):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="PersonaX AI Report", ln=True)

    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Name: {profile.name}", ln=True)
    pdf.cell(200, 10, txt=f"Occupation: {profile.occupation}", ln=True)
    pdf.cell(200, 10, txt=f"Education: {profile.education}", ln=True)

    pdf.multi_cell(0, 10, txt=data["snapshot"])
    pdf.multi_cell(0, 10, txt=data["quote"])

    path = "persona_report.pdf"
    pdf.output(path)

    return path