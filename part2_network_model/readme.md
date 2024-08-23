# Instructions for implementing the SIR model using Mesa

## Exercise: Making A Infection Spreading Model

### Setup
1. Import necessary modules from Mesa:

```python
   from mesa import Agent, Model
   from mesa.time import RandomActivation
   from mesa.space import NetworkGrid
   from mesa.datacollection import DataCollector
```

### Tasks
1. **Define the SIRAgent class**:
   - Inherit from Mesa's Agent class
   - Initialize with unique_id, model, and initial_state ('S', 'I', or 'R')
   - Implement a step() method to define the agent's behavior each time step

2. **Define the SIRModel class**:
   - Inherit from Mesa's Model class
   - Initialize with parameters: N (number of agents), initial_infected,
     infection_probability, recovery_probability
   - Create a network (hint: use networkx to generate a graph)
   - Create agents and place them on the network
   - Set up a scheduler (hint: use RandomActivation)
   - Implement a step() method to advance the model by one time step
   - Set up data collection to track the counts of S, I, and R over time

3. **Implement the SIRAgent's step() method**:
   - If the agent is susceptible:
     - Check neighbors and potentially become infected
   - If the agent is infected:
     - Potentially recover

4. **Implement the SIRModel's step() method:**
   - Advance the scheduler by one step
   - Collect data

5. **Implement** a vaccination option**
   - Vaccinated agents cannot be infected and behave like recovered individuals

6. **(Optional) Implement any helper methods you find useful**

# Exercises
## Exercise 1: Simulating the SIR Model on Different Network Topologies
  **Task**: Simulate the SIR model on different types of networks, including:
      - A random network (Erdős-Rényi model)
      - A small-world network (Watts-Strogatz model)
      - A scale-free network (Barabási-Albert model)
  **Objective**: Observe and compare how the topology of each network affects the spread of the disease. Focus on differences in the speed of the outbreak, the peak of infections, and the final epidemic size for each network type.
  **Question**: How does the network structure influence the timing and extent of the outbreak?

## Exercise 2: Varying Transmission and Recovery Rates
  **Task**: In your SIR model simulation, systematically vary the transmission rate (ββ) and the recovery rate ($\gamma$).
  **Objective**: Investigate how changes in these rates affect the dynamics of the disease, particularly:
      The basic reproduction number $R_0$​
      The peak number of infections
      The duration of the epidemic
  **Question**: How do different values of $\beta$ and $\gamma$ alter the course of the epidemic? What happens when $R_0$​ is greater than or less than 1?

## Exercise 3: Exploring Different Initial Conditions
  **Task**: Start the infection at different nodes within the network, such as:
      - A highly connected node (hub)
      - A node with a low degree (few connections)
  **Objective**: Compare the outcomes to see how the initial placement of the infection affects the spread of the disease. Focus on the speed, peak, and final size of the epidemic.
  Question: How does the location of the initial infection influence the dynamics of the outbreak?

## Exercise 4: Analyzing the Impact of Network Size
  **Task**: Run the SIR model on networks of different sizes while keeping other parameters (e.g., transmission rate, recovery rate) constant.
  **Objective**: Observe how the size of the network influences the epidemic's progression. Pay attention to changes in the epidemic threshold, the peak of infections, and the total number of infected individuals.
  **Question**: How does increasing or decreasing the size of the network affect the spread of the disease?

## Exercise 5: Effect of Clustering and Network Density
  **Task**: Modify the clustering coefficient (the extent to which a node's neighbors are also neighbors) or the overall density of the network (number of edges) in your SIR simulation.
  **Objective**: Explore how changes in clustering or network density influence the spread of the disease. Investigate whether these factors lead to faster local outbreaks or alter the epidemic threshold.
  **Question**: What role do clustering and network density play in the dynamics of the epidemic? How do they affect the speed and extent of the spread?

## Exercise 6: Comparing Targeted vs. Random Vaccination Strategies

    **Task**: Implement different vaccination strategies in your network:
        Targeted vaccination of the most connected nodes (hubs)
        Random vaccination of nodes
    **Objective**: Compare the effectiveness of these strategies in preventing or reducing the outbreak. Measure the reduction in the number of infections and the impact on the epidemic threshold.
    **Question**: Which vaccination strategy is more effective in controlling the spread of the disease? Why?


**Remember**:
- Use self.random to generate random numbers for probabilistic events
- Use self.schedule to manage agents in the model
- Use self.grid to manage the network structure
- Refer to the Mesa documentation for detailed API information

Good luck, and don't hesitate to ask for help if you get stuck!
