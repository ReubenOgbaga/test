from transformers import pipeline
import os
import requests
from PIL import Image

def image2text(image_path):
    image_to_text = pipeline(
        'image-to-text',
        model='Salesforce/blip-image-captioning-large')
    text=image_to_text(image_path)[0]['generated_text']
    return text

scenario = image2text()


def text2story(text):
  # Load the text generation model
  generator = pipeline('text-generation', model='gpt2')
  # Generate a story based on the provided text
  prompt = f"""Tell a short story in no more than 100 words about the following scenario {scenario} """
  story = generator(text, max_length=100, num_return_sequences=1)[0]['generated_text']
  if story.startswith(text):
    story = story.replace(text, "")
  if story.startswith(text):
     story = story[len(text):].strip()
  return story


story = text2story(scenario)



HUGGINGFACEHUB_API_TOKEN="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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN
def text2audio(story):
  API_URL="https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
  headers={"Authorization":f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
  payload = {"inputs": story}
  response = requests.post(API_URL, headers=headers, json=payload)
  if response.status_code == 200:
    with open("output.flac", "wb") as file:
      file.write(response.content)
    print("Audio file saved successfully!")
  else:
    print(f"Request failed with status code {response.status_code}")
print(text2audio(story))
