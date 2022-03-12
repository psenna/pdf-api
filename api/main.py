from io import BytesIO
import os
from typing import List
from fastapi import FastAPI, UploadFile, Form, HTTPException, Request
from fastapi.responses import StreamingResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import fitz

app = FastAPI()

dirname = os.path.dirname(__file__)

app.mount("/assets", StaticFiles(directory=os.path.join(dirname, 'assets')), name="assets")

templates = Jinja2Templates(directory=os.path.join(dirname, 'templates'))

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "titulo": "Api de PDFs"})

@app.get("/join_pdf", response_class=HTMLResponse)
async def join_pdf_page(request: Request):
    return templates.TemplateResponse("join_pdf.html", {"request": request})
    

@app.post("/join_pdf")
async def join_pdf(pdf_files: List[UploadFile], output_file_name:str = Form("out.pdf")):
    new_pdf = fitz.open()
    for pdf_file in pdf_files:
        pdf_stream = await pdf_file.read()
        try:
            pdf = fitz.open(None, pdf_stream, "pdf")
        except:
            raise HTTPException(status_code=400, detail=f"O arquivo {pdf_file.filename} não é um PDF válido.")
        new_pdf.insert_pdf(pdf)
    
    new_pdf_buffer = BytesIO(new_pdf.tobytes())

    headers = {
        'Content-Disposition': f'attachment; filename={output_file_name}'
    }

    return StreamingResponse(new_pdf_buffer, headers=headers, media_type="application/pdf")