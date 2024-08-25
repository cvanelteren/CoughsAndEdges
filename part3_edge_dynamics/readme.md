<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [Disease Dynamics in a Dynamic Network ](#disease-dynamics-in-a-dynamic-network)
- [Setup](#setup)
- [:memo: Exercise 1: Implementing SIREdgeAgent](#memo-exercise-1-implementing-siredgeagent)
- [:memo: Exercise 2: Implementing SIREdgeModel](#memo-exercise-2-implementing-siredgemodel)
- [:memo: Exercise 3: Edge Dynamics in SIREdgeModel](#memo-exercise-3-edge-dynamics-in-siredgemodel)
- [:memo: Exercise 4: Data Collection](#memo-exercise-4-data-collection)
- [:memo: Exercise 5: Behavior Experimentation](#memo-exercise-5-behavior-experimentation)
- [:memo: Exercise 6: Visualization (Optional)](#memo-exercise-6-visualization-optional)
- [:memo: Challenge Exercise:](#memo-challenge-exercise)

<!-- markdown-toc end -->


# Disease Dynamics in a Dynamic Network 
Welcome   to  the   next   level   of  our   epidemiological
exploration! We've  mastered the  basics of  disease spread,
but now it's time to add  a dash of real-world complexity to
our digital petri dish. Remember the days of lockdowns, when
"social distancing" became the buzzword  du jour, and we all
became experts  at washing our  hands to the tune  of "Happy
Birthday"? Well,  it's time to bring  those experiences into
our simulation.

In our  previous session,  we explored how  vaccinations and
mask-wearing impact  disease spread. Now, we're  diving into
the intricate dance of  social distancing. What happens when
we  limit  each  person's   daily  interactions  to  just  k
individuals? Or  imagine a world where  our digital citizens
actively  dodge  their  COVID-positive  peers  like  they're
avoiding spoilers for their favorite TV show.

Your mission, should  you choose to accept it,  is to design
and implement a dynamic system  where our agents adapt their
social networks  based on the  ebb and flow of  the disease.
Can you  create a  set of behaviors  that will  "flatten the
curve" faster  than you  can say "exponential  growth"? It's
time to  turn our simple  SIR model into a  complex adaptive
system,  where not  only  the health  states  of our  agents
change, but also  their social connections. Let's  see if we
can code our way to a safer, albeit more antisocial, digital
world!

Are you ready to make our virtual population practice social
distancing  like pros?  Let's  dive  in and  see  if we  can
outsmart this digital disease!

# Setup
**Import necessary modules (including your base SIR model):**
```python
   from mesa import Agent, Model
   from mesa.time import RandomActivation
   from mesa.space import NetworkGrid
   from mesa.datacollection import DataCollector
   import networkx as nx
   from base_model.sir import SIRAgent, SIRModel  # Assuming you've implemented this
```

# :memo: Exercise 1: Implementing SIREdgeAgent

1. Create a new class `SIREdgeAgent` that inherits from `SIRAgent`.
2. Add methods `add_connection(self, other_agent)` and `remove_connection(self, other_agent)`.
3. Modify the `step()` method to include basic edge dynamics:
    - If the agent is infected, remove a random connection with probability 0.1.
    - If the agent is susceptible, add a random connection with probability 0.05.

# :memo: Exercise 2: Implementing SIREdgeModel

1. Create a new class `SIREdgeModel` that inherits from `SIRModel`.
2. Add a parameter `edge_change_rate` to the init method.
3. Implement a method `apply_social_distancing` that removes a fraction of edges based on the current infection rate.

# :memo: Exercise 3: Edge Dynamics in SIREdgeModel

1. Modify the `step()` method in `SIREdgeModel` to call `apply_social_distancing` after the base model's step.
2. Implement a method `update_network()` that reflects all edge changes made by agents in the NetworkGrid.
3. Call `update_network()` at the end of each step.

# :memo: Exercise 4: Data Collection

Modify the DataCollector in SIREdgeModel to track:

- Average degree of the network
- Number of edges in the network
- Clustering coefficient of the network
- (or your favorite centrality measure)

- Create a method to calculate these metrics using networkx functions.

# :memo: Exercise 5: Behavior Experimentation

1. Implement a "lockdown" behavior where agents remove all connections if the infection rate exceeds a threshold.
2. Create a "selective avoidance" behavior where susceptible agents preferentially remove connections to infected agents.
3. Compare the effect of these behaviors on the disease spread and network structure.

# :memo: Exercise 6: Visualization (Optional)

Create  a method  to visualize  the network,  coloring nodes
based on their SIR state.  Implement an animation that shows
how the network evolves over time as the disease spreads.

# :memo: :smilingimp: Challenge Exercise
Design and  implement a  set of  agent behaviors  and global
dynamics that effectively "flatten the curve" of infections.
Compare the results to the base model without dynamic edges.

**Remember**:
- The network is stored in `self.model.grid.G` and can be accessed directly
- Use `self.model.grid.get_neighbors()` to access an agent's neighbors
- Use `self.model.grid.add_edge()` and `remove_edge()` to modify connections
- Ensure that edge changes are reflected in both the `NetworkGrid` and the underlying networkx graph
- Consider the computational complexity of your edge dynamics, especially for larger networks

Good luck! Don't hesitate to ask for clarification or assistance.
