# BT4012_Fake_Reviews
## Motivation / Potential Social or Business Implication of Project
The motivation behind this ML project is to combat the pervasive issue of fake online reviews, which can deceive consumers, harm business reputations, and disrupt fair competition. By developing effective models to identify and flag fake reviews, it aims to restore consumer trust in online platforms, empower users to make informed decisions, and improve the overall quality of reviews. This reduces deception and fosters transparency in the online environment, while businesses can benefit from improved reputation management, enhanced product development, and a competitive edge. Furthermore, compliance with legal regulations and risk mitigation in the realm of online reviews are additional positive outcomes of this project.
## Basic Information about the Dataset
The data is obtained from the Yelp Restaurant Reviews Dataset, yelpResData.db, containing 3 tables: Restaurant, Review and Reviewer.  It is a collection of data related to businesses and reviews on the Yelp platform. It contains information about restaurants and their associated reviews as well as of reviewers who posted the reviews. We will be merging the tables into one dataset.


| Table         | No. Of Columns| No. Of Rows   |
| ------------- | ------------- | ------------- |
| Restaurant    |      30       |   242,652     |
| Reviewer      |      13       |    16,941     |
| Review        |      10       |   788, 741    | 


## Data Preprocessing and ML Models
#### Data preprocessing
We will clean the data by removing empty cells and null values. We will then do tokenization to convert the review text data into individual words (tokens) for further processing. After converting the tokens to lower case, we will remove punctuations and stop words. Finally, stemming and lemmatization will reduce each token to its root form, making the text data ready for model training/feature engineering.
#### Implementing Machine Learning Models
Semi supervised learning: We plan to use RandomForestClassifier and Gaussian Naive Bayes to tag the reviews(Fake/Not Fake)
Feature engineering: Convert the text data into numerical features that can be used by a machine learning model. 
This could be done using techniques like Bag of Words, TF-IDF, or word embeddings like Word2Vec or GloVe or BERT (hugging face) for tasks like text classification, named entity recognition.
To train a classification model on our preprocessed dataset. We will be implementing: Logistic Regression, Naive Bayes, Support Vector Machines, Random Forests, Gradient Boosting (like XGBoost),  Neural Network. Facebook's FastText library (Text classification tool) and libraries like TextBlob and VADER. (Valence Aware Dictionary and Sentiment Reasoner)
