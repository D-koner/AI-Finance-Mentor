from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class UserData(BaseModel):
    age: int
    income: float
    expenses: float
    savings: float
    debt: float

@app.post("/ai-advice")
def get_advice(data: UserData):
    savings_rate = (data.income - data.expenses) / data.income * 100

    advice = f"""
📊 Financial Summary:

- Savings Rate: {savings_rate:.1f}%
- Monthly Surplus: ₹{data.income - data.expenses}

💡 Advice:
"""

    if savings_rate < 20:
        advice += "\n⚠️ Increase your savings rate."
    else:
        advice += "\n✅ Good savings habit."

    if data.debt > data.income * 5:
        advice += "\n🚨 High debt. Reduce it."

    advice += "\n\n📈 Suggested: Start SIP investing."

    return {"advice": advice}