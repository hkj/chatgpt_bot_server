import os
import openai
from fastapi import FastAPI

app = FastAPI()

@app.get("/q/{q_text}")
async def chatgpt(q_text):
  openai.api_key = os.environ.get('OPENAI_API_KEY')
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": q_text}]
  )

  return {"answer": completion.choices[0].message.content}

# if __name__ == '__main__':
#   uvicorn.run("main:app", port=8000, reload=True)
