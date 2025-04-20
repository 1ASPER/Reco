# app/api/endpoints.py

from fastapi import APIRouter, Request
from app.services.recommender import recommend_complementary_items_by_name

router = APIRouter()

@router.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    cart = data.get("cart", [])

    if not isinstance(cart, list):
        return {"error": "cart must be a list of products"}

    # Извлекаем названия товаров
    product_names = [item.get("Товар") for item in cart if "Товар" in item]

    recommendation = recommend_complementary_items_by_name(product_names)

    return {"recommendation": recommendation}
