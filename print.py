import sys
import weasyprint
import os

# Check if an input file was provided
if len(sys.argv) < 2:
    print("Usage: python print.py <input_filename.html>")
    sys.exit(1)

# Get the input HTML file from the command line
input_filename = sys.argv[1]

# Check if the input file exists
if not os.path.isfile(input_filename):
    print(f"Error: File '{input_filename}' not found.")
    sys.exit(1)

# Generate the output PDF filename by replacing the .html extension with .pdf
output_filename = os.path.splitext(input_filename)[0] + '.pdf'

# Load the HTML content from the input file
with open(input_filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Generate the PDF using WeasyPrint with the custom stylesheet
weasyprint.HTML(string=html_content).write_pdf(
    output_filename,
    stylesheets=['print.css'],
    presentational_hints=True
)

print(f"PDF generated successfully as '{output_filename}'")

