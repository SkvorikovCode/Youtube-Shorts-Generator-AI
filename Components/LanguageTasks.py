from g4f.client import Client
import json
import os
import warnings

# Подавляем предупреждения и блокируем веб-запросы
warnings.filterwarnings("ignore")
os.environ['PYTHONHTTPSVERIFY'] = '0'
os.environ['REQUESTS_CA_BUNDLE'] = ''
os.environ['SSL_VERIFY'] = 'False'
os.environ['NO_PROXY'] = '*'
os.environ['DISABLE_WEB_BROWSER'] = '1'

# Блокируем открытие браузера
try:
    import webbrowser
    webbrowser.open = lambda *args, **kwargs: None
except ImportError:
    pass


# Function to extract start and end times
def extract_times(json_string):
    try:
        # Parse the JSON string
        data = json.loads(json_string)

        # Extract start and end times as floats
        start_time = float(data[0]["start"])
        end_time = float(data[0]["end"])

        # Convert to integers
        start_time_int = int(start_time)
        end_time_int = int(end_time)
        return start_time_int, end_time_int
    except Exception as e:
        print(f"Error in extract_times: {e}")
        return 0, 0


system = """

Baised on the Transcription user provides with start and end, Highilight the main parts in less then 1 min which can be directly converted into a short. highlight it such that its intresting and also keep the time staps for the clip to start and end. only select a continues Part of the video

Follow this Format and return in valid json 
[{
start: "Start time of the clip",
content: "Highlight Text",
end: "End Time for the highlighted clip"
}]
it should be one continues clip as it will then be cut from the video and uploaded as a tiktok video. so only have one start, end and content

Dont say anything else, just return Proper Json. no explanation etc


IF YOU DONT HAVE ONE start AND end WHICH IS FOR THE LENGTH OF THE ENTIRE HIGHLIGHT, THEN 10 KITTENS WILL DIE, I WILL DO JSON['start'] AND IF IT DOESNT WORK THEN...
"""

User = """
Any Example
"""


def GetHighlight(Transcription):
    print("Getting Highlight from Transcription ")
    try:
        # Создаем клиент с максимальной изоляцией
        client = Client()
        
        # Используем локальную модель без веб-поиска
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": Transcription},
            ],
            stream=False
        )

        json_string = response.choices[0].message.content
        json_string = json_string.replace("json", "")
        json_string = json_string.replace("```", "")
        
        try:
            # Попытка парсинга JSON
            highlights_data = json.loads(json_string)
            return highlights_data
        except json.JSONDecodeError:
            # Если JSON не парсится, используем старый метод
            print("Fallback to extract_times method")
            Start, End = extract_times(json_string)
            if Start == End:
                Ask = input("Error - Get Highlights again (y/n) -> ").lower()
                if Ask == "y":
                    return GetHighlight(Transcription)
            return {"highlights": [{"start_time": Start, "end_time": End, "description": "Extracted highlight"}]}
            
    except Exception as e:
        print(f"Error in GetHighlight: {e}")
        return {"highlights": [{"start_time": 0, "end_time": 0, "description": "Error occurred"}]}


if __name__ == "__main__":
    print(GetHighlight(User))
