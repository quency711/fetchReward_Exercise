# Fetch Rewards Coding Exercise - Text Similarity

Project purpose will focus on the similarity between two texts. The objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0. 

## Structure

```
fetchreward_nlp/
├── README.md
├── Dockerfile
├── stopwords.txt
├── app.py
├── caculate_similarity.py
├── templates/
    ├── home.html
└── requirements.txt

```
## What does the code do

1. Dockerfile - use to build docker image
2. stopwords.txt - use to remove stopwords in the sentences
3. app.py - use flask and html page to build a interactive application
4. caculate_similarity.py - backend nlp model to find the similarity score for two sentences
5. templates/home.html - a **interactive home page for end-user to type two sentences and has a predict button** to show the result
6. requirements.txt - contains required packges for model and application

## How to use the code
### I. Build docker image or pull from Dockerhub
#### From Local Computer:
1. ```git clone https://github.com/kkkris7/fetechreward-nlp.git```

2. ```cd fetechreward-nlp```

3. ```docker build -t chrisli957/fetchreward-nlp:latest .```
#### From DockerHub
```docker pull chrisli957/fetchreward-nlp:latest```

### II. Run Application with Docker
```docker run -it --rm -p 80:4000 chrisli957/fetchreward-nlp```

### III. Test with the Application
#### Method 1
open url http://0.0.0.0:80 and follow the instruction on the home page.

#### Method 2
```curl 0.0.0.0:80/predict -d '{"Sentence1": "<text of sentence1>", "Sentence2": "<text of sentence2>"}' -H 'Content-Type: application/json' ```
##### Example:
`curl 0.0.0.0:80/predict -d '{"Sentence1": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you.", "Sentence2": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."}' -H 'Content-Type: application/json'  `



