from fastapi import FastAPI, UploadFile, File, Form
import processing
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze/")
async def analyze_file(file: UploadFile = File(...), prompt: str = Form(...)):
    content = await file.read()
    result = processing.process_data(file.filename, content, prompt)
    return {"filename": file.filename, "result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
