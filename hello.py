import os
import vertexai.preview
# from vertexai.language_models import TextGenerationModel
from vertexai.language_models import ChatModel

vertexai.init(project="prj-mm-plaid-dev-001", location="us-central1")

def create_session():
    model = ChatModel.from_pretrained("chat-bison@001")
    model = model.start_chat()
    return model

def response(model, message):
    parameters = {
        "candidate_count": 1,
        "max_output_tokens": 1024,
        "temperature": 0.9,
        "top_p": 1
    }
    result = model.send_message(message, **parameters)
    return result.text

def run_chat():
    model = create_session()
    print(f"Chat Session created")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break
        content = response(model, user_input)
        print(f"AI: {content}")


if __name__ == '__main__':
    run_chat()


# response = model.predict(
#     """when did Dortmund won their UCL?""",
#     **parameters
# )
# print(f"Response from Model: {response.text}")