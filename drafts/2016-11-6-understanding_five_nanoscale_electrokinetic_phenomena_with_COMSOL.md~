---
layout: post
title: Understanding five electrokinetic phenomena in nanopores with COMSOL
category: Science, Physics
comments: True
---

COMSOL is a software application that allows you to simulate different types of physics using something called the [finite element method](https://en.wikipedia.org/wiki/Finite_element_method), or FEM. The basic idea behind FEM is that you take the system that you want to understand, break it down into many smaller parts, solve the relevant equations in each region, and stitch the solutions together at the end. This allows you to solve really complex physical situations that can't be handled analytically. There are people (programmers, physicists) that spend their whole academic careers developing these methods, and others, the 'consumers', that are only concerned about the answer. COMSOL is great for the latter camp because it does not require extensive knowledge about the FEM to get started. Since it's GUI based, you can build a model following your intuition and get results out quickly.

One thing I think COMSOL is useful for is gaining an intuition about processes that aren't very easily understandable. In this post I'll talk about 5 interesting phenomena surrounding my area of research, nanopores, using COMSOL. Data was generated entirely from COMSOL, and the plots are a mix of some taken from COMSOL, and others made using Python and matplotlib.

# 1. The electrical double layer
The EDL is the basis for everything whacky and counter intuitive that occurs at the nanoscale. When a charged surface comes in contact with a conducting medium, like electrolyte solution, free charges in the medium will redistribute to screen the charge of the surface. More specifically, charges of the same polarity are repelled from the surface while charges of the opposite polarity are attracted. If you calculate the thickness of the screening layer, the EDL, it's approximately 1 nm. The EDL can greatly influence the behavior of a system, especially in nanoscale systems where the total volume within 1 nm of a charged surface is significant.

Debye-Huckel theory predicts the ion and potential distributions in the vicinity of the charged surface, under the assumptions that the surface's electric potential are not too large and that ion-ion correlations can be ignored. Here are the equations for the ion charge and electric potential:


And here are what these two functions look like plotted:

Some key things to highlight:
1. The concentration of counterions (ions of the opposite charge polarity of the surface) is greater than bulk concentration in the EDL
2. Coions (ions of the same charge polarity) are reduced in number in the EDL
3. Concentrations and electric potential exponentially approach their bulk values as we move away from the charged surface, with a characteristic decay length known as the 'Debye length' $\lambda$.
4. $lambda$ is independent of the surface charge value, but depends on the bulk ion concentration--larger bulk ion concentration screens the surface charge over a small distance.

The results are pretty self-explanatory so there's not a ton to explore with COMSOL, but let's take a look at the EDL that COMSOL comes up with for a few different combinations of surface-charge and ion concentration.


# 2. Ion current saturation
If we connect two large, electrolyte reservoirs with a constricted channel we effectively have the ionic equivalent of an electronic resistor circuit. The reservoirs play the role of wires and the constricted channel the resistor. Applying a voltage across the constriction will generate an ionic current, with its magnitude determined by the conductance properties of the resistor. If the constriction is nano-sized, then the conductance of the resistor is influenced by the conductance properties of the EDL. One interesting thing about this is that if we reduce the ion concentration we expect the total conductance of the resistor to drop as well, since there are simply less ions to conduct. However, if the entire volume of the nanochannel is filled with EDL, then this drop cannot occur since the total charge still has to be screened! As a result, there is a saturation concentration at which reducing the bulk ion concentration does not reduce the conductance of the channel. This is known as ion current saturation, and occurs when an EDL 'overlap' occurs, where the EDL's of opposite sides of the channel overlap.

To demonstrate this, let's take IV curves of a simulated cylindrical nanochannel using COMSOL for a range of ion concentrations. We can calculate the resistance R from the slope of each IV curve and plot it against the ion concentration. We should find an approximately linear relationship until the saturation point, at which point the resistance does not change with any further reductions in the ion concentration.


