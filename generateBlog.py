import openai
OPENAI_API_KEY = ''

# import openai
# import os

# # Safe handling of the API Key
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')  # Ensure you've set this environment variable

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Function to generate SEO-optimized content using OpenAI
def generate_seo_content(title, key_words, main_content, context):
    # Convert lists to string
    key_words_str = ", ".join(key_words)
    main_content_str = " ".join(main_content)
    
    # Define the prompt to generate an SEO-optimized title or description
    prompt = (f"Generate an SEO-optimized blog that helps these keywords '{key_words_str}' rank higher. "
              f"Here is the context about the product: {context},"
              f" Title: {title}, Key Words: {key_words_str}, "
              f"Article Bullet Points: {main_content_str},"
              f"the post body should be impressive, convincing with solid points to approve the bullet points")
    
    # Use the ChatCompletion endpoint
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # or "gpt-4" if available
        messages=[
            {"role": "system", "content": ("You are a SEO expert which help to generate blogs to help website "
                                          "on-page SEO according to the input. The output will be a JSON object "
                                          "which includes: name - the title; slug - title with '-' instead of spaces; "
                                          "post-body - blog content with HTML formatting; post-summary - 1 sentence to "
                                          "summarize the blog content. ")},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10000  # Adjust as needed based on expected output length
    )
    
    # Extract and return the generated SEO content
    return response.choices[0].message.content.strip()

# seo_output = generate_seo_content(title, key_word, main_content, context)
# print(seo_output)
