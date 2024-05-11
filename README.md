# Vprom

## Overview
This code provides a class called `Vprom` which utilizes Google's Generative AI model to convert written text into artificial intelligence prompts. It's designed to assist in various use cases such as business, programming, and more by generating prompts from user-provided text.

## Installation
Ensure you have the `langchain_google_genai` package installed. You can install it via pip:



## Usage
1. Import the `Vprom` class from `vprom` package.
2. Create an instance of `Vprom`.
3. Call the `migrate_prompts` method with a list of instructions as input.
4. Access the generated prompts using the `return_prompts` method.

Example:
```python

# Import the Vprom class
from vprom import Vprom

# Create an instance of Vprom
vp = Vprom()

# List of instructions
instructions = [
    "USERNAME(STR) + HELLO = HI USERNAME(STR) HOW CAN I HELP YOU TODAY",
    "USERNAME(STR) + INPUT(CURRENCY IN (USD(INTEGER))) = CONVERT(CURRENCY)-> EGP"
]

# Generate prompts
vp.migrate_prompts(instructions)

# Access generated prompts
vp.return_prompts()
```

```
"USERNAME(STR) + HELLO = HI USERNAME(STR) HOW CAN I HELP YOU TODAY" :
Prompt: Given a username (text), generate a personalized greeting message incorporating the username.

...

"USERNAME(STR) + INPUT(CURRENCY IN (USD(INTEGER))) = CONVERT(CURRENCY)-> EGP"
AI Prompt: Convert user-provided currency amount (USD) to Egyptian Pounds (EGP).


```

## Parameters

    model: Specify the model to use for generative AI. Default is "gemini-pro".
    temperature: Control the randomness of the generated text. Default is 0.3.
    google_api_key: Provide a Google API key for accessing the generative AI service.

## Methods

    schema_build(): Initialize the schema for storing prompts.
    migrate_prompts(instructions): Convert a list of instructions into prompts.
    return_prompts(): Print or return the generated prompts.
    instructions: Get the list of generated prompts.

## Prompt Generation Process

The migrate_prompts method takes a list of instructions as input and converts each instruction into a prompt by following certain procedures:

    Identifying events within the text and placing them in the prompt along with their results.
    Defining inputs, outputs, additions, and exclusions from the output.
    Analyzing the input text to determine types of inputs and outputs in the final prompt.



## Notes

    This code relies on Google's Generative AI model, so ensure you have the necessary API key.
    The generated prompts aim to be concise and adaptable for different use cases.



Feel free to reach out if you have any questions or suggestions!

