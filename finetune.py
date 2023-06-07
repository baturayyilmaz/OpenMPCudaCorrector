import requests
import openai
from pprint import pprint
import subprocess
import argparse


# def prepareData():
#     subprocess.run('openai tools fine_tunes.prepare_data --file data01.jsonl --quiet'.split())
#     # --quiet accepts everything that open ai asks.

# def fineTuneModel(model="davinci"):
#     ## Start fine-tuning
#     subprocess.run(f'openai api fine_tunes.create --training_file prepared_data_prepared.jsonl --model {model} --suffix "SuperHero"'.split())

def fineTuneModel(jsonlFileName):
    # jsonlFileName = output file created after running the command mentioned above
    # RUN PREPARE JSONL SCRIPT BEFORE YOU RUN THIS SCRIPT (So, that openai can make adjustments on data!)
    open_ai_api_key="enter your OPENAI-API-KEY"
    openai.api_key=open_ai_api_key

    upload_response = openai.File.create(file=open(jsonlFileName, "rb"), purpose='fine-tune')
    print(f"Upload Response: {upload_response}")

    file_id = upload_response.id
    fine_tune_response = openai.FineTune.create(training_file=file_id, model="davinci") # default model is Curie
    print(f"Fine Tune Response: {fine_tune_response}")
    # fine tune is started. You can check fine tune status from command line.


def checkFineTuningStatus(fine_tune_response):
    fine_tune_events = openai.FineTune.list_events(id=fine_tune_response.id) # get a list of all the fine-tuning events
    print(fine_tune_events)
    retrieve_response = openai.FineTune.retrieve(id=fine_tune_response.id) # get an object with the fine-tuning job data
    print(retrieve_response)


def sendPrompt():
    prompt=""
    with open("prompt01.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            prompt += line[:-1].strip() + "$<n>$"
    prompt+="$<n>$ ->"
    print(prompt)
    #openai.Completion.create(model="davinci:ft-personal:codegenerate-2023-04-27-16-31-10", prompt=YOUR_PROMPT)

def decodeCompletion():
    decodedOutput=""
    with open("completion01.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            decodedOutput += line.strip().replace("$<n>$", "\n")
    print(decodedOutput)
    #openai.Completion.create(model="davinci:ft-personal:codegenerate-2023-04-27-16-31-10", prompt=YOUR_PROMPT)


if __name__ == "__main__":
    #fineTuneModel("jsonlFiles/data_classification.jsonl") # model oluşuyor ama sonunda suffix yok
    #sendPrompt()
    decodeCompletion()
    pass

