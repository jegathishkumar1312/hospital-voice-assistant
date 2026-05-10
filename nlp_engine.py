from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model (light + fast)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Your hospital intents (training examples)
intent_examples = {
    "icu": [
        "where is icu",
        "icu location",
        "show icu",
        "tell me about icu"
    ],
    "pharmacy": [
        "where is pharmacy",
        "pharmacy location",
        "medicine shop",
        "drug store in hospital"
    ],
    "emergency": [
        "emergency ward",
        "where is emergency",
        "urgent care",
        "accident help"
    ],
    "billing": [
        "billing counter",
        "payment section",
        "hospital bill",
        "fees payment"
    ],
    "timing": [
        "hospital timing",
        "opening time",
        "when hospital open",
        "working hours"
    ]
}

# Precompute embeddings
intent_embeddings = {
    intent: model.encode(sentences)
    for intent, sentences in intent_examples.items()
}

def get_intent(query):
    query_vec = model.encode([query])

    best_intent = None
    best_score = 0

    for intent, embeddings in intent_embeddings.items():
        score = cosine_similarity(query_vec, embeddings).max()

        if score > best_score:
            best_score = score
            best_intent = intent

    # threshold filter (important)
    if best_score < 0.5:
        return "unknown"

    return best_intent