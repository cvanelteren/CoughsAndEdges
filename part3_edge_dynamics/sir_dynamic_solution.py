# Same imports as part 2
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
import networkx as nx, numpy as np

# We need to add the correct path. Since we are not building a proper python package, we need to tell python where to find our initial implementation. We doo this by adding the path to the sys.path list
import sys; sys.path.append('../part2_network_model/')
from sir_solution import SIRAgent, SIRModel, Animation  # Assuming you've implemented this


# We make use of object orietned programming to extend the SIRAgent class and the SIRModel class. Our new classes will be called SIREdgeAgent and SIREdgeModel. Inherentance works by creating a new class that inherits the properties and methods of the parent class. We can then add new properties and methods to the new class. In this case, we will add a new property to the SIREdgeAgent class called is_wearing_mask. We will also add a new method to the SIREdgeAgent class called wear

# The main purpose of this file is to show how can quickly generate a complicated model in which we extend in a natural (humane way) an agent's capability to be more close to the real world. Some of the decisions here are not realistic, but they are made to show how to extend the model.
class SIREdgeAgent(SIRAgent):
    def __init__(self,
        unique_id: int,
        model: Model,
        wearing_mask: bool = False
    ):
        super().__init__(unique_id, model)
        self.is_wearing_mask = wearing_mask

    # we need to override the original step method to include the new behavior of wearing a mask
    def step(self):
        # store the current transmission rate; this gets potentially overriden by wearing the mask, we then restore this value at the end of this function
        orig_transmission = self.model.infection_chance

        # Mask wearing effect
        if self.wear_mask():
            # for n95 masks it removes 95 percent of the particles that would be transmitted. So we can lower the transmission rate by 0.95.
            self.model.infection_chance *= (1 - self.model_mask_effectiveness)
        # Quarantine behavior
        if (
            self.state == "I"
            and np.random.rand() < self.model.quarantine_probability
        ):
            self.quarantine()
        # Social distancing behavior
        if self.state == "S":
            self.social_distance()
        if self.model.grid.G.degree(self.unique_id)== 0:
            if self.state == "S" or self.state == "R":
                other = np.random.choice(self.model.grid.G.nodes)
                if other != self.unique_id:
                    self.model.grid.G.add_edge(self.unique_id, other)

        super().step()  # Call the base step method

        # Reset properties
        self.model.infection_chance = orig_transmission

    def quarantine(self):
        # Logic to remove some of the agent's edges
        if self.model.grid.G.degree(self.unique_id) > 0:
            deg = self.model.G.degree(self.unique_id)
            other = list(self.model.grid.G.neighbors(self.unique_id)).pop()
            self.model.grid.G.remove_edge(self.unique_id, other)
            assert self.model.G.degree(self.unique_id) < deg # this raises an error if the degree is the same or higher than before
            # Recursive call
            self.quarantine()

    def wear_mask(self):
        # Logic to reduce transmission probability
        frac_infected = self.get_general_health()
        frac_wearing_mask = self.get_neighbors_wearing_mask()
        # Wearing mask due to fear
        if frac_infected < np.random.rand():
            self.is_wearing_mask = True
        # Wearing mask due to social influence
        if frac_wearing_mask < np.random.rand():
            self.is_wearing_mask = True

    def get_neighbors_wearing_mask(self):
        # Helper function to get the fraction of neighbors wearing a mask. Is used as a social influence factor
        frac_wearing_mask = 0.0
        for neighbor in self.model.G.neighbors(self.unique_id):
            if self.model.agents[neighbor].is_wearing_mask:
                frac_wearing_mask += 1 / self.model.num_nodes
        return frac_wearing_mask

    def get_general_health(self):
        # Helper function to get the fraction of infected agents in the network. The purpose of this function is that each agent may "sense" how many agents are infected and adjust their behavior accordingly
        frac_infected = 0.0
        for agent in self.model.agents:
            if agent.state == "I":
                frac_infected += 1 / self.model.num_nodes
        return frac_infected

    def vaccinate(self):
        # Introduce a new state "V" which we call vaccinated.
        # There is no logic for the current "V" interaction with the other states. This is left as an exercise for the reader --> should there be an interaction? Or can we just leave it as is and the program will behave accordingly?
        self.state = "V" # Vaccinated

    def social_distance(self):
        # Logic to remove some of the agent's edges. The agent will remove an edge with a probability equal to the fraction of infected agents in the network
        frac_infected = self.get_general_health()
        if np.random.rand() < frac_infected:
            # Remove random edge
            n = self.model.grid.G.degree(self.unique_id)
            if n > 0:
                remove_idx = np.random.randint(0, n)
                other = list(self.model.grid.G.neighbors(self.unique_id))[remove_idx]
                self.model.grid.G.remove_edge(self.unique_id, other)


class SIREdgeModel(SIRModel):
    def __init__(
        self,
        G: nx.Graph,
        social_distance_sensitivity: float = 0.05,
        quarantine_probability: float = 1.0,
        mask_effectiveness: float = 0.95,
        initial_infected: int = 1,
        infection_chance: float = 0.1,
        recovery_chance: float = 0.01,
        mutation_chance: float = 0.00,
        social_limit: float = 0.0,
    ):
        # initialize the parent class such that the parameters are assigned based on our previous implementation
        super().__init__(
            G = G,
            initial_infected = initial_infected,
            infection_chance = infection_chance,
            recovery_chance = recovery_chance,
            mutation_chance = mutation_chance,
            agent_type = SIREdgeAgent,
        )
        self.quarantine_probability = quarantine_probability
        self.mask_effectiveness = mask_effectiveness
        self.social_distance_sensitivity = social_distance_sensitivity
        self.vaccination_is_discovered = False
        self.social_limit = social_limit


        # NOTE: override datacollector otherwise we get a memory collision. That is, the datacollector is tied to the parent object, which does not have access to the parameters of the child object
        self.datacollector = DataCollector(
            agent_reporters={"State": "state"},
            model_reporters={
                "S": lambda m: self.count_state(m, "S"),
                "I": lambda m: self.count_state(m, "I"),
                "R": lambda m: self.count_state(m, "R"),
                "States": lambda m: [a.state for a in m.agents],
                "V": lambda m: self.count_state(m, "V"),
                "edges": lambda m: self.count_edges(m)
            },
        )

    @staticmethod
    def count_edges(model: SIRModel) -> int:
        return model.grid.G.number_of_edges()

    def step(self):
        super().step()  # Call the base step method

        # Apply global social distancing
        if self.social_limit > 0:
            self.apply_social_distancing()

        # Optionally, apply vaccination program
        if self.vaccination_is_discovered:
            self.vaccination_program()

    def apply_social_distancing(self):
        # OPTIONAL: Logic to adjust the entire network's connectivity based on infection rate
        for agent in self.agents:
            agent.social_distance()

    def vaccination_program(self):
        # OPTIONAL: Logic to vaccinate part of the population
        agent = np.random.choice(self.model.agents)
        if agent.state != "I":
            self.agent.vaccinate()


if __name__ == "__main__":
   G = nx.random_tree(100, seed = 1991)
   model = SIREdgeModel(
       G,
       initial_infected = 10,
       infection_chance = 1,
       recovery_chance = 0.2,
       quarantine_probability = 1
   )
   animator = Animation(G=G, model = model)
   idx = 0
   while animator.step():
       animator.ax.set_title(f"T={idx}")
       idx += 1
       plt.pause(1e-23)  # need to pause to allow the plot to update
   plt.show(block=1)
   exit()
