## Fetch Rewards Coding Exercise - Text Similarity

The objective of this project is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0. 
 

## Files

```
├── Dockerfile
├── README.md 
├── functions.py
├── main.py
├── requirements.txt 
└── stopwords.txt
```

## What each file represents 

1. Dockerfile : used to build docker image
2. stopwords.txt : used to remove the stopwords in the sentences, the function provides the option to use stopwords or not 
3. functions.py - functions used to calculate similarity between two texts
4. main.py - used to run fastapi
6. requirements.txt - contains required packges for model and application

## Answers 
1. Do you count punctuation or only words?
> No, the punctuations are excluded. 
2. Which words should matter in the similarity comparison?
> All the words exclude stopwords are important.  
3. Do you care about the ordering of words?
> Yes, the ordering is important in this model. 
4. What metric do you use to assign a numerical value to the similarity?
> The function calculated the cosine distance between two texts. 
5. What type of data structures should be used? (Hint: Dictionaries and lists are particularly helpful data structures that can be leveraged to calculate the similarity of two pieces of text.)
> Dictionaries are primarily used. I used dictionary to get verctor values of the text after converting it to n-gram bag.  

## How to run it
### Run the application through Docker

1. ```git clone https://github.com/quency711/fetchReward_Exercise.git```
2. ```docker build -t myimage .  ```
3. ```docker run -d --name fetchReward -p 80:80 myimage  ```  

### Test with the Application

`curl -X 'POST' \                                                           
  'http://127.0.0.1:80/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text1": "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'\''ll get points based on the cost of the products. You don'\''t need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'\''ll find the savings for you."
,
  "text2": "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."}'`

### Resources

1. Docker base image: https://hub.docker.com/r/tiangolo/uvicorn-gunicorn-fastapi/dockerfile



