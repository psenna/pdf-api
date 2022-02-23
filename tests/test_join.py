from fastapi.testclient import TestClient

from tests.factory.pdf_factory import PdfFactory

import fitz


def test_join_2_pdfS(client: TestClient) -> None:

    pdf1 = PdfFactory.getPdf(1)
    pdf2 = PdfFactory.getPdf(2)

    files = [
        ('pdf_files', ('pdf1.pdf', pdf1, "application/pdf")),
        ('pdf_files', ('pdf2.pdf', pdf2, "application/pdf"))
        ]

    response = client.post("/join_pdf", files=files)

    assert response.status_code == 200

    novo_pdf = fitz.open(None, response.content, "pdf")

    assert novo_pdf.page_count == 3
    texto_por_pagina = ["PDF1", "PDF2", "PDF2"]
    for index, texto in enumerate(texto_por_pagina):
        assert texto in novo_pdf.get_page_text(index)


def test_join_2_pdfS_ordem_inversa(client: TestClient) -> None:

    pdf1 = PdfFactory.getPdf(1)
    pdf2 = PdfFactory.getPdf(2)

    files = [
        ('pdf_files', ('pdf2.pdf', pdf2, "application/pdf")),
        ('pdf_files', ('pdf1.pdf', pdf1, "application/pdf"))
        ]

    response = client.post("/join_pdf", files=files)

    assert response.status_code == 200

    novo_pdf = fitz.open(None, response.content, "pdf")

    assert novo_pdf.page_count == 3
    texto_por_pagina = ["PDF2", "PDF2", "PDF1"]
    for index, texto in enumerate(texto_por_pagina):
        assert texto in novo_pdf.get_page_text(index)

def test_join_3_pdfS(client: TestClient) -> None:

    pdf1 = PdfFactory.getPdf(1)
    pdf2 = PdfFactory.getPdf(2)
    pdf3 = PdfFactory.getPdf(3)


    files = [
        ('pdf_files', ('pdf1.pdf', pdf1, "application/pdf")),
        ('pdf_files', ('pdf2.pdf', pdf2, "application/pdf")),
        ('pdf_files', ('pdf3.pdf', pdf3, "application/pdf")),
        ]

    response = client.post("/join_pdf", files=files)

    assert response.status_code == 200

    novo_pdf = fitz.open(None, response.content, "pdf")

    assert novo_pdf.page_count == 6
    texto_por_pagina = ["PDF1", "PDF2", "PDF2", "PDF3", "PDF3", "PDF3"]
    for index, texto in enumerate(texto_por_pagina):
        assert texto in novo_pdf.get_page_text(index)

def test_join_txt(client: TestClient) -> None:

    arquivo_txt = PdfFactory.getTxt()
    pdf2 = PdfFactory.getPdf(2)

    files = [
        ('pdf_files', ('texto.txt', arquivo_txt, "application/pdf")),
        ('pdf_files', ('pdf2.pdf', pdf2, "application/pdf"))
        ]

    response = client.post("/join_pdf", files=files)

    assert response.status_code == 400

