import os
import subprocess

import speech_recognition as sr
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


def apps_setup(_es):
    apps_directory = '/Applications'
    records = []
    apps = os.listdir(apps_directory)
    for app in apps:
        record = {'voice_command': 'open ' + app.split('.app')[0],
                  'sys_command': 'open ' + apps_directory + '/%s' % app.replace(' ', '\ ')}
        records.append(record)

    bulk(_es, records, index='voice_assistant', doc_type='text', raise_on_error=True)


def search_es(_es, query):
    res = _es.search(index="voice_assistant", doc_type="text", body={
        "query": {
            "match": {
                "voice_command": {
                    "query": query,
                    "fuzziness": 2
                }
            }
        },
    })
    return res['hits']['hits'][0]['_source']['sys_command']


def say(text):
    print(text)
    subprocess.call(['say', text])


def listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        _transcript = recognizer.recognize_google(audio)
        say(f"You said: {_transcript}")
        return _transcript


def run_command(_es, _transcript):
    sys_command = search_es(_es, _transcript)

    if sys_command.split(" ")[0] in ["open"]:
        say(f"Opening {_transcript.split(' ', 1)[1]}")
        os.system(sys_command)


if __name__ == '__main__':
    es = Elasticsearch(['localhost:9200'])

    apps_setup(es)

    say("How can I help you?")

    transcript = listen()
    run_command(es, transcript)
