import chainlit as cl

@cl.on_message
async def main(message: cl.Message):
    # This runs when user sends a message
    await cl.Message(
        content=f"Received: {message.content}"
    ).send()