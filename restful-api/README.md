# JSONPlaceholder API Interaction

This project demonstrates how to interact with the JSONPlaceholder API using Python's requests library.

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install requests directly:
```bash
pip install requests
```

## Usage

Run the main script:
```bash
python3 main_02_requests.py
```

## What it does

1. **fetch_and_print_posts()**: Fetches all posts from JSONPlaceholder API and prints their titles
2. **fetch_and_save_posts()**: Fetches all posts and saves them to a CSV file called `posts.csv`

## Expected Output

- Status code: 200
- List of post titles printed to console
- CSV file `posts.csv` created with columns: id, title, body

## Files

- `task_02_requests.py`: Main module with the API interaction functions
- `main_02_requests.py`: Script to run both functions
- `requirements.txt`: Python dependencies
- `posts.csv`: Generated CSV file with post data 