from flask import Flask, request, render_template, jsonify
import pdfplumber
import openpyxl
from pdf2image import convert_from_path
import pytesseract
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the uploads directory exists

# Function to extract questions from text-based PDFs
def extract_questions_from_pdf(pdf_path, question_pattern="?"):
    questions = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                for line in text.split("\n"):
                    if question_pattern in line:
                        questions.append(line.strip())
    return questions

# Function to extract text from scanned PDFs using OCR
def extract_text_from_scanned_pdf(pdf_path):
    pages = convert_from_path(pdf_path)
    extracted_text = ""
    for page_image in pages:
        text = pytesseract.image_to_string(page_image)
        extracted_text += text + "\n"
    return extracted_text

# Function to write extracted questions into an Excel file
def write_questions_to_excel(questions, excel_path):
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.title = "Questions"

    for i, question in enumerate(questions, start=1):
        sheet.cell(row=i, column=1, value=question)

    wb.save(excel_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_pdf():
    pdf_file = request.files['pdfFile']
    excel_path = request.form['excelPath']
    question_pattern = request.form.get('questionPattern', '?')

    if not pdf_file or not excel_path:
        return jsonify({"error": "Please provide both a PDF file and an Excel path."}), 400

    pdf_path = os.path.join(UPLOAD_FOLDER, pdf_file.filename)
    pdf_file.save(pdf_path)

    try:
        questions = extract_questions_from_pdf(pdf_path, question_pattern)
        if not questions:  # If no questions were found, attempt OCR
            text = extract_text_from_scanned_pdf(pdf_path)
            questions = [line.strip() for line in text.split("\n") if question_pattern in line]

        write_questions_to_excel(questions, excel_path)
        return jsonify({"success": f"Questions saved to {excel_path}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
