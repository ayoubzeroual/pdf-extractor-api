from flask import Flask, request, jsonify
import requests
import pdfplumber
import tempfile
import os
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

@app.route('/')
def home():
    return "PDF Extractor API is running ✅"

@app.route('/extract', methods=['POST'])
def extract_text_from_pdf():
    data = request.get_json()
    pdf_url = data.get("pdf_url")

    if not pdf_url:
        return jsonify({"error": "Missing pdf_url"}), 400

    # Download the PDF
    try:
        r = requests.get(pdf_url, verify=False, timeout=30)
        r.raise_for_status()
    except Exception as e:
        return jsonify({"error": f"Failed to fetch PDF: {str(e)}"}), 400

    # Save it temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(r.content)
        tmp_path = tmp.name

    # Extract text and tables
    full_text = ""
    tables = []

    try:
        with pdfplumber.open(tmp_path) as pdf:
            for i, page in enumerate(pdf.pages):
                text = page.extract_text() or ""
                full_text += f"\n--- Page {i+1} ---\n{text}"
                page_tables = page.extract_tables() or []
                for t in page_tables:
                    tables.append(t)
    except Exception as e:
        return jsonify({"error": f"Failed to extract text from PDF: {str(e)}"}), 400
    finally:
        # Clean up temporary file
        try:
            os.unlink(tmp_path)
        except:
            pass

    return jsonify({
        "text": full_text, 
        "tables": tables,
        "status": "success"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
