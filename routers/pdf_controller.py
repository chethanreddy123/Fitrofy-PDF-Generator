import io
from fastapi import APIRouter, Body
from fastapi.responses import StreamingResponse
from fastapi import FastAPI, HTTPException
from services.pdf_service import PDFServiceV2
import asyncio
from helper import fetch_user_details, get_diet_plans
import loguru as logger

router = APIRouter()


async def generate_pdf(data: dict ) -> StreamingResponse:
    template_path = "index.html"  
    html_content = PDFServiceV2.render_html(template_path, data)

    # Create a new coroutine instance for each request
    pdf_task = asyncio.ensure_future(PDFServiceV2.generate_pdf_from_html2(html_content))

    # Send response immediately and close the connection
    response = StreamingResponse(io.BytesIO(await pdf_task), media_type="application/pdf", headers={"Content-Disposition": "inline; filename=output.pdf"})
    return response



@router.get("/get_user_and_diet_pdf")
async def get_user_and_diet(auth_token: str, date_range: int, date: str):
    try:
        template_path = "index.html"  
        user_details = fetch_user_details(auth_token)

        # Get diet plans
        diet_plans = get_diet_plans(auth_token, date_range, date)

        logger.logger.info("User Details: ", user_details)


        data = {"user_details": user_details, "diet_plans": diet_plans}
        html_content = PDFServiceV2.render_html(template_path, data)
        pdf_task = asyncio.ensure_future(PDFServiceV2.generate_pdf_from_html2(html_content))

        response = StreamingResponse(io.BytesIO(await pdf_task), media_type="application/pdf", headers={"Content-Disposition": "inline; filename=output.pdf"})
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")