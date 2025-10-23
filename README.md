# PDF Extractor API

A simple Flask API that extracts text and tables from PDF files via URL. Perfect for integration with Agent Builder workflows.

## 🎯 What it does

- Downloads PDFs from public URLs
- Extracts text content from all pages
- Extracts tables from all pages
- Returns structured JSON response
- Handles errors gracefully

## ⚙️ Setup Instructions

### Option 1: Deploy on Replit (Recommended)

1. Go to [https://replit.com/~](https://replit.com/~)
2. Click **"+ Create" → "Python"**
3. Name it `pdf-extractor-api`
4. Copy the contents of `main.py` into the editor
5. In the Shell tab, run: `pip install -r requirements.txt`
6. Click the green **"Run"** button
7. Copy your public URL (e.g., `https://pdf-extractor-api.ayoubz.repl.co`)

### Option 2: Run Locally

1. Install Python 3.10+
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the server:
   ```bash
   python main.py
   ```
4. API will be available at `http://localhost:8080`

## 📡 API Usage

### Endpoints

- `GET /` - Health check
- `POST /extract` - Extract text and tables from PDF

### Request Format

```bash
curl -X POST https://your-api-url.com/extract \
  -H "Content-Type: application/json" \
  -d '{"pdf_url": "https://example.com/document.pdf"}'
```

### Response Format

```json
{
  "text": "--- Page 1 ---\nDocument content here...",
  "tables": [
    [["Header1", "Header2"], ["Data1", "Data2"]]
  ],
  "status": "success"
}
```

## 🔧 Agent Builder Integration

1. Open your agent in [Agent Builder](https://platform.openai.com/agents)
2. Go to **Tools → Add Tool → "Custom Function"**
3. Fill in:
   - **Name:** `extract_text_from_pdf`
   - **Description:** "Extracts text and tables from a PDF via a web API"
   - **Endpoint URL:** `https://your-api-url.com/extract`
   - **Method:** POST
   - **Parameters schema:**
     ```json
     {
       "type": "object",
       "properties": {
         "pdf_url": { "type": "string", "description": "Public URL of the PDF" }
       },
       "required": ["pdf_url"]
     }
     ```

## 🧠 Usage in Workflow

In your LLM node, add:
> "Use the tool `extract_text_from_pdf` to get the text and tables of the uploaded PDF. Then analyze it to find the Bilan and CPC sections."

Pass the PDF URL:
```json
{ "pdf_url": "{{user_input.pdf_url}}" }
```

## 🚀 Features

- ✅ Handles text-based PDFs
- ✅ Extracts tables automatically
- ✅ Error handling for invalid URLs
- ✅ Temporary file cleanup
- ✅ Ready for production deployment

## 🔮 Future Enhancements

- OCR support for scanned PDFs (using pytesseract + pdf2image)
- Batch processing
- File upload support
- Authentication

## 📝 Example Test

Test with an AMMC financial report:
```bash
curl -X POST https://your-api-url.com/extract \
  -H "Content-Type: application/json" \
  -d '{"pdf_url": "https://www.ammc.ma/sites/default/files/2024-04/ETATS_FINANCIERS_WAFACASH_2023.pdf"}'
```