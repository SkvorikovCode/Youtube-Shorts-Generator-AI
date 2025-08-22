# AI YouTube Shorts Generator

🎬 Автоматический генератор коротких видео из YouTube роликов с использованием ИИ

## Описание

Этот проект автоматически создает короткие вертикальные видео (Shorts) из длинных YouTube роликов, используя:
- Автоматическую транскрипцию речи
- ИИ-анализ для поиска лучших моментов
- Автоматическую обрезку и форматирование
- Детекцию лиц для оптимального кадрирования

## Возможности

✅ Загрузка видео с YouTube  
✅ Извлечение и транскрипция аудио  
✅ ИИ-анализ для поиска интересных моментов  
✅ Автоматическая обрезка видео  
✅ Конвертация в вертикальный формат  
✅ Детекция и центрирование лиц  
✅ Объединение финального видео  

## Технологии

- **Python 3.13**
- **OpenAI Whisper** - транскрипция речи
- **MoviePy** - обработка видео
- **OpenCV** - компьютерное зрение
- **PyTubeFix** - загрузка с YouTube
- **FFmpeg** - кодирование видео

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/SkvorikovCode/AI-Youtube-Shorts-Generator.git
cd AI-Youtube-Shorts-Generator
```

2. Создайте виртуальное окружение:
```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# или
.venv\Scripts\activate  # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Убедитесь, что FFmpeg установлен:
```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Windows
# Скачайте с https://ffmpeg.org/download.html
```

## Использование

1. Запустите основной скрипт:
```bash
python main.py
```

2. Введите URL YouTube видео когда будет запрошено

3. Выберите качество видео для загрузки

4. Дождитесь завершения обработки

5. Готовое видео будет сохранено как `Final.mp4`

## Структура проекта

```
AI-Youtube-Shorts-Generator/
├── Components/
│   ├── YoutubeDownloader.py    # Загрузка видео с YouTube
│   ├── Edit.py                 # Извлечение аудио и обрезка
│   ├── Transcription.py        # Транскрипция речи
│   ├── LanguageTasks.py        # ИИ-анализ текста
│   ├── FaceCrop.py            # Детекция лиц и кадрирование
│   ├── Speaker.py             # Детекция говорящего
│   └── SpeakerDetection.py    # Дополнительная детекция
├── models/                     # Модели для детекции лиц
├── videos/                     # Папка для загруженных видео
├── main.py                     # Основной скрипт
├── requirements.txt            # Зависимости Python
└── README.md                   # Документация
```

## Требования к системе

- **Python 3.9+**
- **FFmpeg**
- **4GB+ RAM** (для обработки видео)
- **Интернет-соединение** (для загрузки с YouTube)

## Поддерживаемые платформы

- ✅ macOS (включая Apple Silicon M1/M2)
- ✅ Linux (Ubuntu, Debian, CentOS)
- ✅ Windows 10/11

## Автор

👨‍💻 **Denis Skvorikov**  
🔗 GitHub: [@SkvorikovCode](https://github.com/SkvorikovCode)

## Лицензия

MIT License - см. файл [LICENSE](LICENSE) для подробностей.

## Вклад в проект

Приветствуются Pull Request'ы! Для крупных изменений сначала откройте Issue для обсуждения.

---

⭐ Если проект был полезен, поставьте звездочку!

*Создано в 2025 году*