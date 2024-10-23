# Import libraries
import re
import requests
import nltk
from sentence_transformers import SentenceTransformer
import torch
import tensorflow as tf

# Length of reply (in sentences)
length_of_reply = 3

# Loads model
model = SentenceTransformer("multi-qa-mpnet-base-dot-v1", model_kwargs={"torch_dtype": "float16"})


def download():
    # Downloads data from github
    data_base_url = "https://raw.githubusercontent.com/ComputerScienceTHS/Group-LLM-Project/refs/heads/main/Datasets/history_data.txt"
    response = requests.get(data_base_url)
    with open("db1.txt", "wb") as file:
        file.write(response.content)


def preprocessing():
    with open("db1.txt", "r", encoding="utf_8") as file:
        clean_file = file.read()
    clean_file = re.sub(r"\s+", " ", clean_file)
    clean_file = re.sub(r"\n+", "", clean_file)
    clean_file = clean_file.lower()
    corpus = nltk.sent_tokenize(clean_file)
    return corpus


def cosine_similarity(corpus):
    pass


def ann_search():
    pass

def embedding(corpus):
    # Instantiates pool of workers
    pool = model.start_multi_process_pool()
    # Encodes data
    print("Encoding")
    vectors = model.encode_multi_process(preprocessing(), pool=pool, show_progress_bar=True)
    model.stop_multi_process_pool(pool)
    print("Done encoding; saving to disk")
    torch.save(tf.convert_to_vectors(vectors), "vector_db.pt")


def answer_queries(corpus):
    vectors = torch.load('vector_db.pt')
    while True:
        best_finds = {}
        # Encodes query
        print("Encoding Query")
        query = model.encode(input(), convert_to_tensor=True)

        # Calculates cosine sim
        print("Calculating similarities. . ")
        similarities =
        print("Responding to query. . .")

        for index, sentence in enumerate(corpus):
            best_finds.update({sentence: similarities[index]})
        best_finds = sorted(best_finds)
        for x in range(length_of_reply):
            print(best_finds[len(best_finds) - (x + 1)])


# Preprocesses data
sentences = preprocessing()
print("Estimated Time: " + str(len(sentences)/142) + " sec (According to model data but probably inaccurate)")

# LLM Embedding
embedding(sentences)

