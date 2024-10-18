from flask import Flask, request, jsonify
import os
import csv
import ollama

app = Flask(__name__)

# Ensure the 'conversations' folder exists
def create_conversations_folder():
    folder_path = os.path.join(os.getcwd(), "conversations")
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

# Function to process CSV and save conversations as text files
def csv_to_text_by_conversation_id(csv_file_path):
    try:
        folder_path = create_conversations_folder()  # Ensure folder exists

        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            last_conversation_id = None
            txtfile = None

            for row in reader:
                current_conversation_id = row['conversation_id']
                
                # When we encounter a new conversation_id, start a new file
                if current_conversation_id != last_conversation_id:
                    if txtfile:
                        txtfile.close()

                    # Save the file inside the 'conversations' folder
                    txtfile_path = os.path.join(folder_path, f"{current_conversation_id}.txt")
                    txtfile = open(txtfile_path, 'w', encoding='utf-8')

                # Write the row data into the text file
                txtfile.write(f"Speaker: {row['speaker']}\n")
                txtfile.write(f"Text: {row['text']}\n")
                txtfile.write(f"Summary A: {row['summary_a']}\n")
                txtfile.write(f"Response: {row['response']}\n")
                txtfile.write(f"Answer: {row['answer']}\n")
                txtfile.write("\n")

                last_conversation_id = current_conversation_id

            if txtfile:
                txtfile.close()

        return {"message": "File processed successfully"}, 200

    except UnicodeDecodeError as e:
        return {"error": str(e)}, 500
    

model = "llama3.2"  # Model updated to LLaMA 3.2

# Function to read the conversation details from the file
def read_conversation_from_file(conversation_id):
    try:
        # Construct the file path from conversation_id
        file_path = f"conversations/{conversation_id}.txt"
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None

# Flask route to handle the conversation ID request
@app.route('/conversation/<conversation_id>', methods=['GET'])
def process_conversation(conversation_id):
    # Read conversation details from the file based on the conversation_id
    conversation_details = read_conversation_from_file(conversation_id)
    
    if conversation_details is None:
        return jsonify({"error": "Conversation ID not found."}), 404

    # Construct the prompt with conversation details
    prompt = f"""
    I have conversation details in the following format:

    {conversation_details}

    Using this format, please read and understand the context of the entire conversation. 
    There will be only one summary for the whole conversation, which is already generated. 
    Based on your understanding of the conversation, compare it with Summary A (which is available only in the first row) and determine whether Summary A is hallucinated or not.

    Provide the output just with the following format (translate other language in conversation to English) :

    Hallucination : result(just  yes or no)
    \n
    Explanation : If hallucinated, explain the conversations line by where Summary A diverged from the actual context, or if not, explain why it is accurate.
    """

    # Running the chat with streaming enabled
    stream = ollama.chat(
        model=model,
        messages=[{'role': 'user', 'content': prompt}],
        stream=True  # Enable streaming for real-time output
    )

    # Capture the response from the LLaMA model
    
    
    out = ""  # To store the first line of the first chunk
   
    for chunk in stream:
        out += chunk['message']['content']
    print(out)
    # Return the response to the user
    return jsonify({"conversation_id": conversation_id, "out": out})

# Flask route to handle CSV file upload
@app.route('/process_csv', methods=['POST'])
def process_csv():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file temporarily to the server
    file_path = os.path.join(os.getcwd(), file.filename)
    file.save(file_path)
    
    # Call the function to process the CSV
    response = csv_to_text_by_conversation_id(file_path)
    
    # Clean up by deleting the uploaded CSV file
    os.remove(file_path)
    
    return jsonify(response)

# Start the Flask server
if __name__ == "__main__":
    app.run(debug=True)
