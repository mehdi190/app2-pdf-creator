from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='L', format='A4', unit='mm')
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # --- Header ---
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
    pdf.line(10, 22, 287, 22)  # 287 mm wide for A4 landscape

    # --- Footer for first page ---
    pdf.set_y(-10)  # 10 mm from bottom
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    # --- Add extra pages ---
    for i in range(row["Pages"] - 1):
        pdf.add_page()

        pdf.set_y(-10)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
