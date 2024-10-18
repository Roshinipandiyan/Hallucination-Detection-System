import re
import emoji
import pandas as pd
from googletrans import Translator

# Function to clean and preprocess the conversation
def preprocess_conversation(conversation):
    # Step 1: Convert any emoji to text representation
    conversation = emoji.demojize(conversation)

    # Step 2: Remove structured patterns like {voice.ssn.digitsTranscribed:******}
    conversation = re.sub(r'{.*?}', '', conversation)

    # Step 3: Remove extraneous punctuation, unnecessary commas, and repeated symbols
    conversation = re.sub(r',+|\.\.\.|#+', '', conversation)
    
    # Step 4: Remove filler words (e.g., "um", "uh", etc.)
    fillers = ['um', 'uh', 'well', 'yeah', 'okay']
    for filler in fillers:
        conversation = re.sub(r'\b' + filler + r'\b', '', conversation, flags=re.IGNORECASE)
    
    # Step 5: Fix minor misspellings or unclear words
    conversation = conversation.replace('four 0z four', '404').replace("They're tiff a kit", "the certificate")
    
    # Step 6: Remove non-verbal utterances and unclear parts
    conversation = re.sub(r'\b(noise|incomprehensible|unclear)\b', '', conversation, flags=re.IGNORECASE)
    
    # Step 7: Remove extra whitespace
    conversation = re.sub(r'\s+', ' ', conversation).strip()
    
    return conversation

# Function to translate text to English
def translate_word(word, dest_language='en'):
    translator = Translator()
    
    # Check if the word is empty
    if not word:
        return ''
    
    try:
        # Automatically detect the source language
        detection = translator.detect(word)
        src_language = detection.lang
        i=+1
        print(i,src_language)

        # Translate the word
        translation = translator.translate(word, src=src_language, dest=dest_language)
        return translation.text
    except Exception as e:
        print(f"Translation error: {e}",word)
        return word  # Return original word in case of error

# Function to process CSV file
def process_csv(input_csv_file, output_csv_file):
    # Read input from CSV file
    df = pd.read_csv(input_csv_file)

    # Clean column names by stripping whitespace
    df.columns = df.columns.str.strip()

    # Print the column names to debug
    print("Columns in the CSV:", df.columns.tolist())

    # Assuming the CSV has a column named 'text'
    if 'Column5' not in df.columns:
        raise KeyError("Column 'text' not found in the CSV file.")
    
    df['cleaned_conversation'] = df['Column5'].apply(preprocess_conversation)
    df['translated_conversation'] = df['cleaned_conversation'].apply(translate_word)

    # Write the output to a new CSV file
    df.to_csv(output_csv_file, index=False)

# Define file paths
input_csv_file = 'input.csv'  # Replace with your input CSV file path
output_csv_file = 'output.csv'  # Output file path

# Process the CSV
process_csv(input_csv_file, output_csv_file)

print(f'Processed conversation saved to "{output_csv_file}".')
