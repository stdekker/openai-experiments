import openai
from goose3 import Goose

openai.api_key = "your-key-here"

def get_main_content(url):
    # Configure Goose
    g = Goose()

    # Extract the main content using Goose
    article = g.extract(url)

     # Get the article's main text and title
    main_content = article.cleaned_text
    title = article.title

    # Combine the title and main content into a single string
    combined_content = f"{title}\n\n{main_content}"

    return combined_content

def main():
    url = input("Enter the URL of the website: ")
    try:
        text_clean = get_main_content(url)
        
        # Check if the main content is empty
        if not text_clean.strip():
            print("There is no extracted text")
        else:
            # print (text_clean)
            prompt = f"Make a short Dutch tweet of the following text: \n{text_clean}\n"

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=280,  # Adjust the number of tokens according to the desired summary length
                n=1,
                stop=None,
                temperature=0.3,  # Adjust the temperature to control the randomness of the output. Lower values make the output more focused and deterministic
            )
            
            print("\nTry this Tweet:")
            print(response.choices[0].text.strip())

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
