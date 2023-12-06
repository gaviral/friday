# Friday

Voice-driven assistant

## Screenshots

<img width="1770" alt="Screen Shot 2021-02-02 at 12 28 00 AM" src="https://user-images.githubusercontent.com/12901566/106572754-b0baf000-64ed-11eb-862b-41638a6024c3.png">

## Setup

[reference](https://towardsdatascience.com/building-a-simple-voice-assistant-for-your-mac-in-python-62247543b626)

1. Install the following softwares/packages:

```zsh
brew install portaudio      # access to microphone
brew install elasticsearch  # query-query matching and return a response

python3 -m pip install SpeechRecognition
python3 -m pip install pyaudio
python3 -m pip install elasticsearch

```

2. Download [ChromeDriver](https://chromedriver.chromium.org/downloads) for selenium to work.
3. Include the ChromeDriver location in your PATH environment variable.
    1. One option is to add `export PATH="path/to/chromedriver:$PATH"` in your `~/.zshrc` file.
4. Run ElasticSearch server by simply entering: `elasticsearch` in your terminal.
5. Wait for Friday to start talking.
6. Speak any of the commands below.

---

## Commands

| Command               | Example      | Details                                  |
| --------------------- | ------------ | ---------------------------------------- |
| Open << app >>          | Open Spotify | Access to microphone                     |
| anything else         | What's life? | Google search                            |

## Tech

| Tech               | Purpose                                    |
| ------------------ | ------------------------------------------ |
| portaudio          | Access to microphone                        |
| elasticsearch      | query-query matching and return a response |
| pip                | python package management                  |
| speech_recognition | speech to text                             |
| pyaudio            | connecting to mac's microphone             |

## Notes

1. The SpeechRecognition library acts as a wrapper for several popular speech APIs and is thus extremely flexible. One
   of these — the Google Web Speech API — supports a default API key that is hard-coded into the SpeechRecognition
   library.
   
## Warnings

1. elasticsearch has been deprecated because it is switching to an incompatible license!
