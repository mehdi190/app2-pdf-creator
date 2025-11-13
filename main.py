from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='L', format='A4', unit='mm')
pdf.set_auto_page_break(False, margin=0)

df = pd.read_csv("topics.csv")

# A4 landscape dimensions
PAGE_WIDTH = 297
PAGE_HEIGHT = 210

for index, row in df.iterrows():
    for page in range(row["Pages"]):
        pdf.add_page()

        # --- Header on first page only ---
        if page == 0:
            pdf.set_font("Times", "B", 24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)
            pdf.line(10, 22, PAGE_WIDTH - 10, 22)

        # --- Draw horizontal lines ---
        pdf.set_draw_color(220, 220, 220)  # light gray lines
        y = 30
        while y < PAGE_HEIGHT - 15:
            pdf.line(10, y, PAGE_WIDTH - 10, y)
            y += 10  # spacing between lines

        # --- Footer ---
        pdf.set_y(-10)
        pdf.set_font("Times", "I", 8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
