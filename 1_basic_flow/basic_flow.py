from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv
from litellm import completion
#first comment
#second comment

load_dotenv()

# This flow, ExampleFlow, uses the GPT-4o-mini model to generate a random city name and then provide a fun fact about that city.
# The flow consists of two main functions:
# 1. generate_city: This function is marked with the @start() decorator, indicating the start of the flow. It sends a request to the model to return the name of a random city in the world. The response is then printed and returned.
# 2. generate_fun_fact: This function is marked with the @listen(generate_city) decorator, meaning it waits for the generate_city function to complete. Once it receives the random city name, it sends another request to the model to get a fun fact about that city. The fun fact is then returned.
# The flow is initiated by creating an instance of ExampleFlow and calling the kickoff method. The generated fun fact is printed at the end.

class ExampleFlow(Flow):
    model = "gpt-4o-mini"

    @start() # @start() is a decorator that marks the start of the flow
    def generate_city(self):
        print("Starting flow")

        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Return the name of a random city in the world.",
                },
            ],
        )

        random_city = response["choices"][0]["message"]["content"]
        print(f"Random City: {random_city}")

        return random_city

    @listen(generate_city) # @listen() is a decorator that waits for the generate_city function to finish and then calls the generate_fun_fact function
    def generate_fun_fact(self, random_city):
        print("Received random city:", random_city)
        response = completion(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Tell me a fun fact about {random_city}",
                },
            ],
        )

        fun_fact = response["choices"][0]["message"]["content"]
        return fun_fact


flow = ExampleFlow()
result = flow.kickoff()

print(f"Generated fun fact: {result}")
