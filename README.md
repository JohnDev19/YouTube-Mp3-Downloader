# YouTube-Mp3-Downloader

This project allows you to download audio from YouTube videos and convert them to MP3 format.

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Ensure you have FFmpeg installed on your system

## Usage

Run the main script:

```
python main.py
```

Enter the YouTube URL when prompted. The audio will be downloaded and converted to MP3 format in the `downloads` directory.

## Configuration

You can modify the settings in `config/settings.py` to change download directories, logging configuration, etc.

## File structure:
```
YouTube-Mp3-Downloader/
│
├── src/
│   ├── __init__.py
│   ├── downloader.py
│   ├── converter.py
│   ├── utils.py
│   └── exceptions.py
│
├── config/
│   └── settings.py
│
├── logs/
│   └── .gitkeep
│
├── main.py
├── requirements.txt
└── README.md
```


## License

This project is licensed under the MIT License.
