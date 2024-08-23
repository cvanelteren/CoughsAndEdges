<div style="display: flex; align-items: center; justify-content: space-between;">
    <h1 style="margin: 0;">Summer School 2024 - Complex Adaptive Systems</h1>
    <img src="./figures/applied_complexity.png" style="margin-right: 70%; width: 35%;" alt="Applied Complexity">
</div>

You’ve reached the  landing page for the  RIVM Summer School
2024 on  Complex Systems Modeling. This  session is designed
to introduce you to the fascinating world of complex systems
modeling. Aimed  at beginners  to intermediate  learners, we
will   guide  you   through  implementing,   analyzing,  and
enhancing a complex system.

Our approach is hands-on, so be  prepared to dive in and get
your hands dirty. By the end of the session, you will have:

-   Implemented an SIR model
-   Added edge dynamics to the model
-   Conducted some preliminary analyses

Check out  the detailed schedule  below to see what  we have
planned.  We  look  forward  to a  productive  and  engaging
session with you!

# Table of Contents

1.  [Part 1: Exact Analysis of the SIR Model](#orga2515fe)
2.  [Part 2: Implementing SIR on a Network](#orgae70a18)
3.  [Part 3: Implementing Social Distancing](#orgb01ce91)
4.  [Wrap-up and discussion](#orgb01ce91)
4.  [Key Takeaways](#org62df5e8)

<a id="org223bd63"></a>
## Welcome and Overview
-  Greeting: Welcome to the workshop! We’re excited to dive into the SIR model with edge dynamics together.
-  Session Goals: Our aim is to build and analyze an SIR model enhanced with edge dynamics. Here’s how we’ll break down our time:
    -  Part 1: Implementing the SIR model
    -  Part 2: Adding edge dynamics
    -  Part 3: Analyzing the model and discussing insights
-  Breaks: We’ll take two 15-minute breaks to keep our energy up and ensure we have ample time to reflect and discuss.

![timeline](./figures/flatten_curve.png)

Feel free to  ask questions at any point.  Let’s get started
and  explore  the  dynamics  of  the  SIR  model  with  edge
dynamics!


<a id="orga2515fe"></a>

# Part 1: Exact Analysis of the SIR Model
The SIR model is one of the simplest models used to describe
the  spread of  infectious  diseases. In  this  part of  the
workshop, we  will implement the  SIR model and  analyze its
behavior. The  model is  part of a  family of  models called
compartemental  models,  which  divide the  population  into
different  compartments.  Rather  than  modeling  the  nitty
gritty details of each  individual, we model the population,
and the different stages an individual can be in. In the SIR
model, an individual can be in one of three possible states:
Susceptible, Infectious,  or Recovered. The  model describes
the interaction  between these different  compartements. Two
different rates controle how  likely a susceptible indivdual
could transfer into an infected individual, and the infected
to recovered.

The SIR model knows  many different extentions and variants.
In  this workshop  we will  focus on  the basic  form as  it
already  shows  some   non-intuitive  behavior  where  small
effects can blosom to big effects.

# Part 2:  Adding a Social Network

-   Environment Setup and Model Overview
    -   **Environment  Preparation**: We’ll  start by  setting up
        the  necessary environment.  A Git  repository will  be
        provided   with   all   the   required   packages   and
        dependencies.
    -   **SIR Model  Background**: I’ll give a  brief overview of
        the   SIR   (Susceptible-Infectious-Recovered)   model,
        explaining   its  purpose   and   how   it’s  used   in
        epidemiological modeling.
-   Hands-On Coding
    -   **Activity**:  You’ll begin  implementing the  base SIR
        model. This will involve writing code to simulate the
        spread  of  an  infectious   disease  using  the  SIR
        framework.
    -   **Support**:  I’ll  be  available to  assist  with  any
        questions or  issues you might encounter  during this
        coding session.
-   Break
    -    **Purpose**:  Take a  short  break  to refresh  and
    discuss any  immediate questions  or thoughts  about the
    first part of the session.


<a id="orgae70a18"></a>

# Part 3: Adding some Edge Dynamics: Social Distancing
Agents  are not  static, they  move! One  of the  key pillar
during  the  COVID  pandemic was  social  distancing,  where
agents limit the number of interactions as well as whom they
interact with. In this  section, we will
explore the effects  of dynamic agents on the  ability for a
disease to spread.

- Introduction to Networks
 -  **Concept Explanation**:  We’ll  discuss  the basics  of
   network  theory  and  how  it can  be  applied  to  model
   interactions between individuals in a population.
 -  **Activity**: You’ll  learn  how to  represent a  social
   network   in  code   and  visualize   it  using   network
   visualization tools such as networkx and matplotlib.
-  Break
    -   **Purpose**: Take another break to relax, ask questions, or discuss what we’ve covered so far.


<a id="orgb01ce91"></a>
# Wrap-up
You  have  reached the  end  of  our too-short  workshop  on
epidemic modeling. You  are now wondering, "Great,  how do I
continue this epic tale?" The  world of epidemic modeling is
vast, and  we have only reached  the tip of the  mountain of
knowledge that lies  underneath. Agent-based modeling offers
a  natural framework  to  explore the  intricacies of  human
behavior. It emphasizes the relationship to the "other" with
evolving and emerging dynamics.  This flexibility comes with
a cost, however. Agent-based models tend to include too much
detail,  making the  model  complex (and  slow)  to run  and
understand.  Additional  complexity   does  not  necessarily
entail improved accuracy or understanding.

In your modeling  process, you should always ask,  "Why am I
adding  parameter X,  and how  does  it allow  me to  better
predict or understand Y?" Striking the right balance between
detail and simplicity is key.  As you move forward, consider
the purpose  of each element  you include in your  model and
how it contributes to the overall goals of your study.

Remember,  the  journey  in epidemic  modeling  doesn’t  end
here—it’s just the beginning. There are countless resources,
research papers, and communities  dedicated to advancing the
field.  Continue  experimenting, questioning,  and  refining
your models. With persistence  and curiosity, you'll uncover
deeper  insights and  perhaps  even contribute  to the  next
generation of epidemic models.  Keep pushing the boundaries,
and enjoy the process of discovery.

I leave you now with two profound quotes from the greate scientists of the past. See you in a future workshop!

> All models are wrong, but some are useful.
>>George P.A. Box


> With four parameters I can fit an elephant, and with five I can make him wiggle his trunk.
>> John von Neumann


<a id="org62df5e8"></a>
# Key Takeaways
-   **Simplification  Strategy**:  Emphasize the  importance  of
    starting with  a simple  model and adding  complexity only
    when necessary.
-   **Troubleshooting**: If you  encounter difficulties, attempt
    to simplify the model to better understand the issues.
-   **Understanding**: Ensure  you fully understand  the current
    model before proceeding. Make  sure that the added details
    are necessary and useful for your analysis.
