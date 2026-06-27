import os
import time

AUDIO_DIR = "audio"


def cleanup_old_files(max_age=3600):

    current_time = time.time()

    for file in os.listdir(AUDIO_DIR):

        filepath = os.path.join(
            AUDIO_DIR,
            file
        )

        if os.path.isfile(filepath):

            file_age = (
                current_time -
                os.path.getmtime(filepath)
            )

            if file_age > max_age:

                os.remove(filepath)
