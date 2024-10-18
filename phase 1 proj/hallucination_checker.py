import streamlit as st
import pandas as pd
import requests

# Title for the app
st.title("Hallucination Checker")

# Step 1: Upload the CSV file
uploaded_file = st.file_uploader("Upload conversation as CSV", type="csv")

# Initialize the session state for CSV processing status
if "csv_processed" not in st.session_state:
    st.session_state.csv_processed = False

# Check if the file has been uploaded
if uploaded_file is not None:
    st.write("File uploaded successfully.")
    
    # Read the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Step 2: Check if "conversation_id" column exists
    if "conversation_id" in df.columns:
        # Extract "conversation_id" as a list
        conversation_id_list = df["conversation_id"].tolist()

        # Step 3: Display a button to trigger CSV processing after the upload
        if st.button("Process CSV"):
            # Sending the uploaded CSV to the Flask API
            files = {'file': uploaded_file.getvalue()}
            
            # Call the Flask API to process the CSV file
            response = requests.post('http://127.0.0.1:5000/process_csv', files={'file': uploaded_file})
            
            # Handle the response from the Flask API
            if response.status_code == 200:
                st.success("CSV processed successfully!")
                st.session_state.csv_processed = True  # Set the session state to indicate CSV is processed
            else:
                st.error("Error processing the CSV file.")
        
        # Display the dropdown to select a conversation_id if CSV is processed
        if st.session_state.csv_processed:
            selected_conversation_id = st.selectbox("Select a Conversation ID",  df['conversation_id'].unique())

            # Step 4: Display the 'Find Conversation' button after selecting the conversation ID
            if st.button("Find Conversation"):
                # Call the API to fetch the conversation details
                response = requests.get(f'http://127.0.0.1:5000/conversation/{selected_conversation_id}')
                
                if response.status_code == 200:
                    # Parse the API response
                    result = response.json()

                    out = result.get("out", "No output found")

                    out_lines = out.splitlines()

                    # Check if the first line contains "YES" and set the color accordingly
                    if out_lines and "yes" in out_lines[0].lower():
                        st.markdown(f'<p style="color:red;">{out_lines[0]}</p>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<p style="color:green;">{out_lines[0]}</p>', unsafe_allow_html=True)



                    # Display the response from the API
                    st.write("\n".join(out_lines[1:]))

                    # Display the hallucination result as well
                    #st.write(f"Hallucination: {hallucination_result}")
                    
                    #st.write(f"Details: {out}")
                else:
                    st.error("Error fetching conversation details or conversation ID not found.")
    else:
        st.error("The uploaded CSV file does not contain a 'conversation_id' column.")
else:
    st.info("Please upload a CSV file to proceed.")
