from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from logic import create_video, upscale_video, output_folder_path
from pydantic import BaseModel,  ValidationError
from fastapi import HTTPException
import uvicorn

import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount the directory containing your static files
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "name": "World"})



@app.post("/generate_video")

def process_text_prompt(text_prompt: str = Form(...)):
    if not text_prompt:
        raise HTTPException(status_code=400, detail="Text prompt is missing or empty.")
    
 
    prompt = text_prompt
    print(f'{prompt}')
    # Add this line for debugging
    print("Received text prompt:")  

    # Perform video generation based on the text prompt

    video_path = create_video(prompt)
    # video_path2 = upscale_video(prompt)
    
    # Placeholder logic for demonstration
    
    generated_video_url = os.path.join(output_folder_path, os.path.basename(video_path))
    return {"video_url": generated_video_url}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080)
