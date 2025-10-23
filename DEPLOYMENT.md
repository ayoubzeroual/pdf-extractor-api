# 🚀 Deployment Guide

## Quick Deploy Options

### Option 1: Replit (Recommended - Free & Easy)

1. **Go to [Replit.com](https://replit.com/~)**
2. **Click "+ Create" → "Python"**
3. **Name it:** `pdf-extractor-api`
4. **Copy files:**
   - Copy `main.py` content into the editor
   - Copy `requirements.txt` content
5. **Install dependencies:**
   - Click "Shell" tab
   - Run: `pip install -r requirements.txt`
6. **Run the app:**
   - Click the green "Run" button
   - Copy your public URL (e.g., `https://pdf-extractor-api.ayoubz.repl.co`)

### Option 2: Render (Free Tier)

1. **Go to [Render.com](https://render.com)**
2. **Click "New" → "Web Service"**
3. **Connect your GitHub repo** (or create one)
4. **Configure:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Environment:** Python 3
5. **Deploy!**

### Option 3: Railway (Free Tier)

1. **Go to [Railway.app](https://railway.app)**
2. **Click "New Project" → "Deploy from GitHub repo"**
3. **Select your repo**
4. **Railway auto-detects Python and runs `main.py`**
5. **Deploy!**

## 🔧 Environment Variables (Optional)

If you need to configure anything:

```bash
# For production
export FLASK_ENV=production
export PORT=8080
```

## 📝 Testing Your Deployment

Once deployed, test with:

```bash
# Health check
curl https://your-app-url.com/

# Extract test
curl -X POST https://your-app-url.com/extract \
  -H "Content-Type: application/json" \
  -d '{"pdf_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"}'
```

## 🎯 Agent Builder Integration

1. **Open [Agent Builder](https://platform.openai.com/agents)**
2. **Go to Tools → Add Tool → "Custom Function"**
3. **Fill in:**
   - **Name:** `extract_text_from_pdf`
   - **Description:** "Extracts text and tables from a PDF via a web API"
   - **Endpoint URL:** `https://your-deployed-url.com/extract`
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

## ✅ You're Done!

Your PDF extractor is now live and ready to use in Agent Builder workflows!
