# DSC495 Project — Looking at word frequencies across subreddits

## Running the code

### `lookup.py`

This script will extract all comments from the top 100 posts for provided subreddits. The results will be stored in the `comments` directory.

Depending on the amount of comments in each subreddit, this script will take a long time to run, because of reddit's rate limiting.

1. Copy `praw.ini.blueprint` to `praw.ini`
2. Replace the `client_id` and `client_secret` with values obtained from your account ([instructions](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps))
3. Install [PRAW](https://praw.readthedocs.io/en/stable/) with `pip3 install praw`
4. Run the code with `python3 lookup.py`

### `calculate_freqs.py`

This script will extract the frequencies of tokens from the files generated with the script above. Uses the `comments` directory as input and the `freqs` directory as output (with one subdirectory for each input).

- Straight frequencies are just a straight counter of the words.
- Weighted frequencies are weighted by the `score` that reddit has for each comment (which is basically upvotes–downvotes). So words appearing in comments with a lot upvotes are therefore higher scored.

1. Install the libraries: `pip3 install nltk contractions`
2. Run the script above
3. Run the code with `python3 calculate_freqs.py`

### `plots.py`

This script takes the output of `lookup.py` and plots the number of comments and the score of each post in each subreddit.

1. Install the libraries: `pip3 install matplotlib`
2. Run `lookup.py` (instructions see above)
3. Run the code with `python3 plots.py`