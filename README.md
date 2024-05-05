# YouTube Video Downloader

This is a simple Python project that allows you to download videos from YouTube.

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Create a virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (Unix/MacOS) or `.\env\Scripts\activate` (Windows)
5. Install the required packages: `pip install -r requirements.txt`

## Usage

1. Set the `path` variable in the `main.py` script to the directory where you want to save the downloaded videos.
2. Set the `url` variable in the `main.py` script to the URL of the YouTube video you want to download.
3. Run the `main.py` script with the URL of the YouTube video you want to download as an argument: `python main.py`
4. The video will be downloaded to the directory you specified.

## Dependencies

This project uses the following Python libraries:

- `pytube`: for downloading YouTube videos
- `humanize`: for formatting file sizes and durations

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
