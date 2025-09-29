# Spotify Playlist Time Machine

## Project Scope

This project was designed to automate the creation of Spotify playlists based on the Billboard Hot 100 chart for any given date. The goal was to scrape the Billboard website for the top 100 songs on a user-specified date and then search for those songs on Spotify, compiling them into a playlist for easy listening.

## Expectations

- Scrape Billboard Hot 100 song titles for a specific date.
- Search for each song on Spotify and collect their track URIs.
- Create a new Spotify playlist (or update an existing one) with these tracks.
- Handle authentication securely using environment variables.
- Ensure the process is robust and repeatable.

## Requirements

- Python 3.8+
- [Spotipy](https://spotipy.readthedocs.io/en/2.23.0/) for Spotify API access
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping
- [python-dotenv](https://pypi.org/project/python-dotenv/) for environment variable management
- Spotify Developer account and app credentials
- Internet access

## How We Started

We began by exploring the Billboard website’s structure to identify how song titles are presented. Next, we set up Spotify API credentials and learned how to authenticate using Spotipy. The initial script focused on scraping song titles and manually searching for them on Spotify.

## Trials and Errors

- **Scraping Issues:** The Billboard page contains extra headings and metadata, so our initial selector grabbed hundreds of irrelevant titles. We refined our BeautifulSoup logic to filter only actual song titles.
- **Spotify Authentication:** We encountered errors with environment variables not loading, which was solved by using `python-dotenv`.
- **Playlist Creation:** The script was creating duplicate playlists on each run. We added logic to check for existing playlists and reuse them.
- **API Changes:** Spotipy’s API changed, requiring us to switch from `user_playlist_add_tracks` to `playlist_add_items`.

## Overcoming Obstacles

- Improved HTML parsing to accurately extract song titles.
- Used environment variables for secure credential management.
- Implemented playlist existence checks to avoid duplicates.
- Added progress and debug print statements to monitor scraping and searching.

## Technology Used

- **Python**: Main programming language
- **Spotipy**: Spotify Web API wrapper
- **BeautifulSoup**: HTML parsing and scraping
- **Requests**: HTTP requests for web scraping
- **python-dotenv**: Loads environment variables from `.env` files

## Why Build This Project?

Music is a powerful way to revisit memories. This project lets users "travel back in time" by instantly recreating the soundtrack of any week in history, making nostalgia accessible and shareable.

## Real World Use Cases

- Personal nostalgia playlists
- DJs or radio hosts curating retro sets
- Music historians or researchers
- Social media challenges ("What was #1 on your birthday?")
- Automated playlist generation for events

## Future Improvements

- Add support for other charts (e.g., Billboard 200, genre charts)
- Improve song matching accuracy (use artist names, fuzzy search)
- Handle missing tracks gracefully (log/report)
- Add a web interface for easier use
- Support batch playlist creation for multiple dates

## How to Build and Run

1. **Clone the repository**  
   `git clone https://github.com/martialchess/spotify-billboard-time-machine`

2. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

3. **Set up Spotify credentials**  
   - Create a `.env` file with:
     ```
     SPOTIPY_CLIENT_ID=your_client_id
     SPOTIPY_CLIENT_SECRET=your_client_secret
     ```

4. **Run the script**  
   ```
   python main.py
   ```
   - Enter a date in `YYYY-MM-DD` format when prompted.

5. **Check your Spotify account**  
   - The playlist will appear in your account with the Billboard Hot 100 songs for the selected date.

---

Feel free to contribute or suggest improvements!