# # chatbot.py

# from transformers import AutoModelForCausalLM, AutoTokenizer
# import torch

# # Load the Llama model and tokenizer
# model_name = "meta-llama/Llama-2-7b-chat-hf"  # Replace with a smaller model if needed
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(model_name)

# def get_response(user_input):
#     inputs = tokenizer.encode(user_input, return_tensors="pt")
#     outputs = model.generate(inputs, max_length=100, do_sample=True, temperature=0.7)
#     response = tokenizer.decode(outputs[0], skip_special_tokens=True)
#     return response