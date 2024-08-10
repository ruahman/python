import pandas as pd
from fpdf import FPDF


def csv_to_pdf(csv_file, pdf_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Create instance of FPDF class
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add a title
    pdf.cell(200, 10, txt="CSV to PDF", ln=True, align="C")

    # Add a line break
    pdf.ln(10)

    # Add column headers
    col_width = pdf.w / (len(df.columns) + 1)  # Column width based on page width
    for column in df.columns:
        pdf.cell(col_width, 10, column, border=1, align="C")
    pdf.ln()

    # Add rows from DataFrame
    for row in df.itertuples(index=False):
        for item in row:
            text = str(item).replace("\u2013", "")  # Remove special characters
            pdf.cell(col_width, 10, text, border=1)
        pdf.ln()

    # Save the PDF with the specified filename
    pdf.output(pdf_file)


# Example usage
csv_file = "isabela-pretty.csv"  # Replace with your CSV file path
pdf_file = "output.pdf"  # Replace with desired PDF file name
csv_to_pdf(csv_file, pdf_file)
