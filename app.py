from fastapi import FastAPI, File, UploadFile
import openai

app = FastAPI()

@app.post("/describe")
async def describe_image(file: UploadFile = File(...)):
    response = openai.Image.transcribe(
        image=file.file,
        model="gpt-4-vision-preview",
        max_tokens=300,
    )
    return {"description": response.choices[0].text}
