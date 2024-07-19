from pydub import AudioSegment
import os
import logging
from .exceptions import ConversionError

logger = logging.getLogger(__name__)

class AudioConverter:
    @staticmethod
    def convert_to_mp3(input_file, output_file, bitrate="192k"):
        try:
            audio = AudioSegment.from_file(input_file)
            audio.export(output_file, format="mp3", bitrate=bitrate)
            logger.info(f"Successfully converted to MP3: {output_file}")
        except Exception as e:
            logger.error(f"Failed to convert {input_file} to MP3: {str(e)}")
            raise ConversionError(f"Failed to convert {input_file} to MP3: {str(e)}")

    @staticmethod
    def cleanup(file_path):
        try:
            os.remove(file_path)
            logger.info(f"Cleaned up temporary file: {file_path}")
        except Exception as e:
            logger.warning(f"Failed to clean up {file_path}: {str(e)}")
