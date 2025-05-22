# A model for the dynamics of human weight cycling

## Introduction

1. What is weight cycling

2. What is the model designed for?

## PQR model for weight cycling

1. Definition of the model
   1) Model representation (Fig.1)
      - $P$: body weight (in excess of a basal reference value)
        - increases with dietary intake $Q$  at a rate $aQ$
        - decreases due to energy dissipation at a rate that saturates at a maximum value $b$
      - $Q$: dietary intake
        - increase at a maximum rate $V_1$
        - decrease at a maximum rate $V_2R$.
      - $R$: cognitive restraint (the degree of resolution to lose weight, reduce the amount of dietary intake Q once weight P becomes too large)
        - increase at a maximum rate $V_3P$ caused by an increase in $P$.
        - decreases at a maximum rate $V_4$ due to habituation. 
      - Note:
        - **Range** of parameter values:
          - Both $Q$ and $R$ are normalized to vary between 0 and 1.
          - $P$ and $Q$ are expressed as amounts in excess of a reference value.
            - The healthy weight reached around the age of 21 corresponds to a certain value $P > 0$ that is specific to each individual. (Garn 1996; Meisler and St Jeor 1996) 
        - **Threshold functions** are built into the model equations  
          - for the dependence of R on P, and of Q on R, which reflect the fact that the decision to lose weight by reducing dietary intake is generally of a sudden, all-or-none nature. (**Dashed arrows** indicate the regulations exerted by P on R and by R on Q, respectively.)
          - Thus, 
            - The degree of cognitive restraint R increases abruptly once weight P passes a threshold value
            - Dietary intake Q decreases sharply once R exceeds a threshold level. 
            - Such thresholds, naturally associated with time delays, prove to be crucial for the occurrence of sustained oscillations.
        - In an appropriate range of parameter values, the PQR model gives rise to sustained oscillations of the limit cycle type corresponding to weight cycling.
      - **Thoughts**
        - Why 1-Q/1-R???
          - Both $Q$ and $R$ are normalized to vary between 0 and 1.
          - eqs (1b) and (1c) indicate that both Q and R vary in a reciprocal manner between two reservoirs, the constant sum of which remains equal to unity.
   2) Evolution Equations
        $$
        \begin{aligned}
            \frac{dP}{dt} &= aQ - b\frac{P}{K + P}\\
            \frac{dQ}{dt} &= V_1 \frac{(1-Q)}{K_1 + (1-Q)} - V_2 R \frac{Q}{K_2 + Q} \\
            \frac{dR}{dt} &= PV_3 \frac{(1-R)}{K_3 + (1-R)} - V_4 \frac{R}{K_4 + R} 
        \end{aligned}
        $$
        - Equations (1a) - (1c)
          - $P$ and $Q$ are controlled and vary in the course of time. **(Why R not???)**
          - a positive and a negative term measuring increases or decreases, respectively.
        - Equation (1a)  for $P$ (above the reference value) 
          - An increase is linked to the excess $Q$
            - with a proportionality constant, a measuring metabolic efficiency $a$
          -  decreases with a metabolic energy dissipation rate
             - characterized by a **Michaelian function** ($M$) 
               - The Michaelis-Menten type is encountered in enzyme kinetics, where the reaction rate initially rises with the level of substrate and reaches a maximum value when the substrate level becomes large.
             - reaches a maximum value, b, when the excess $P$ is much larger than the constant $K$
               - $K$ measures the value of $P$ yielding half-maximum rate. 
             - Similar results are obtained when the sink for $P$ is of a linear form ($–bP$).          
           - parameters $a$ and $b$ have a metabolic meaning
             - They measure how weight P increases with food intake Q 
             - or decreases autonomously due to energy dissipation.
       - Equation (1b) for $Q$
         - increase at a maximum rate $V_1$ multiplied by a $M$ function
           - $(1-Q)$ as substrate: the smaller $Q$ (i.e. the stronger the restriction), the stronger the ‘craving’ to increase dietary intake. 
           - The tendency to increase food intake diminishes as $Q$ tends to its maximum value equal to unity. 
         - decrease at a maximum rate $V_2R$, multiplied by a $M$ function
           - $Q$ as substrate
           - proportional to cognitive restraint
         - Parameters $V_1$ and $V_2$ respectively  measure the tendency of $Q$ to increase with orexigenic signals or to decrease with anorexigenic signals and with cognitive restraint $R$
         - In the absence of coupling to cognitive restraint, $P$ and $Q$ would settle to a stable steady state for a given set of parameter values.
       - Equation (1c) for $R$
         - increases in a Michaelian manner with $(1-R)$
           - at a maximum rate $V_3P$
           - proportional to weight
         - decreases at a maximum rate $V_4$ multiplied by a Michaelian function 
           - R as substrate. 
           - reflects a loss of cognitive restraint in the course of time due to a process of habituation
           - $V_3$ and $V_4$ have a psychological  nature and measure the rate at which $R$ increases with $P$ or wanes in the course of time.
       - Why Michaelian functions?
         - these functions are saturable
           - i.e. they increase from zero up to a plateau corresponding to a maximum value, and therefore cannot grow in an explosive manner. 
           - Thus, the rate of decrease in Q triggered by anorexigenic signals rises with Q up to a maximum value, while the rate of increase in Q triggered by orexigenic signals diminishes from a plateau and goes to zero as Q increases from zero up to its maximum value. 
         - it naturally produces a threshold in the dependence of Q on R at steady state (fig.2B). 
           - This result is based on prior work on biochemical systems controlled by protein covalent modification, where thresholds originate from similar equations involving two antagonistic enzyme reactions which obey Michaelis-Menten, saturable kinetics (see below).

   3) Threshold values of P and R
       - The phenomenological eqs (1b) and (1c) ensure that at steady state $R$ and $Q$ exhibit a threshold dependence on $P$ and $R$

