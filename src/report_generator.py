
from fpdf import FPDF

def generate_pdf(summary, output_pdf):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Summary Report", ln=True, align='C')

    for col in summary.columns:
        pdf.cell(200, 10, txt=f"{col}: {summary[col].to_dict()}", ln=True)

    pdf.output(output_pdf)
