# Instructions for implementing edge dynamics in the SIR model using Mesa

## Exercise: Improving Our Infection Spreading Model
### Setup

1. **Import necessary modules (including your base SIR model):**
```python
   from mesa import Agent, Model
   from mesa.time import RandomActivation
   from mesa.space import NetworkGrid
   from mesa.datacollection import DataCollector
   import networkx as nx
   from base_model.sir import SIRAgent, SIRModel  # Assuming you've implemented this
```

## Tasks

1. **Define a new SIREdgeAgent class (inheriting from SIRAgent):** 
   - Add methods for managing connections (e.g., add_connection, remove_connection)
   - Modify the step() method to include edge dynamics behavior

2. **Define a new SIREdgeModel class (inheriting from SIRModel):** 
   - Add parameters related to edge dynamics (e.g., edge_change_rate)
   - Modify the __init__() method to set up the initial network with dynamic edges
   - Implement methods for global edge dynamics (e.g., apply_social_distancing)
   - Modify the step() method to include edge dynamics processes

3. **Implement edge dynamics in SIREdgeAgent's step() method:** 
   - Example: If infected, potentially remove connections (self-isolation)
   - Example: If susceptible, potentially add new connections

4. **Implement edge dynamics in SIREdgeModel's step() method:**
   - Call the base model's step() method
   - Apply global edge dynamics (e.g., social distancing measures)
   - Update the network structure based on agent behaviors and global dynamics

5. **Modify data collection to track network metrics over time:**
   - Example: Average degree, clustering coefficient, number of edges

6. **(Optional) Implement visualization methods to show network changes over time**

**Remember**:
- Use self.model.grid.get_neighbors() to access an agent's neighbors
- Use self.model.grid.add_edge() and remove_edge() to modify connections
- Ensure that edge changes are reflected in both the NetworkGrid and the underlying networkx graph
- Consider the computational complexity of your edge dynamics, especially for larger networks

Good luck! Don't hesitate to ask for clarification or assistance.
