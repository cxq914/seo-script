import requests
import hashlib
import json


def get_image_md5(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        md5_hash = hashlib.md5()
        md5_hash.update(response.content)
        return md5_hash.hexdigest()
    except requests.RequestException as e:
        print(f"Error fetching image: {e}")
        return None

def get_image(access_key, key_word):
    url = 'https://api.unsplash.com/photos/random'
    params = {'client_id': access_key, 'query': key_word, 'orientation': 'landscape', 'count': 1}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if data and isinstance(data, list) and data:
            photo = data[0]
            return (photo['id'], photo['urls']['full'], photo['urls']['thumb'])
        else:
            return (None, None, None)
    except requests.RequestException as e:
        print(f"Error getting image from Unsplash: {e}")
        return (None, None, None)

def post_image_to_webflow(file_id, file_url, headers, url):
    payload = {"fileName": f"{file_id}.jpg", "fileHash": file_url}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error posting image to Webflow: {e}")
        return None

def get_images_info(access_key, key_word):
    image_id, image_url, image_thumb = get_image(access_key, key_word)
    if image_url and image_thumb:
        md5_hash_main = get_image_md5(image_url)
        md5_hash_thumb = get_image_md5(image_thumb)
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "authorization": ""  # Replace with your token
        }
        url = "https://api.webflow.com/v2/sites/65701e7563fb53dc3a790f0d/assets"
        main_image_response = post_image_to_webflow(image_id, md5_hash_main, headers, url)
        thumb_image_response = post_image_to_webflow(image_id, md5_hash_thumb, headers, url)

        return {
            "main-image": {
                "fileId": main_image_response.get('id', ''),
                "url": main_image_response.get('hostedUrl', ''),
                "alt": key_word
            },
            "thumbnail-image": {
                "fileId": thumb_image_response.get('id', ''),
                "url": thumb_image_response.get('hostedUrl', ''),
                "alt": key_word
            }
        }

# Example of how to call the function
# result = get_images_info(access_key, key_word)
# print(json.dumps(result, indent=4))  # Pretty print the JSON result
