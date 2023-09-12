import streamlit as st
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained model and tokenizer
model_name = "pytorch_version"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def get_new_prompt(messages):
    prompt = ""
    for message in messages:
        prompt += f"{message['role']}: {message['content']}\n"
    return prompt
  
st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    # Tokenize the input
    new_prompt = get_new_prompt(st.session_state.messages)
    input_ids = tokenizer.encode(new_prompt, return_tensors="pt")
    
    # Generate a response
    output = model.generate(input_ids, max_length=350, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
	
	
def get_new_prompt(messages):
	prompt = ""
	for message in messages:
		prompt += ""
        '''
