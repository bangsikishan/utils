import logging

from pydub import AudioSegment


def convert_mp3_to_wav(mp3_file_path: str, wav_file_path: str) -> None:
    """
        Convert an MP3 audio file to WAV format.

        Args:
            mp3_file_path (str): The path to the MP3 audio file.
            wav_file_path (str): The destination path for the WAV file.

        Returns:
            None

        Example:
            convert_mp3_to_wav("audio.mp3", "output.wav")
    """
    try:
        sound = AudioSegment.from_mp3(mp3_file_path)

        sound.export(wav_file_path, format="wav")
    except FileNotFoundError:
        logging.error(f"[-] Audio file {mp3_file_path} not found!")
    except Exception as e:
        logging.error(f"[-] Error during conversion: {e}")
