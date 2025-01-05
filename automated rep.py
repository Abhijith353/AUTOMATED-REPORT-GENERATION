import csv

# Data to be written
data = [
    ['Category', 'Value'],
    ['A', 10],
    ['B', 20],
    ['C', 30],
    ['D', 40],
    ['E', 50]
]

# Writing to csv file
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
import pandas as pd
from fpdf import FPDF

# Read data from a CSV file
def read_data(file_path):
    return pd.read_csv(file_path)

# Perform data analysis and generate summary statistics
def analyze_data(df):
    summary = df.describe()  # Basic summary statistics
    return summary

# Create a formatted PDF report using FPDF
def create_pdf_report(summary, output_pdf_path):
    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Title of the report
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Automated Data Analysis Report", ln=True, align='C')
    pdf.ln(10)

    # Add summary statistics to the report
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt="Summary Statistics:", ln=True)
    pdf.ln(5)

    # Convert the summary statistics DataFrame to string and add it to the PDF
    summary_str = summary.to_string()
    pdf.multi_cell(0, 10, summary_str)
    pdf.ln(10)

    # Output the PDF file
    pdf.output(output_pdf_path)
    print(f"Report saved as {output_pdf_path}")

# Main function to orchestrate the steps
def main():
    # Define file paths
    input_file = 'data.csv'  # Path to your CSV data file
    pdf_report = 'data_analysis_report.pdf'  # Output PDF report path

    # Step 1: Read data from CSV file
    df = read_data(input_file)

    # Step 2: Perform data analysis
    summary = analyze_data(df)

    # Step 3: Create and save the PDF report
    create_pdf_report(summary, pdf_report)

# Run the script
if __name__ == "__main__":
    main()

