from generateBlog import generate_seo_content
from getImage import get_images_info
import json
import requests

access_key = ''  # Remember to replace with your actual Unsplash access key


context = ("context: Qquest is an AI analytics tool. Qquest is designed to transform the way "
           "individuals interact with their data and files. Our app utilizes the latest generative AI "
           "to simplify and enrich data querying, converting complex interactions into straightforward, "
           "conversational exchanges. This innovation is not just about accessing data; it's about enhancing "
           "the efficiency of information utilization in both your work and personal life!")
key_word = ["business analytics", "ai", "data quality", "data analytics","data engineering","data privacy and compliance"]
title = 'Customer Data Privacy and Compliance'
main_content = ['1. when we talk about ai, we are worried about data privacy and compliance; 2. what is data privacy and compliance; 3. how to improve the data privacy and compliance']

# category = '66e32fbaf067b773fe87bae8' #business analytics
# category = '66e32fbaf067b773fe87baeb' # data engineering
category = '66e32fbaf067b773fe87bae6' # AI webflow only

print("here it is:")
seo_output = generate_seo_content(title, key_word, main_content, context)
# Assuming seo_output is a JSON string
# print("seo_output content:", repr(seo_output))  # This will show exactly what seo_output contains

# Strip out the Markdown code block syntax
cleaned_output = seo_output.strip('`')
cleaned_output = cleaned_output.replace("json\n", "")  # Remove the 'json' keyword and the newline after it

# Debug print to verify the cleaned content
print(cleaned_output)

### Step 2: Convert to JSON
try:
    seo_output_dict = json.loads(cleaned_output)
    print("Converted to dictionary.")
except json.JSONDecodeError as e:
    print("Error parsing JSON:", e)

image_info = get_images_info(access_key, key_word[0])
print(type(image_info))

combined_data = {
    "isArchived": False,
    "isDraft": False,
    "fieldData": 
    {
        "featured": True,
        "color": "#FF9800",
        "name": seo_output_dict["name"],
        "slug": seo_output_dict["slug"],
        "post-body": seo_output_dict["post-body"],
        "post-summary": seo_output_dict["post-summary"],
        "main-image": {
            "fileId": image_info['main-image']['fileId'],
            "url": image_info['main-image']['url'],
            "alt": image_info['main-image']['alt']
        },
        "thumbnail-image": {
            "fileId": image_info['thumbnail-image']['fileId'],
            "url": image_info['thumbnail-image']['url'],
            "alt": image_info['thumbnail-image']['alt']
        },
        "category": category
    }
}

print(combined_data)

url = "https://api.webflow.com/v2/collections/66e21762d7f89de0a33047c4/items"


headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": ""  # Replace with your token
}

response = requests.post(url, json=combined_data, headers=headers)

print(response.text)



