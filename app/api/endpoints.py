from fastapi import APIRouter, Request
from app.services.recommender import recommend_complementary_items

router = APIRouter()

@router.post("/recommend")
async def recommend(request: Request):
    data = await request.json()
    cart = data.get("cart", [])

    # Проверка: cart должен быть списком целых чисел
    if not isinstance(cart, list) or not all(isinstance(i, int) for i in cart):
        return {"error": "Invalid cart format. Expected list of integers."}

    recommendation = recommend_complementary_items(cart, n=5)

    return {"recommendation": recommendation}
