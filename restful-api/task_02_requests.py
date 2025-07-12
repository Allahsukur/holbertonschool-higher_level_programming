#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints their titles
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post['title'])
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
            
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")


def fetch_and_save_posts():
    """
    Fetches all posts from JSONPlaceholder and saves them to a CSV file
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            posts = response.json()
            
            # Structure data into list of dictionaries
            structured_posts = []
            for post in posts:
                structured_posts.append({
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
                })
            
            # Write to CSV file
            with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for post in structured_posts:
                    writer.writerow(post)
                    
            print(f"Successfully saved {len(structured_posts)} posts to posts.csv")
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")
            
    except requests.RequestException as e:
        print(f"Error fetching posts: {e}")
    except IOError as e:
        print(f"Error writing to CSV file: {e}") 