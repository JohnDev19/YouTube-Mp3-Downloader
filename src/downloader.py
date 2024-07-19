import yt_dlp
import logging
from .exceptions import DownloadError

logger = logging.getLogger(__name__)

class YoutubeDownloader:
    def __init__(self, output_path):
        self.output_path = output_path
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': self.output_path,
            'quiet': True,
            'no_warnings': True,
        }

    def download(self, url):
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                filename = ydl.prepare_filename(info)
                ydl.download([url])
            logger.info(f"Successfully downloaded: {filename}")
            return filename
        except Exception as e:
            logger.error(f"Failed to download {url}: {str(e)}")
            raise DownloadError(f"Failed to download {url}: {str(e)}")
