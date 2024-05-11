from langchain_google_genai import ChatGoogleGenerativeAI

class Vprom:
    def __init__(self,schema=None)
        self.llm  = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.3,google_api_key='AIzaSyCPcRRwqR8l4f0Dnmaj0M_QeJqYgV_o9lY')
        self.schema  = schema 

    def schema_build(self):
        self.schema = {}
        self.schema.input = {}
        self.schema.input.instructions = []
    
    def migrate_prompts(self,instructions):
        #self.schema_build()
        for index,instruct in enumerate(instructions):

            MIGRATE_INSTRUCTION = f"""

You are a compiler that converts written text into an artificial intelligence prompt for some use cases in business, programming,
 and other use cases. When the user enters the text he wants to convert, you must do some procedures before converting it:
   - Identifying the events within it: You must check whether the text contains any event. If it contains an event, 
   you must place the event in the prompt and in front of it its result. 
   - Defining inputs, outputs, pluses, and deficiencies:
    Inputs are variables that the user must enter into the system, and outputs are the outputs after the “=” sign, and the “+” are addition operations.
    You must pay close attention to what the user is adding, as he can add many things on top of each other to build something. 
    Certain deficiencies must be excluded from the output 
    - You must also determine the type of input and the type of output in the final probit by analyzing the input text well and writing in the final probit every input and output, its type, events, and everything related to it. 
    Your primary job: It is converting text into an understandable and adaptable promp for different use cases, whether in business, programming, health care, or anything else , without details just 1 sentence prompt

    {instruct}

"""
            print(f"Prompt Instruct ({index}/{len(instructions)}) is Migrating Righ Now ...")
            prompt_output = self.llm.invoke(MIGRATE_INSTRUCTION)
            self.schema.input.instructions.append(prompt_output)

    def return_prompts(self):
        print(self.schema.input.instructions)

    @property
    def instructions(self):
        return self.schema.input.instructions


        



