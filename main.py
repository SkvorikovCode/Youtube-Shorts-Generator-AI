from Components.YoutubeDownloader import download_youtube_video
from Components.Edit import extractAudio, crop_video
from Components.Transcription import transcribeAudio
from Components.LanguageTasks import GetHighlight
from Components.FaceCrop import crop_to_vertical, combine_videos

url = input("Enter YouTube video URL: ")
import time

Vid= download_youtube_video(url)
if Vid:
    Vid = Vid.replace(".webm", ".mp4")
    print(f"Downloaded video and audio files successfully! at {Vid}")

    start_time = time.time()
    Audio = extractAudio(Vid)
    end_time = time.time()
    print(f"extractAudio took {end_time - start_time:.2f} seconds")

    if Audio:

        start_time = time.time()
        transcriptions = transcribeAudio(Audio)
        end_time = time.time()
        print(f"transcribeAudio took {end_time - start_time:.2f} seconds")

        if len(transcriptions) > 0:
            TransText = ""

            for text, start, end in transcriptions:
                TransText += (f"{start} - {end}: {text}")

            start_time = time.time()
            highlight_result = GetHighlight(TransText)
            end_time = time.time()
            print(f"GetHighlight took {end_time - start_time:.2f} seconds")
            print(f"GetHighlight result: {highlight_result}")
            print(f"GetHighlight result type: {type(highlight_result)}")

            # Обработка результата GetHighlight
            start = 0
            stop = 0
            if highlight_result and isinstance(highlight_result, list) and len(highlight_result) > 0:
                # Если возвращается список с данными
                first_highlight = highlight_result[0]
                print(f"First highlight: {first_highlight}")
                start = int(float(first_highlight.get('start', 0)))
                stop = int(float(first_highlight.get('end', 0)))
            elif highlight_result and isinstance(highlight_result, dict):
                # Если возвращается словарь с highlights
                highlights = highlight_result.get('highlights', [])
                if highlights and len(highlights) > 0:
                    first_highlight = highlights[0]
                    start = first_highlight.get('start_time', 0)
                    stop = first_highlight.get('end_time', 0)

            if start != 0 and stop != 0:
                print(f"Start: {start} , End: {stop}")

                Output = "Out.mp4"

                start_time = time.time()
                crop_video(Vid, Output, start, stop)
                end_time = time.time()
                print(f"crop_video took {end_time - start_time:.2f} seconds")

                croped = "croped.mp4"

                start_time = time.time()
                crop_to_vertical("Out.mp4", croped)
                end_time = time.time()
                print(f"crop_to_vertical took {end_time - start_time:.2f} seconds")

                start_time = time.time()
                combine_videos("Out.mp4", croped, "Final.mp4")
                end_time = time.time()
                print(f"combine_videos took {end_time - start_time:.2f} seconds")
            else:
                print("Error in getting highlight")
        else:
            print("No transcriptions found")
    else:
        print("No audio file found")
else:
    print("Unable to Download the video")