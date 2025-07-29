from fastapi import FastAPI
from pydantic import BaseModel
from data import SHOP_DATA, HISTORICAL_DATA
from ai_engine import DeepSeekAI
from config import APP_TITLE

app = FastAPI(title=APP_TITLE)
ai_engine = DeepSeekAI()

class ChatRequest(BaseModel):
    question: str

@app.get("/shop/analysis")
async def get_shop_analysis():
    return {
        "shop_data": SHOP_DATA,
        "ai_insights": ai_engine.analyze_shop_performance(SHOP_DATA),
        "historical_data": HISTORICAL_DATA
    }

@app.post("/chat")
async def chat_with_ai(req: ChatRequest):
    return {"answer": ai_engine.chat_response(req.question, SHOP_DATA)}
