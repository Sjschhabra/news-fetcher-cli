# news-fetcher-cli

A Python command-line utility that allows users to fetch and display news articles based on specific keywords using the News API. The script provides a user-friendly interface for querying news and reading articles.

## Features

- **Keyword-Based Search**: Users can input keywords to fetch related news articles.
- **Dynamic Loading**: Articles are loaded in batches, allowing users to view more articles interactively.
- **User-Friendly Interface**: The command line interface displays article titles, contents, and URLs in a colored format for better visibility.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sjschhabra/news-fetcher-cli.git
   ```

2. Navigate to the project directory:

   ```bash
   cd news-fetcher-cli
   ```

3. Ensure you have Python 3.x installed on your system.

4. Install required packages:

   ```bash
   pip install requests colorama
   ```

## Usage

1. Run the script:

   ```bash
   python news-fetcher.py
   ```

2. Enter a keyword to search for news articles. You can exit the program by typing `-e`.

3. Follow the prompts to view articles, and choose to see more topics if desired.

### Example

```bash
$ python news-fetcher.py

What News Are You Interested In? (-e:exit): technology
1. Title: New advancements in AI
   Content: Artificial Intelligence (AI) has made significant progress...
   (*--URL--*: https://example.com/news/new-advancements-in-ai)

--------------------
Do you want to see more topics? (y=yes, else it will exit): y

What News Are You Interested In? (-e:exit): -e
```
