import speech_recognition as sr


def extract_text_from_wav(wav_file_path: str) -> str:
    """
        Extract text from a WAV file using Google Speech Recognition.

        Args:
            wav_file_path (str): The path to the WAV file.

        Returns:
            str: The extracted text from the WAV file.

        Raises:
            FileNotFoundError: If the input WAV file is not found.
            RuntimeWarning: If ffmpeg or avconv is not found.
            sr.UnknownValueError: If Google Speech Recognition could not understand the audio.
            sr.RequestError: If Google Speech Recognition service could not be reached.

        Example:
            extract_text_from_wav("audio.wav")
    """
    try:
        recognizer: sr.Recognizer = sr.Recognizer()

        with sr.AudioFile(wav_file_path) as source:
            audio: sr.AudioData = recognizer.record(source)
            return recognizer.recognize_google(audio)
    except FileNotFoundError as e:
        print(f"[-] Error: {e}")
    except RuntimeWarning as e:
        print(f"[-] Error: {e}")
    except sr.UnknownValueError as e:
        print(f"[-] Error: Google Speech Recognition could not understand the audio: {e}")
    except sr.RequestError as e:
        print(f"[-] Error: Google Speech Recognition service could not be reached: {e}")
