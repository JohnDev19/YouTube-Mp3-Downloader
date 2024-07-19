import os
import logging.config
from src.downloader import YoutubeDownloader
from src.converter import AudioConverter
from src.utils import sanitize_filename, format_file_size
from src.exceptions import DownloadError, ConversionError
from config.settings import DOWNLOAD_DIR, LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def main():
    try:
        url = input("Enter YouTube video URL: ")
        output_template = os.path.join(DOWNLOAD_DIR, '%(title)s.%(ext)s')

        downloader = YoutubeDownloader(output_template)
        logger.info(f"Downloading audio from: {url}")
        downloaded_file = downloader.download(url)

        mp3_file = os.path.splitext(downloaded_file)[0] + '.mp3'
        sanitized_mp3_file = os.path.join(DOWNLOAD_DIR, sanitize_filename(os.path.basename(mp3_file)))

        converter = AudioConverter()
        logger.info(f"Converting {downloaded_file} to MP3")
        converter.convert_to_mp3(downloaded_file, sanitized_mp3_file)

        file_size = os.path.getsize(sanitized_mp3_file)
        logger.info(f"MP3 extracted and saved as: {sanitized_mp3_file} (Size: {format_file_size(file_size)})")

        if os.path.splitext(downloaded_file)[1].lower() != '.mp3':
            converter.cleanup(downloaded_file)

    except (DownloadError, ConversionError) as e:
        logger.error(str(e))
    except Exception as e:
        logger.exception("An unexpected error occurred")

if __name__ == "__main__":
    main()
