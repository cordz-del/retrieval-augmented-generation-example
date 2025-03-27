def retrieve_information(query):
    # Simulated retrieval from a dataset
    dataset = {
        "python": "Python is a versatile programming language.",
        "ai": "Artificial Intelligence enables machines to mimic human behavior."
    }
    return dataset.get(query.lower(), "No information found.")

def generate_response(retrieved_text):
    # Placeholder for generative AI response logic
    return f"Based on the retrieved info: {retrieved_text}"

if __name__ == "__main__":
    query = input("Enter a query (e.g., 'python', 'ai'): ")
    info = retrieve_information(query)
    response = generate_response(info)
    print("Response:", response)
