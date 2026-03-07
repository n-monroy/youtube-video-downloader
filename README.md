# YouTube Video Downloader

A simple Python script to download YouTube videos using [yt-dlp](https://github.com/yt-dlp/yt-dlp).

## Features

- Downloads videos up to 1080p (configurable)
- Automatically merges separate video and audio streams into a single mp4
- Displays video metadata (title, channel, duration, views, resolution) before downloading
- Console progress bar with speed and ETA
- Accepts a URL as a command-line argument or via the default in the script
- Embeds metadata tags into the downloaded file (requires ffmpeg)

## Prerequisites

- **Python 3.8+**
- **ffmpeg** (optional but recommended) — needed to merge high-res video+audio streams and embed metadata.
  Install on Windows:
  ```
  winget install ffmpeg
  ```
  On macOS: `brew install ffmpeg` · On Ubuntu/Debian: `sudo apt install ffmpeg`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/youtube-downloader.git
   cd youtube-downloader
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS / Linux
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Pass the YouTube URL as an argument:

```bash
python main.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Or edit the `default_url` variable inside `main.py` and run without arguments:

```bash
python main.py
```

Videos are saved to the `downloads/` folder in the project directory.

### Configuration

Inside `main.py` you can change:

| Variable       | Default  | Description                                       |
|----------------|----------|---------------------------------------------------|
| `default_url`  | —        | Fallback URL when no argument is provided         |
| `resolution`   | `"1080"` | Max resolution (`"1080"`, `"720"`, `"480"`, etc.) |

## Dependencies

- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) — YouTube video downloading

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
