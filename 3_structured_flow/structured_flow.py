# This flow, StructuredExampleFlow, demonstrates a structured flow using CrewAI.
# It uses Pydantic to define a state model with two fields: counter and message.
# The flow consists of three methods: first_method, second_method, and third_method.
# Each method is decorated with @listen() to indicate that it should execute after another method completes.
# The flow is initiated by creating an instance of StructuredExampleFlow and calling the kickoff() method.
# The final state is printed after the flow has completed.


# Whats different from the unstructured flow. You need to define an initial state.
# the initial state must be a Pydantic model.
# Goal is to add structure to the flow.
# 

from crewai.flow.flow import Flow, listen, start
from pydantic import BaseModel

# Define the initial state as a Pydantic model
class ExampleState(BaseModel):
    counter: int = 0
    message: str = ""


class StructuredExampleFlow(Flow[ExampleState]):

    @start()
    def first_method(self):
        print("Starting flow")
        print(f"State before first_method:\n{self.state}\n")
        self.state.message = "Hello from structured flow"
        self.state.counter += 1

    @listen(first_method)
    def second_method(self):
        print(f"State before second_method:\n{self.state}\n")
        self.state.counter += 1
        self.state.message += " - updated"

    @listen(second_method)
    def third_method(self):
        print(f"State before third_method:\n{self.state}\n")
        self.state.counter += 1
        self.state.message += " - updated again"

        print(f"State after third_method: {self.state}")


flow = StructuredExampleFlow()
flow.kickoff()

print(f"Final state:\n{flow.state}")
