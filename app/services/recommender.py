import os
import pandas as pd
import pickle

# Абсолютный путь от корня проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'item_similarity_df.pkl')

# Загрузка модели
with open(MODEL_PATH, 'rb') as f:
    item_similarity_df = pickle.load(f)

def get_recommendations(item_id, n=5):
    try:
        similar_items = item_similarity_df[item_id].sort_values(ascending=False)
        return similar_items.iloc[1:n+1].index.tolist()
    except KeyError:
        return []

def recommend_complementary_items(current_cart, n=5):
    all_recommendations = []

    for item in current_cart:
        item_recs = get_recommendations(item, n * 2)
        all_recommendations.extend(item_recs)

    recommendation_counts = pd.Series(all_recommendations).value_counts()
    recommendation_counts = recommendation_counts.drop(current_cart, errors='ignore')

    reco_list = recommendation_counts.head(n).index.tolist()

    if reco_list:
        return reco_list[0]
    else:
        return None
