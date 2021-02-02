# friday

assistant

## Setup

[reference](https://towardsdatascience.com/building-a-simple-voice-assistant-for-your-mac-in-python-62247543b626)

1. install the following softwares/packages
```zsh
brew install portaudio      # access to microphone
brew install elasticsearch  # query-query matching and return a response

python3 -m pip install SpeechRecognition
python3 -m pip install pyaudio
python3 -m pip install elasticsearch

```
2. Run ElasticSearch server by simply entering: `elasticsearch` in your terminal.

---

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
