import os
import openai
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/q/{q_text}")
async def chatgpt(q_text):
  openai.api_key = os.environ.get('OPENAI_API_KEY')
  try:
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": q_text}]
    )
    return {"answer": completion.choices[0].message.content}
  except Exception as e:
    return {"answer": str(e)}

port = int(os.environ.get('SERVER_PORT'))
if __name__ == '__main__':
  uvicorn.run("main:app", port=port, reload=True, host="0.0.0.0")
