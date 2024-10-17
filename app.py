import streamlit as st
import pandas as pd

# Function to display conversation summary
def display_summary(df, conversation_id):
    conversation = df[df['conversation_id'] == conversation_id]
    if not conversation.empty:
        st.write("### Conversation Summary")
        st.write(conversation['summary_a'].values[0])
    else:
        st.write("Conversation not found")

# Streamlit UI
st.title("Hallucination Detection")
st.write("Upload a CSV file to begin:")

# File uploader for CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read CSV into DataFrame, skipping the first row
    df = pd.read_csv(uploaded_file, skiprows=1)

    # Rename columns based on the dataset structure
    df.columns = ['conversation_id', 'speaker', 'text', 'summary_a', 'response', 'answer']

    # Ensure the necessary columns are present
    if set(['conversation_id', 'speaker', 'text', 'summary_a', 'response', 'answer']).issubset(df.columns):
        st.write("### Select a Conversation ID")
        
        # Dropdown to select a conversation ID
        conversation_id = st.selectbox("Select a conversation", df['conversation_id'].unique())

        # Display the summary for the selected conversation
        if st.button("Show Summary"):
            display_summary(df, conversation_id)
    else:
        st.error("The uploaded CSV does not have the required columns.")
