# base_model/sir.py

"""
Instructions for implementing the SIR model using Mesa

1. Import necessary modules from Mesa:
   from mesa import Agent, Model
   from mesa.time import RandomActivation
   from mesa.space import NetworkGrid
   from mesa.datacollection import DataCollector

2. Define the SIRAgent class:
   - Inherit from Mesa's Agent class
   - Initialize with unique_id, model, and initial_state ('S', 'I', or 'R')
   - Implement a step() method to define the agent's behavior each time step

3. Define the SIRModel class:
   - Inherit from Mesa's Model class
   - Initialize with parameters: N (number of agents), initial_infected,
     infection_probability, recovery_probability
   - Create a network (hint: use networkx to generate a graph)
   - Create agents and place them on the network
   - Set up a scheduler (hint: use RandomActivation)
   - Implement a step() method to advance the model by one time step
   - Set up data collection to track the counts of S, I, and R over time

4. Implement the SIRAgent's step() method:
   - If the agent is susceptible:
     - Check neighbors and potentially become infected
   - If the agent is infected:
     - Potentially recover

5. Implement the SIRModel's step() method:
   - Advance the scheduler by one step
   - Collect data

6. (Optional) Implement any helper methods you find useful

Remember:
- Use self.random to generate random numbers for probabilistic events
- Use self.schedule to manage agents in the model
- Use self.grid to manage the network structure
- Refer to the Mesa documentation for detailed API information

Good luck, and don't hesitate to ask for help if you get stuck!
"""

# Your implementation starts here:

# Import necessary modules


# Define SIRAgent class


# Define SIRModel class


# (Optional) Helper methods
