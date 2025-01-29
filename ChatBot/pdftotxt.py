import PyPDF2

# Specify the path to the PDF file
pdf_path = "stepbrothersscript.pdf"

# Open the PDF file
with open(pdf_path, "rb") as file:
    reader = PyPDF2.PdfReader(file)
    script_text = ""

    # Extract text from each page
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        script_text += page.extract_text() + "\n"

# Specify the filename for the text file
text_filename = "Step_Brothers_Script.txt"

# Write the extracted text to the text file
with open(text_filename, "w", encoding="utf-8") as text_file:
    text_file.write(script_text)

print(f"Script saved to {text_filename}")
