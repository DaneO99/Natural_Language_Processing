from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create a SentimentIntensityAnalyzer object
sia_obj = SentimentIntensityAnalyzer()

# List of Harry Potter review files in the current directory
files = [
    "Harry_Potter_and_the_Prisoner_of_Azkaban_reviews.txt",
    "Harry_Potter_and_the_Chamber_of_Secrets_reviews.txt",
    "Harry_Potter_and_the_Goblet_of_Fire_reviews.txt",
    "Harry_Potter_and_the_Half_Blood_Prince_reviews.txt",
    "Harry_Potter_and_the_Order_of_the_Phoenix_reviews.txt",
    "Harry_Potter_and_the_Deathly_Hallows_Part_1_reviews.txt",
    "Harry_Potter_and_the_Deathly_Hallows_Part_2_reviews.txt",
    "Harry_Potter_and_the_Philosophers_Stone_reviews.txt"
]

# Iterate through each file
for file_name in files:
    # Initialize sentiment score accumulators
    total_pos = total_neg = total_neu = total_compound = 0
    review_count = 0

    # Open the file and read the reviews
    with open(file_name, "r") as file:
        reviews = file.readlines()
    
    # Analyze each review in the file
    for review in reviews:
        sentiment_dict = sia_obj.polarity_scores(review)
        total_pos += sentiment_dict['pos']
        total_neg += sentiment_dict['neg']
        total_neu += sentiment_dict['neu']
        total_compound += sentiment_dict['compound']
        review_count += 1
    
    # Calculate the average sentiment scores
    if review_count > 0:
        average_pos = total_pos / review_count
        average_neg = total_neg / review_count
        average_neu = total_neu / review_count
        average_compound = total_compound / review_count
    else:
        average_pos = average_neg = average_neu = average_compound = 0

    # Print the file name and its average sentiment analysis
    print(f"File: {file_name}")
    print(f"Average Sentiment Analysis:")
    print(f"Positive: {average_pos:.3f}")
    print(f"Negative: {average_neg:.3f}")
    print(f"Neutral: {average_neu:.3f}")
    print(f"Compound: {average_compound:.3f}")
    print("-" * 50)  # Separator for better readability
