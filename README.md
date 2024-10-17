# Hallucination-Detection-System
This project implements a hallucination detection system for conversation data, designed to identify whether a conversation contains hallucinations (misleading or incorrect information). The system allows users to upload a CSV file containing conversation details and then provides an interface to explore the conversations and their summaries.

# Key Features
CSV File Upload: Users can upload conversation data in CSV format. The expected CSV structure includes the following columns:
        conversation_id: A unique ID for each conversation.
        speaker: The individual speaking in the conversation (e.g., agent, customer).
        text: The content of the conversation.
        summary_a: A summary of the conversation.
        response: The response to the conversation.
        answer: The answer related to the conversation.
Interactive UI: Once the CSV is uploaded, the system displays all conversation IDs in a dropdown list. Users can select a conversation ID to view its corresponding summary.
Hallucination Detection: The backend logic detects whether the conversation includes any hallucination by analyzing the summary and conversation content.




