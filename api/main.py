from io import BytesIO
from typing import List
from fastapi import FastAPI, UploadFile, Form, HTTPException
from fastapi.responses import StreamingResponse
import fitz

app = FastAPI()

@app.get("/")
async def home():
    return {"Home"}

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