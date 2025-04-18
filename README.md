# **AsiaCart FastAPI Backend**

This is the backend for the **AsiaCart** recommendation system, built with **FastAPI**. It generates product recommendations using **item-based collaborative filtering**.

---

## **Project Structure**

```plaintext
asiacart-backend/
│
├── app/
│   ├── __init__.py                     # Initialization for app
│   ├── main.py                         # FastAPI entry point
│   ├── models/
│   │   └── item_similarity_df.pkl      # Pre-trained similarity matrix
│   ├── services/
│   │   └── recommender.py              # Recommendation logic
│   └── api/
│       └── endpoints.py                # API routes
│
├── requirements.txt                    # Project dependencies
├── run.sh                              # Shell script to run the server
├── README.md                           # This file
└── .gitignore                          # Git ignore file
