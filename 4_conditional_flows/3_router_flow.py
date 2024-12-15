# This flow, RouterFlow, demonstrates a router flow using CrewAI.
# It uses the router() function to conditionally route the flow based on the success_flag in the state.
# The flow is initiated by creating an instance of RouterFlow and calling the kickoff() method.
# The final state is printed after the flow has completed.

import random

from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel


class ExampleState(BaseModel):
    success_flag: bool = False


class RouterFlow(Flow[ExampleState]):

    @start()
    def start_method(self):
        print("Starting the structured flow")
        random_boolean = random.choice([True, False])
        self.state.success_flag = random_boolean

    @router(start_method) # This listens for the start_method to finish and then calls the second_method function       
    def second_method(self):
        if self.state.success_flag:
            return "success" # if things weere successful, we return the string "success"
        else:
            return "failed" # if things were not successful, we return the string "failed"

    @listen("success") # This will listen and go down the success branch of the router
    def third_method(self):
        print("Third method running")

    @listen("failed") # This will listen and go down the failed branch of the router    
    def fourth_method(self):
        print("Fourth method running")


flow = RouterFlow()
flow.kickoff()
