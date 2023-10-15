

import sqlite3
import pandas as pd
from time import time

def load_training_data():
    print("Obtaining Training Data")
    # db_path = "/Users/admin/Desktop/UNI/Y3/y3s1/BT4012 Project/BT4012_Reviews/YelpData/yelpResData.db"
    conn = sqlite3.connect(db_path)

     

    conn.text_factory = lambda x: str(x, 'gb2312', 'ignore')
    db_cursor = conn.cursor()

    # define sql queries in a dictionary 

    # for reviews, we select those where flagged are either Y/N to be used in training set 
    sql_queries = {
        'review':  "SELECT date AS reviewDate, reviewID, reviewerID, reviewContent, rating AS reviewRating,\
                        usefulCount AS reviewUsefulCount, coolCount AS reviewCoolCount, funnyCount AS reviewFunnyCount, restaurantID, flagged",
        'reviewer': "SELECT reviewerID, name AS reviewerName, location AS reviewerLocation, yelpJoinDate AS reviewerYelpJoinDate, \
                        friendCount AS reviewerFriendCount, reviewCount AS reviewerNumReviews, reviewCount AS reviewerFirstCount, usefulCount AS reviewerUsefulCount, \
                             coolCount AS reviewerCoolCount, funnyCount AS reviewerFunnyCount, complimentCount AS reviewerComplimentCount, \
                              tipCount AS reviewerTipCount, fanCount AS reviewerFanCount FROM reviewer",
        'restaurant': "SELECT restaurantID, location AS resLocation, name AS resName, \
                        reviewCount AS resReviewCount, rating AS resRating FROM restaurant"
    }

    #  create a dictionary of data frames to load the dfs for the 3 tables 

    data_frames = {}

    # iterate through sql query dict to modify original data to new data 
    for table_name, sql_query in sql_queries.items():
        # execute query 
        db_cursor.execute(sql_query)

        # create df and add to dict 
        data_frames[table_name] = pd.DataFrame(db_cursor.fetchall(), columns=[column[0] for column in db_cursor.description])
        
        # save the files to csv 
        # data_frames[table_name].to_csv(f"{table_name}.csv", sep=',', index=False)
        # print(data_frames[table_name])
        print(data_frames[table_name].info())


    # Merge all DataFrames
    review_df = data_frames["review"]
    reviewer_df = data_frames["reviewer"]
    restaurant_df = data_frames["restaurant"]
    review_reviewer_df = review_df.merge(reviewer_df, on='reviewerID', how='inner')
    merged_df = review_reviewer_df.merge(restaurant_df, on='restaurantID', how='inner')

    print("Training Data Obtained")
    return merged_df



def main():
    merged_df = load_training_data()

    merged_df_2 = merged_df.sample(n=50000, random_state=1)

# If you want to save the sampled data to a new CSV file:
    merged_df_2.to_csv('merged_df.csv', sep=',', index=False)

if __name__ == '__main__':
    main()

