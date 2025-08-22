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
            start , stop = GetHighlight(TransText)
            end_time = time.time()
            print(f"GetHighlight took {end_time - start_time:.2f} seconds")

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