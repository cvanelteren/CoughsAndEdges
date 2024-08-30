# Importing necessary libraries
import networkx as nx
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import matplotlib.pyplot as plt, numpy as np
from typing import List, Dict # for type hinting
from matplotlib.collections import LineCollection

# When this script is run we will create a new model and run it
# It will show some visualizations of the model with a network

# Try to see if you understand the code below. The syntax is not what to focus on, the logic is. What we do is we create a model,  add agents to it, and then run the model. The agents interact with each other and the model updates the state of the agents. We then visualize the model.

# Define the SIR agent class
class SIRAgent(Agent):
    def __init__(self,
        unique_id: int,
        model: Model
    ):
        # Call the parent class to initialize the agent
        super().__init__(unique_id, model)
        self.state = "S"  # All agents start as susceptible by default

    # Always implement a step otherwise the model does not do antyhing
    def step(self) -> None:
        # We override the parent class to implement the agent's behavior in the new model
        neighbors = list(self.model.grid.G.neighbors(self.unique_id))
        if self.state == "I" and np.random.rand() < self.model.recovery_chance:
            self.state = "R"
        if len(neighbors) == 0:
            return
        other = np.random.choice(neighbors)
        if self.state == "I" and self.model.agents[other].state == "S":
            if np.random.rand() < self.model.infection_chance:
                self.model.agents[other].state = "I"
        elif self.state == "S" and self.model.agents[other].state == "I":
            if np.random.rand() < self.model.infection_chance:
                self.state = "I"
        elif self.state == "I":
            if np.random.rand() < self.model.recovery_chance:
                self.state = "R"
        if np.random.rand() < self.model.mutation_chance:
            if self.state == "S":
                self.state = "I"
            elif self.state == "R":
                self.state = "S"


# Define the SIR model class
# A class is defined as class X where X is the name which is traditionally capitalized. We inherit from the Model class in the mesa library. This defines a few functions one of the important ones is the step method and the data collections. The data collection produces a pandas dataframe which is essentially a CSV file.
class SIRModel(Model):
    def __init__(
        self,
        G: nx.Graph,
        initial_infected: int = 1,
        infection_chance: float = 0.05,
        recovery_chance: float = 0.05,
        mutation_chance: float = 0.00,
        agent_type = SIRAgent,
    ):
        super().__init__(self)
        # the self keyword refers to the instance of the class. An instance is a specific object created from a particular class. For example farm = Farm() would create a potential instance of the Farm class. The self keyword is used to access variables that belongs to the class. It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class.
        self.num_nodes = len(G)
        self.grid = NetworkGrid(G)
        self.G = G
        np.random.seed = 42 # What is the answer to the universe?
        self.schedule = RandomActivation(self)
        self.infection_chance = infection_chance
        self.recovery_chance = recovery_chance
        self.mutation_chance = mutation_chance

        # Set up data collection
        # This automatically collects data from the model for each time step and stores it in a pandas dataframe
        self.datacollector = DataCollector(
            model_reporters={
                "S": lambda m: self.count_state(m, "S"),
                "I": lambda m: self.count_state(m, "I"),
                "R": lambda m: self.count_state(m, "R"),
                "States": lambda m: [a.state for a in m.agents],
            },
        )

        # Create agents and place them on the network
        for i, node in enumerate(self.G.nodes()):
            a = agent_type(i, self)
            self.schedule.add(a)
            self.grid.place_agent(a, node)

        # Infect initial set of nodes
        infected_nodes = self.random.sample(list(self.G.nodes()), initial_infected)
        for node in infected_nodes:
            self.grid.get_cell_list_contents([node])[0].state = "I"

    # This is called for eacht time step when you run the model by calling this step function
    def step(self) -> np.ndarray:
        # Collect data for this step
        self.datacollector.collect(self)
        # Advance the model by one step
        self.schedule.step()
        return np.arange(self.num_nodes)

    # A static method is a method that doesn't access the instance or class state but is still logically related to the class. It is defined with the @staticmethod decorator. It's use is to indicate to the programmer to what the function should be applied to
    @staticmethod
    def count_state(model, state)-> int:
        # Helper method to count the number of agents in a given state
        count = 0
        for agent in model.schedule.agents:
            if agent.state == state:
                count += 1
        return count

# Animation class
# Not intended for student's to understand but can be used
# to animate the spread of the disease
class Animation:
    def __init__(self, G, model=SIRModel, **kwargs):
        self.pos = kwargs.pop("layout", nx.arf_layout(G))
        self.colors = plt.colormaps.get_cmap("tab20c")(np.linspace(0, 1, 3))
        self.mapped = {
            state: self.colors[idx] for idx, state in enumerate(["S", "I", "R"])
        }
        self.model = model(G=G, **kwargs)
        self.fig, self.ax = plt.subplots()

        # add nodes and edges
        self.node_colors = [
            self.mapped[self.model.agents[id].state] for id in self.model.G.nodes()
        ]
        artists =  [plt.Line2D([], [], color=self.colors[idx], label=i) for idx, i in enumerate(["S", "I", "R"])]
        self.ax.legend(handles = artists)

        inax = self.ax.inset_axes((0.75, 0.75, 0.25, 0.25))
        for spine in inax.spines.values():
            spine.set_visible(False)
        inax.set_facecolor("none")
        inax.add_collection(LineCollection([], color="k", alpha=0.2))
        self.nodes = nx.draw_networkx_nodes(
            self.model.G,
            pos=self.pos,
            ax=inax,
            node_color=self.node_colors,
            node_size=48,
        )
        self.edges = inax.collections[0]
        inax.grid(False)
        inax.axis("equal")
        self.lines = {}
        for pop in "SIR":
            self.lines[pop] = self.ax.plot([], [], color=self.mapped[pop], label=pop)[0]
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Fraction of Population")
        self.ax.set_ylim(0, 1)

    def simulate(self, t=1):
        for ti in range(t):
            self.step()

    def step(self):
        mutations = self.model.step()
        return self.draw(mutations)

    def draw(self, mutations: List[int]) -> bool:
        if mutations is not None:
            # Add data to the curve
            for pop in "SIR":
                data = self.model.datacollector.model_reporters[pop](self.model)
                x, y = self.lines[pop].get_data()
                new_x = 1
                if len(x):
                    new_x = x[-1] + 1
                x = np.append(x, new_x)
                y = np.append(y, data/self.model.num_nodes)
                self.lines[pop].set_data(x, y)
            self.ax.relim()
            self.ax.autoscale_view()

            # Update the colors
            for node in mutations:
                self.node_colors[node] = self.mapped[self.model.agents[node].state]
            # Update the edges
            self.nodes.set_facecolors(self.node_colors)
            self.edges.set_segments(
                [
                    (self.pos[node], self.pos[neighbor])
                    for node, neighbor in self.model.G.edges()
                ]
            )
        # Force redraw of canvas
        self.fig.canvas.draw()
        # Keep running until the epidemic is over
        return self.model.datacollector.model_reporters["I"](self.model) > 0

# Main execution block
if __name__ == "__main__":
    G = nx.random_tree(100, seed = 1991)
    model_settings = dict(
        infection_chance = 1,
        recovery_chance = 0.1,
        initial_infected = 10,
    )
    animator = Animation(G=G, **model_settings)
    idx = 0
    while animator.step():
        animator.ax.set_title(f"T={idx}")
        idx += 1
        plt.pause(1e-23)  # need to pause to allow the plot to update
    plt.show(block=1)
