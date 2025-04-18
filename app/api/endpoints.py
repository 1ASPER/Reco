from fastapi import APIRouter, Request
from app.services.recommender import recommend_complementary_items

router = APIRouter()

@router.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    cart = data.get("cart", [])
    
    recommendations = recommend_complementary_items(cart, n=5)
    return {"recommendations": recommendations}
