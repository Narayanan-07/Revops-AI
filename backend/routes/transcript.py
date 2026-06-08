import io
from typing import Optional
from fastapi import APIRouter, UploadFile, File, Form
from database import supabase

router = APIRouter()


def _extract_text(filename: str, raw: bytes) -> str:
    """Pull plain text out of an uploaded transcript file.
    Supports .txt/.vtt/.srt/.md (decoded directly), .pdf (pdfplumber) and
    .docx (python-docx)."""
    name = (filename or "").lower()

    if name.endswith((".txt", ".vtt", ".srt", ".md", ".text")):
        return raw.decode("utf-8", errors="ignore")

    if name.endswith(".pdf"):
        import pdfplumber
        text = []
        with pdfplumber.open(io.BytesIO(raw)) as pdf:
            for page in pdf.pages:
                text.append(page.extract_text() or "")
        return "\n".join(text)

    if name.endswith(".docx"):
        import docx
        document = docx.Document(io.BytesIO(raw))
        return "\n".join(p.text for p in document.paragraphs)

    # Unknown extension: best-effort decode.
    return raw.decode("utf-8", errors="ignore")


@router.post("/submit/transcript")
async def submit_transcript(
    lead_id: str = Form(...),
    text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None),
):
    """Accept a transcript as pasted text OR an uploaded file. Extracted text is
    inserted into the transcripts table, which fires the Supabase webhook ->
    /trigger/discovery-intelligence (Agent 3)."""
    transcript_text = (text or "").strip()

    if file is not None:
        raw = await file.read()
        extracted = _extract_text(file.filename, raw).strip()
        if extracted:
            transcript_text = extracted

    if not transcript_text:
        return {"status": "error", "message": "No transcript text found"}

    result = supabase.table("transcripts").insert({
        "lead_id": lead_id,
        "transcript_text": transcript_text,
    }).execute()

    return {"status": "ok", "transcript_id": result.data[0]["id"]}
