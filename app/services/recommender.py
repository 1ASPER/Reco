# app/services/recommender.py

COMBO_RECOMMENDATIONS = {
    frozenset(["Морковь вес", "Сметана ВМ 15% 170г"]): "Картофель молодой 1кг",
    frozenset(["Хлеб Солдатский 320г", "Сметана ВМ 15% 170г"]): "Зелень укроп 100г",
    frozenset(["Морковь вес", "Хлеб Солдатский 320г"]): "Куриные котлеты охлажденные 400г",
    frozenset(["Мука Алия 1 сорт 1кг", "Сметана ВМ 15% 170г"]): "Яйца куриные 10шт",
    frozenset(["Чипсы Lay's сыр 70г", "Кофе Lavaz C.E Gusto мол 250г"]): "Шоколад молочный Alpen Gold 90г",
    frozenset(["Кофе Lavaz C.E Gusto мол 250г", "Сметана ВМ 15% 170г"]): "Печенье савоярди 200г",
    frozenset(["Хлеб Солдатский 320г", "Мука Алия 1 сорт 1кг"]): "Сыр Российский 200г",
    frozenset(["Морковь вес", "Сметана ВМ 15% 170г", "Хлеб Солдатский 320г"]): "Суповая курица 1.2кг",
}

SINGLE_RECOMMENDATIONS = {
    "Морковь вес": "Картофель молодой 1кг",
    "Сметана ВМ 15% 170г": "Блины с мясом 300г",
    "Хлеб Солдатский 320г": "Колбаса варёная Докторская 400г",
    "Мука Алия 1 сорт 1кг": "Дрожжи сухие 10г",
    "Чипсы Lay's сыр 70г": "Pepsi 0.5л",
    "Кофе Lavaz C.E Gusto мол 250г": "Сливки стерилизованные 10% 200мл",
}


def recommend_complementary_items_by_name(cart_items: list[str]) -> str | None:
    cart_set = set(cart_items)

    # 1. Комбинированные рекомендации
    for combo, recommendation in COMBO_RECOMMENDATIONS.items():
        if combo.issubset(cart_set):
            return recommendation

    # 2. Одиночные рекомендации
    for item in cart_items:
        if item in SINGLE_RECOMMENDATIONS:
            return SINGLE_RECOMMENDATIONS[item]

    return None
