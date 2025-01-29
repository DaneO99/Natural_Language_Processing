import requests
from bs4 import BeautifulSoup
import re
import os

# List of URLs for Harry Potter movies
urls = [
    "https://www.imdb.com/title/tt0241527/reviews/?ref_=tt_ov_rt",  # Philosopher's Stone
    "https://www.imdb.com/title/tt0304141/reviews/?ref_=tt_ov_rt",  # Chamber of Secrets
    "https://www.imdb.com/title/tt0304141/reviews/?ref_=tt_ov_rt",  # Prisoner of Azkaban
    "https://www.imdb.com/title/tt0417741/reviews/?ref_=tt_ov_rt",  # Goblet of Fire
    "https://www.imdb.com/title/tt0373889/reviews/?ref_=tt_ov_rt",  # Order of the Phoenix
    "https://www.imdb.com/title/tt0417741/reviews/?ref_=tt_ov_rt",  # Half-Blood Prince
    "https://www.imdb.com/title/tt0926084/reviews/?ref_=tt_ov_rt",  # Deathly Hallows – Part 1
    "https://www.imdb.com/title/tt1201607/reviews/?ref_=tt_ov_rt"   # Deathly Hallows – Part 2
]

# Ensure the output directory exists
output_dir = './reviews'
os.makedirs(output_dir, exist_ok=True)

# Loop through each URL
for url in urls:
    response = requests.get(url)
    movie_page = BeautifulSoup(response.content, 'html.parser')
    
    review_tiles = movie_page.find_all('div', attrs={'class': 'review-container'})
    
    reviews = []
    for review_tile in review_tiles:
        review_div = review_tile.find('div', attrs={'class': 'content'})
        if review_div:
            # Define keywords and patterns to ignore
            ignore_patterns = [r'\d+ out of \d+ found this helpful',  # Pattern for helpfulness votes
                               r'Was this review helpful? Sign in to vote\.?',  # Pattern for helpfulness prompt
                               r'\b\d+\b']  # Pattern to match any standalone number
            
            review_text = review_div.get_text(separator=' ', strip=True)
            
            # Remove unwanted patterns using regex
            for pattern in ignore_patterns:
                review_text = re.sub(pattern, '', review_text, flags=re.IGNORECASE)
            
            # Clean up extra whitespace left after removal
            review_text = ' '.join(review_text.split())
            
            reviews.append(review_text)
    
    # Generate a unique file name based on the URL
    url_parts = url.split('/')
    movie_id = url_parts[4]  # Get the movie ID from the URL
    file_name = f'{movie_id}_reviews.txt'
    file_path = os.path.join(output_dir, file_name)
    
    # Write reviews to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        for review in reviews:
            file.write(f"{review}\n")
    
    print(f"Reviews from {url} have been written to {file_path}")
