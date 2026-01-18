# pdf-question-extractor

A Flask web application that automatically extracts questions from PDF files and saves them into an Excel spreadsheet. It handles both standard text-based PDFs and scanned image PDFs using OCR (Optical Character Recognition).

## 🌟 Features

* **Dual Extraction Modes:**
    * **Text-based:** Rapidly extracts text from standard PDFs using `pdfplumber`.
    * **OCR (Scanned):** Uses `pytesseract` to read text from scanned images or non-selectable PDFs.
* **Excel Export:** Automatically formats and saves found questions into an `.xlsx` file using `openpyxl`.
* **Custom Patterns:** Defaults to looking for sentences ending in `?`, but is customizable via the UI.
* **Web Interface:** Simple upload interface built with Flask.

## 🛠️ Prerequisites

This project requires system-level dependencies for image processing and OCR.

### 1. Python 3.x
Ensure Python is installed on your machine.

### 2. Tesseract OCR (Required for `pytesseract`)
* **Windows:** Download the installer from [UB-Mannheim/tesseract](https://github.com/UB-Mannheim/tesseract/wiki).
    * *Important:* Add the Tesseract installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your System Path environment variable.
* **macOS:** `brew install tesseract`
* **Linux:** `sudo apt-get install tesseract-ocr`

### 3. Poppler (Required for `pdf2image`)
* **Windows:** Download the latest binary from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/). Extract it and add the `bin` folder to your System Path.
* **macOS:** `brew install poppler`
* **Linux:** `sudo apt-get install poppler-utils`

## 🚀 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/pdf-question-extractor.git](https://github.com/yourusername/pdf-question-extractor.git)
    cd pdf-question-extractor
    ```

2.  **Create a virtual environment**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Python dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

1.  **Start the application**
    ```bash
    python app.py
    ```

2.  **Open your browser**
    Navigate to `http://127.0.0.1:5000`.

3.  **Process a PDF**
    * Upload a PDF file.
    * Enter the full path where you want the Excel file saved (e.g., `output.xlsx` or `C:\Users\You\Documents\questions.xlsx`).
    * (Optional) Update the "Question Pattern" if you are searching for specific text strings.
    * Click **Process**.

## 📂 Project Structure

* `app.py`: Main Flask application logic.
* `templates/`: HTML files for the web interface.
* `uploads/`: Temporary storage for processing PDFs.
* [cite_start]`requirements.txt`: List of Python libraries[cite: 2].
* `vercel.json`: Configuration for Vercel deployment.

## ☁️ Deployment

This project is configured for deployment on Vercel (`vercel.json` included).

**Note:** Because this app relies on binary dependencies (Tesseract and Poppler) for OCR, a standard serverless environment may require a custom buildpack or Docker container to function fully. The text-only extraction (via `pdfplumber`) will work in most standard Python environments.

## 📄 License

[MIT](https://choosealicense.com/licenses/mit/)
