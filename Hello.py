import streamlit as st
import replicate
import os

st.set_page_config(page_title='Chatbot using replicate')

with st.sidebar:

    st.title('Chatbots Comparision')
    st.write('This chatbot is created for comparing responses from the open-source Llama2, Mistral, and Gemma LLM model.')
    if 'REPLICATE_API_TOKEN' in st.secrets:
        st.success('API key already provided!', icon='✅')
        replicate_api = st.secrets['REPLICATE_API_TOKEN']
    else:
        replicate_api = st.text_input('Enter Replicate API token:', type='password')
        if not (replicate_api.startswith('r8_') and len(replicate_api)==40):
            st.warning('Please enter your credentials!', icon='⚠️')
        else:
            st.success('Proceed to entering your prompt message!', icon='👉')
    os.environ['REPLICATE_API_TOKEN'] = replicate_api

    #st.title('Select you chatbot model')

    # st.subheader('Models and parameters')
    # selected_model = st.sidebar.selectbox('Choose a model', ['Llama2-70b', 'Mistral-7b', 'Gemma-7b'], key='selected_model')
    # if selected_model == 'Llama2-70b':
    #     llm = 'meta/llama-2-70b-chat:2d19859030ff705a87c746f7e96eea03aefb71f166725aee39692f1476566d48'
    # elif selected_model == 'Mistral-7b':
    #     llm = 'mistralai/mistral-7b-instruct-v0.2:f5701ad84de5715051cb99d550539719f8a7fbcf65e0e62a3d1eb3f94720764e'
    # elif selected_model == 'Gemma-7b':
    #     llm = 'google-deepmind/gemma-7b-it:2790a695e5dcae15506138cc4718d1106d0d475e6dca4b1d43f42414647993d5'
    # option = st.selectbox('Models:',
    # ('Llama2-70b', 'Mistral-7b', 'Claude2-13b'))
    # if option == 'Llama2':
    #     llm = 'meta/llama-2-70b-chat:2d19859030ff705a87c746f7e96eea03aefb71f166725aee39692f1476566d48'
    # elif option == 'Mistral':
    #     llm = 'mistralai/mistral-7b-instruct-v0.2:f5701ad84de5715051cb99d550539719f8a7fbcf65e0e62a3d1eb3f94720764e'
    # elif option == 'Mistral':
    #     llm = 'tomasmcm/claude2-alpaca-13b:49b2d4cc082625d10463f56426bd012ebd75c11e3d6c2b54f7532c6ddd46b944'
    #     st.write('Model selection complete', option)

    #st.write('you selected', option)

    

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

#st.write('Selected model', llm)

def generate_response(input):

    string_dialogue = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once and in one sentence'."
    # for dict_message in st.session_state.messages:
    #     if dict_message["role"] == "user":
    #         string_dialogue += "User " + ": " + dict_message["content"] + "\n\n"
    #     else:
    #         string_dialogue += "Assistant "  + ": " + dict_message["content"] + "\n\n"
    
    output1 = replicate.run('meta/llama-2-70b-chat:2d19859030ff705a87c746f7e96eea03aefb71f166725aee39692f1476566d48', input={"prompt": f"{string_dialogue} {input} Assistant: ","temperature":1, "max_length":32, "repetition_penalty":1})
    st.write('**Llama2 - 70b:**')
    placeholder1 = st.empty()
    full_response = ''
    for item in output1:
        full_response += item
        placeholder1.markdown(full_response)
    placeholder1.markdown(full_response)
    message1 = {"role": "assistant", "content": full_response}
    x1 = st.session_state.messages.append(message1)

    output2 = replicate.run('mistralai/mistral-7b-instruct-v0.2:f5701ad84de5715051cb99d550539719f8a7fbcf65e0e62a3d1eb3f94720764e', input={"prompt": f"{string_dialogue} {input} Assistant: ","temperature":1, "max_length":32, "repetition_penalty":1})
    st.write('**Mistral  7b:**')
    placeholder2 = st.empty()
    full_response = ''
    for item in output2:
        full_response += item
        placeholder2.markdown(full_response)
    placeholder2.markdown(full_response)
    message2 = {"role": "assistant", "content": full_response}
    x2 = st.session_state.messages.append(message2)
    #st.write('This is Mistral: ', message2)

    # for dict_message in st.session_state.messages:
    #     if dict_message["role"] == "user":
    #         string_dialogue += "User " + ": " + dict_message["content"] + "\n\n"
    #     else:
    #         string_dialogue += "Assistant "  + ": " + dict_message["content"] + "\n\n"

    output3 = replicate.run('google-deepmind/gemma-7b-it:2790a695e5dcae15506138cc4718d1106d0d475e6dca4b1d43f42414647993d5', input={"prompt": f"{string_dialogue} {input} Assistant: ","temperature":1, "max_length":32, "repetition_penalty":1})
    st.write('**Gemma - 7b:**')
    placeholder3 = st.empty()
    full_response = ''
    for item in output3:
        full_response += item
        placeholder3.markdown(full_response)
    placeholder3.markdown(full_response)
    message3 = {"role": "assistant", "content": full_response}
    x3 = st.session_state.messages.append(message3)

    output4 = replicate.run('swartype/lanne-m1-70b:1df3f75ba48b648d82399ed7f6f8537d718903c2c2e73e5eabb4e014377dfe79', input={"prompt": f"{string_dialogue} {input} Assistant: ","temperature":1, "max_length":32, "repetition_penalty":1})
    st.write('**Lanne - 70b:**')
    placeholder4 = st.empty()
    full_response = ''
    for item in output4:
        full_response += item
        placeholder4.markdown(full_response)
    placeholder4.markdown(full_response)
    message3 = {"role": "assistant", "content": full_response}
    x4 = st.session_state.messages.append(message3)

    #st.write('This is Gemma: ', message3)
    
    #output =  x1 + x2 + x3

    #return output

#input = st.text_input("")
# st.write(generate_response(input))

if input := st.chat_input(disabled=not replicate_api):
    st.session_state.messages.append({"role": "user", "content": input})
    with st.chat_message("user"):
        st.write(input)

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(input)
    #         placeholder = st.empty()
    #         full_response = ''
    #         for item in response:
    #             full_response += item
    #             placeholder.markdown(full_response)
    #         placeholder.markdown(full_response)
    # message = {"role": "assistant", "content": full_response}
    #st.session_state.messages.append(response)
