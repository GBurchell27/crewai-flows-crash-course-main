from crewai.flow.flow import Flow, listen, start
# UntructuredExampleFlow inherits from CrewAI's Flow class
# Manages state and execution flow between methods

# **Decorators:**
# @start(): Marks first_method as the entry point
# @listen(): Indicates which method should execute after another one completes
# Creates a sequential chain: first_method → second_method → third_method

# **State Management:**
# Uses self.state dictionary to maintain data between method calls
# Initializes state in first_method
# Each subsequent method can access and modify the state

# **Flow Execution:**   
# Creates flow instance and starts execution with kickoff()

# When run, this will:
# Start with first_method
# Initialize state with message and counter
# Execute second_method, updating the message and incrementing counter
# Execute third_method, further updating the message and counter
# Print final state
# This demonstrates a basic unstructured flow where methods execute in sequence while sharing and modifying state data.


class UntructuredExampleFlow(Flow):

    @start() 
    def first_method(self):
        print("Starting flow")
        print(f"State before first_method:\n{self.state}")
        self.state["message"] = "Hello from unstructured flow" # self.state is a dictionary that stores the state of the flow
        self.state["counter"] = 0 # self.state is a dictionary that stores the state of the flow

    @listen(first_method) 
    def second_method(self):
        print(f"State before second_method:\n{self.state}")
        self.state["message"] += " - updated" # This takes the message from the first_method and adds " - updated" to it
        self.state["counter"] += 1 # This takes the counter from the first_method and increments it by 1

    @listen(second_method) 
    def third_method(self):
        print(f"State before third_method:\n{self.state}")
        self.state["message"] += " - updated again" # This takes the message from the second_method and adds " - updated again" to it
        self.state["counter"] += 1 # This takes the counter from the second_method and increments it by 1

        print(f"State after third_method: {self.state}")


flow = UntructuredExampleFlow()
flow.kickoff()

print(f"Final state:\n{flow.state}")
