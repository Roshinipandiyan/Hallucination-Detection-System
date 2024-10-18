# # import torch
# # from sentence_transformers import SentenceTransformer, util

# # # Load a pre-trained model for embeddings
# # model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # A smaller model for sentence embeddings

# # # Function to calculate cosine similarity
# # def calculate_similarity(conversation_sentences, summary_sentences):
# #     # Encode the sentences to get their embeddings
# #     conversation_embeddings = model.encode(conversation_sentences, convert_to_tensor=True)
# #     summary_embeddings = model.encode(summary_sentences, convert_to_tensor=True)

# #     # Calculate cosine similarities between the summary and conversation
# #     similarity_matrix = util.pytorch_cos_sim(summary_embeddings, conversation_embeddings)

# #     # For each summary sentence, find the highest similarity with any conversation sentence
# #     max_similarities = torch.max(similarity_matrix, dim=1)[0]
    
# #     return max_similarities

# # # Function to detect hallucinations
# # def detect_hallucinations(conversation_text, summary_text, threshold=0.7):
# #     # Split conversation and summary into sentences
# #     conversation_sentences = [sent.strip() for sent in conversation_text.split('.') if sent.strip()]
# #     summary_sentences = [sent.strip() for sent in summary_text.split('.') if sent.strip()]

# #     # Calculate similarity between conversation and summary
# #     similarities = calculate_similarity(conversation_sentences, summary_sentences)

# #     # Identify hallucinations (where similarity is below the threshold)
# #     hallucinations = [summary_sentences[i] for i in range(len(similarities)) if similarities[i] < threshold]

# #     # Calculate hallucination percentage
# #     hallucination_percentage = len(hallucinations) / len(summary_sentences) * 100

# #     return hallucinations, hallucination_percentage

# # # Sample conversation and summary
# # conversation_text = """
# # I need to cancel my cousin's appointment
# # vSure, I can help you with that. What's the appointment date?
# # It's on the 23rd of this month
# # Got it. The appointment has been canceled
# # """

# # summary_text = """
# # The customer called to reschedule their cousin's appointment. The agent helped them with this"""
# # # Detect hallucinations in the summary
# # hallucinations, hallucination_percentage = detect_hallucinations(conversation_text, summary_text)

# # # Print results
# # print("Hallucinations:", hallucinations)
# # print(f"Hallucination Percentage: {hallucination_percentage:.2f}%")

# import torch
# from sentence_transformers import SentenceTransformer, util

# # Load a pre-trained model for embeddings
# model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # A smaller model for sentence embeddings

# # Function to calculate cosine similarity
# def calculate_similarity(conversation_sentences, summary_sentences):
#     # Encode the sentences to get their embeddings
#     conversation_embeddings = model.encode(conversation_sentences, convert_to_tensor=True)
#     summary_embeddings = model.encode(summary_sentences, convert_to_tensor=True)

#     # Calculate cosine similarities between the summary and conversation
#     similarity_matrix = util.pytorch_cos_sim(summary_embeddings, conversation_embeddings)

#     # For each summary sentence, find the highest similarity with any conversation sentence
#     max_similarities, closest_indices = torch.max(similarity_matrix, dim=1)
    
#     return max_similarities, closest_indices

# # Function to detect hallucinations and explain why
# def detect_hallucinations_with_explanation(conversation_text, summary_text, threshold=0.7):
#     # Split conversation and summary into sentences
#     conversation_sentences = [sent.strip() for sent in conversation_text.split('.') if sent.strip()]
#     summary_sentences = [sent.strip() for sent in summary_text.split('.') if sent.strip()]

#     # Calculate similarity between conversation and summary
#     similarities, closest_indices = calculate_similarity(conversation_sentences, summary_sentences)

#     explanations = []

#     # Identify hallucinations and give reasons
#     for i, sim in enumerate(similarities):
#         summary_sentence = summary_sentences[i]
#         closest_conversation_sentence = conversation_sentences[closest_indices[i]]

#         if sim < threshold:
#             explanation = f"Hallucination: \"{summary_sentence}\" does not closely match any sentence in the conversation."
#             explanation += f"\nClosest match in conversation: \"{closest_conversation_sentence}\" (Similarity: {sim:.2f})"
#             explanations.append(explanation)
#         else:
#             explanation = f"Supported: \"{summary_sentence}\" is consistent with the conversation."
#             explanation += f"\nMatched with: \"{closest_conversation_sentence}\" (Similarity: {sim:.2f})"
#             explanations.append(explanation)
    
#     # Calculate hallucination percentage
#     hallucination_count = sum(1 for sim in similarities if sim < threshold)
#     hallucination_percentage = hallucination_count / len(summary_sentences) * 100

#     return explanations, hallucination_percentage

# # Sample conversation and summary
# conversation_text = """
# Deborah Smith?,The customer needs to cancel their cousin's cellphone service because he passed away and she has been named administrator by the court. The agent advised the customer to go to a corporate store with a valid ID and the death certificate in order to authenticate and cancel the service. The customer was given clear instructions on what documents to bring to the store for authentication and cancellation of the cellphone service.
# "How are you today, ma'am, everything good.",,,
# "I'm doing fine, thank you.",,,
# "Um, I need to cancel my cousins.",,,
# Um cellphone.,,,
# "You're welcome. So, how can I help you today.",,,
# Because his passed away?,,,
# "Oh, I'm so sorry for your loss.",,,
# Thank you.,,,
# His phone number is four 0z four.,,,
# "OK, Can I please provide me with your phone number.",,,
# #####,,,
# "Alright, can you please provide me with the passcode?",,,
# I do not know it know.,,,
# "Uh to be able to open this account. I need to authenticate it, ma'am.",,,
# And I cannot.,,,
# Without without the passcode?,,,
# Well,,,
# Uh,,,
# "Well, how can I do that he passed away unexpectedly No one knows what the passcode is I've been named administrator by the court, and I'm supposed.",,,
# This so.,,,
# Okay.,,,
# "OK, uh, all you need to do right now, you need to go to PSG store with this They're They're tiff a kit and your on your I D. But about, but it's need to be valid. Your your I D. And this certificate?",,,
# suggest I do?,,,
# Yeah.,,,
# "OK, say that again, I need the death certificate. And the my I D.",,,
# I?,,,
# "Yeah, but but but That's valid I D, uh,",,,
# "No, you need to go to a PSG corporate sales store.",,,
# "So, do I? Just go to a cellphone store, what do I do?",,,
# "OK, can.",,,
# Can you?,,,
# "Corporate store, ma'am Fo of PSG.",,,
# "Can you can you say that again, please.",,,
# OK.,,,
# "Alright, and how do I know if it's a corporate store.",,,
# ok you need to go to uh the PSG corporate store with a valid i d and this certificate,,,
# ok maybe you can go through your nearest store,,,
# I mean there's a million around me. I'm not gonna go from the store to store.,,,
# And they can help you with that.,,,
# """

# summary_text = """
# The customer needs to cancel their cousin's cellphone service because he passed away and she has been named administrator by the court. The agent advised the customer to go to a corporate store with a valid ID and the death certificate in order to authenticate and cancel the service. The customer was given clear instructions on what documents to bring to the store for authentication and cancellation of the cellphone service."""

# # Detect hallucinations in the summary and provide explanations
# explanations, hallucination_percentage = detect_hallucinations_with_explanation(conversation_text, summary_text)

# # Print results
# for explanation in explanations:
#     print(explanation)
# print(f"Hallucination Percentage: {hallucination_percentage:.2f}%")

import torch
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained model for embeddings
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # A smaller model for sentence embeddings

# Function to calculate cosine similarity
def calculate_similarity(conversation_sentences, summary_sentences):
    # Encode the sentences to get their embeddings
    conversation_embeddings = model.encode(conversation_sentences, convert_to_tensor=True)
    summary_embeddings = model.encode(summary_sentences, convert_to_tensor=True)

    # Calculate cosine similarities between the summary and conversation
    similarity_matrix = util.pytorch_cos_sim(summary_embeddings, conversation_embeddings)

    # For each summary sentence, find the highest similarity with any conversation sentence
    max_similarities, closest_indices = torch.max(similarity_matrix, dim=1)
    
    return max_similarities, closest_indices

# Function to detect hallucinations, explain, and generate final corrected summary
def correct_summary(conversation_text, summary_text, threshold=0.7):
    # Split conversation and summary into sentences
    conversation_sentences = [sent.strip() for sent in conversation_text.split('.') if sent.strip()]
    summary_sentences = [sent.strip() for sent in summary_text.split('.') if sent.strip()]

    # Calculate similarity between conversation and summary
    similarities, closest_indices = calculate_similarity(conversation_sentences, summary_sentences)

    explanations = []
    final_summary = []

    # Identify hallucinations and correct the summary
    for i, sim in enumerate(similarities):
        summary_sentence = summary_sentences[i]
        closest_conversation_sentence = conversation_sentences[closest_indices[i]]

        if sim < threshold:
            explanation = f"Hallucination: \"{summary_sentence}\" does not closely match any sentence in the conversation."
            explanation += f"\nReplacing with: \"{closest_conversation_sentence}\" (Similarity: {sim:.2f})"
            explanations.append(explanation)
            final_summary.append(closest_conversation_sentence)  # Replace with closest conversation sentence
        else:
            explanation = f"Supported: \"{summary_sentence}\" is consistent with the conversation."
            explanation += f"\nMatched with: \"{closest_conversation_sentence}\" (Similarity: {sim:.2f})"
            explanations.append(explanation)
            final_summary.append(summary_sentence)  # Keep the original summary sentence
    
    # Calculate hallucination percentage
    hallucination_count = sum(1 for sim in similarities if sim < threshold)
    hallucination_percentage = hallucination_count / len(summary_sentences) * 100

    # Join the corrected sentences into a final summary
    final_corrected_summary = '. '.join(final_summary) + '.'

    return explanations, hallucination_percentage, final_corrected_summary

# Sample conversation and summary
conversation_text = """
I need to cancel my cousin's appointment
Sure, I can help you with that. What's the appointment date?
It's on the 23rd of this month
Got it. The appointment has been canceled
"""

summary_text = """
The customer called to reschedule their cousin's appointment. The agent helped them with this"""

# Detect hallucinations, provide explanations, and generate the final summary
explanations, hallucination_percentage, final_corrected_summary = correct_summary(conversation_text, summary_text)

# Print explanations and the final summary
for explanation in explanations:
    print(explanation)
print(f"Hallucination Percentage: {hallucination_percentage:.2f}%")
print("\nFinal Corrected Summary:\n", final_corrected_summary)
