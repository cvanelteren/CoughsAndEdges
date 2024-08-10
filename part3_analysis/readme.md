# Part 3: Analysis and Visualization of SIR Model with Edge Dynamics

In this final part of the workshop, we'll analyze the SIR model with edge dynamics that you've implemented. We'll use various tools to gain insights into the model's behavior and the impact of edge dynamics on disease spread.

## Exercise: Analyzing and Visualizing Your Model

### Setup
1. Create a new Jupyter notebook or Python script for your analysis.
2. Import your SIREdgeModel and any necessary libraries (matplotlib, numpy, networkx, etc.).

### Tasks

1. **Basic SIR Curve Visualization**
   - Run your model for a suitable number of steps.
   - Plot the SIR curves (number of Susceptible, Infected, and Recovered agents over time).
   - Experiment with different initial conditions and parameters. How do they affect the curves?

2. **Network Visualization**
   - Create a visualization of your network at different time steps.
   - Color nodes based on their state (S, I, or R).
   - How does the network structure change over time due to edge dynamics?

3. **Edge Dynamics Analysis**
   - Plot the number of edges in the network over time.
   - Calculate and plot the average degree of nodes over time.
   - How do these metrics correlate with the progression of the disease?

4. **Comparative Analysis**
   - Run simulations with and without edge dynamics.
   - Compare the results. How do edge dynamics affect the speed and extent of disease spread?

5. **Parameter Sensitivity**
   - Create a heatmap showing how varying two parameters (e.g., infection rate and edge change rate) affects the peak number of infected individuals.
   - What insights can you draw from this analysis?

6. **Advanced: Cluster Analysis**
   - Implement a method to identify clusters in your network.
   - How does the number and size of clusters change over time?
   - Is there a relationship between cluster structure and disease spread?

7. **Your Own Analysis**
   - Based on what you've learned, devise and implement your own analysis or visualization that provides insight into the model's behavior.

### Tips
- Use Jupyter notebooks for an interactive analysis experience.
- Leverage libraries like matplotlib, seaborn, or plotly for rich visualizations.
- Consider using animations to show how the network and disease spread evolve over time.
- Don't hesitate to go back and modify your model if you need additional data for your analysis.

### Bonus Challenge
Create a dashboard (using tools like Dash or Streamlit) that allows users to interactively explore your model with different parameters and view the resulting analyses and visualizations in real-time.

Remember, the goal is to gain insights into how edge dynamics affect the spread of disease in your model. Be creative, and don't hesitate to explore beyond these suggestions!

When you're done, be prepared to share your most interesting findings with the group.
