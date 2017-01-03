---
layout: post
title: Understanding nanopores with Python and COMSOL, Part 0: Nanopores and the Electrical double layer
category: Science, Physics
comments: True
---

_This is part one of a multi-part introduction series on studying nanopore phenomena with COMSOL._

### Nanopore?
The most precise definition of nanopore: a hole with opening diameter on the order of 1 nm in size. I'll be the first to admit that this definition is a little dry, but there are a number of reasons, both academic and practical, that make nanopores worth studying. Nanopores exist naturally in nature, where they can be found in cells' membranes and act as channels that allow water, ions, and biomolecules to pass through. Many natural nanopores have interesting transport properties; for example, potassium ions diffuse freely through a potassium channel while sodium ions are blocked, despite the two ions being nearly identical in size and charge. This type of transport regulation is made possible by the pore's shape and its interior surface charge.

It is also possible to fabricate synthetic nanopores, which can be created using electron beam drilling, carbon nanotubes, and chemical etching, to name a few. One distinct advantage of synthetic pores is the ability to tailor their geometry to the application at hand; biological pores have a fixed size and shape. There are a number of different applications for both types of nanopores, including creating ionic circuits, water desalination, DNA sequencing, and biomolecule detection and characterization. Going back to the basic definition of nanopores 'a 1 nm in diameter hole', it is not immediately apparent why they are able to perform in all these applications. It turns out that the key is in something called the 'electrical double layer'. In the rest of this blog post we'll look into the properties of the nanopores, and in the [next post](https://tphinkle.github.io/blog/2016-11-1-nanopores_pt1) we'll explore why the EDL is responsible for nanopore's novel transport properties.

### The electrical double layer
In the bulk, a symmetric ion solution is composed of equal parts cation and anion and the total solution charge is neutral. As we approach a charged surface, the electric potential from the surface makes it more energetically favorable for ions of the opposite polarity--counterions--to populate the solution compared to coions. This region of net charge in the solution, approximately within ~1 nm of the surface, is known as the __electrical double layer__ or EDL. Suppose we have a charged cylindrical nanopore of variable radius; the following plot shows the fractional volume of charge in the EDL compared to in the bulk.

<img src="http://tphinkle.github.io/files/2016-11-6-nanopores_pt0/fractional_volume.png" alt="fractional volume" style="width: 480px;" align="middle"/>

Notice that at around 100 nm the fraction of the ion solution within the EDL becomes appreciable, and rapidly increases as the pore shrinks further into the nanoscale. For this reason, even though we typically define nanopores as holes around 1 nm in size, nanopore-like behavior can exist for pores having diameters of tens of nanometers.

We can understand the formation of the electrical double layer as a competition between diffusion (chemical potential) and electrostatic forces (electric potential). Consider an infinite planar surface with constant surface charge $\sigma$, and a solution composed of water and two types of oppositely charged ions dissolved in the solution with concentrations $C^{+}_{0}$.

**Cite Israelichaveli**













### What is COMSOL?
COMSOL is a software application that allows you to simulate different types of physics using something called the [finite element method](https://en.wikipedia.org/wiki/Finite_element_method), or FEM. The basic idea behind FEM is that you create a geometric fascimile of the system you want to study, break it down into many smaller parts, solve the relevant equations in each part, and stitch the solutions together at the end. This allows you to solve really complex physical situations that can't be handled analytically. There are people (programmers, physicists) that spend their whole academic careers developing these methods, and others, the 'consumers', that are just concerned with getting answers. COMSOL is great for the latter camp because it does not require extensive knowledge about the FEM method to get started.

One thing I think COMSOL is useful for is gaining an intuition about processes that aren't very easily understandable. In this post I'll talk about 5 interesting phenomena surrounding my area of research, nanopores, using COMSOL. Data was generated entirely from COMSOL, and the plots are a mix of some taken from COMSOL, and others made using Python and matplotlib.

# 1. The electrical double layer
The EDL is the basis for everything whacky and counter intuitive that occurs in nanopores. When a charged surface comes in contact with a conducting medium, like electrolyte solution, free charges in the conducting medium redistribute to screen the charge of the surface. More specifically, charges of the same polarity (coions) are repelled from the surface while charges of the opposite polarity (counterions) are attracted. This screening layer is known as the electrical double layer, and typically ranges between 0.1 and 10 nm. The EDL can greatly influence the behavior of a system, especially in nanoscale systems where the total volume within 1 nm of a charged surface is significant. Another interesting thing to point out is that the 'importance' of surface effects scales like $1/R$, where R is the system size (e.g. diameter). One way to see this is to plot the volume fraction that is within $\lambda_{D}$ as a function of system size, as in the plot below. 

The plot shows that even at $\sim 20$ nm, the EDL is still only a small fraction of the total volume. However, past that point the fraction within $\lambda_{D}$ rises sharply.

Debye-Hückel theory predicts the ion and potential distributions in the vicinity of the charged surface, under the assumptions that the surface's electric potential are not too large and that ion-ion correlations can be ignored. Here are the equations for the ion charge and electric potential:


And here's a plot showing how the ion concentrations change in the vicinity of a charged surface according to Debye-Hückel.



Some key things to highlight:
1. The concentration of counterions (ions of the opposite charge polarity of the surface) is greater than bulk concentration in the EDL
2. Coions (ions of the same charge polarity) are reduced in number in the EDL
3. From 1. and 2. it follows that the **the solution has a net charge near the charged surface**
3. The *total* ion concentration remains equal to the bulk everywhere
3. Concentrations and electric potential exponentially approach their bulk values as we move away from the charged surface, with a characteristic decay length known as the 'Debye length' $\lambda_{\text{D}}$. Another important parameter is the $\zeta$-potential ('zeta'), the electric potential at the surface's slip plane, which is effectively a measure of the surface's charge.
4. $lambda_{\text{D}}$ is independent of the surface charge value, but depends on the bulk ion concentration--larger bulk ion concentration screens the surface charge over a small distance.

That's all there is to the EDL according to Debye-Hückel, but let's see if COMSOL can confirm what we already know.

# 2. Electroosmosis
Electroosmosis is when water flows in an electrical field. This effect is surprising, since water is a neutral molecule and in a constant electric field shouldn't experience any force. The explanation from the effect comes from the EDL. Ions migrate in an electric field, and drag water molecules along with them. In the bulk, positive and negative ions move in opposite directions, so their is no net flow of water. However, as we've just seen there *is* a net charge polarity in the EDL, and due to the charge imbalance there, there is similarly a drag imbalance that can cause the net motion of water. This is electroosmosis. What's interesting is that this effect doesn't exist only in the EDL, but extends into the bulk.

# 3. Ion current saturation
If we connect two large, electrolyte reservoirs with a constricted channel we effectively have the ionic equivalent of an electronic resistor circuit. The reservoirs play the role of wires and the constricted channel the resistor. Applying a voltage across the constriction will generate an ionic current, with its magnitude determined by the conductance properties of the resistor. If the constriction is nano-sized, then the conductance of the resistor is influenced by the conductance properties of the EDL, due to surface charges on the channel surface. One interesting thing about this is that if we reduce the ion concentration we expect the total conductance of the resistor to drop as well. Less charges, less current. But, if the entire volume of the nanochannel is filled with EDL, then this drop cannot occur since the total charge still has to be screened! As a result, there is a threshold concentration below which reducing the bulk ion concentration does not reduce the conductance of the channel. This is known as ion current saturation, and occurs when an EDL 'overlap' occurs, where the EDL's of opposite sides of the channel overlap.

To demonstrate this, let's calculate IV curves of a simulated cylindrical nanochannel using COMSOL for a range of ion concentrations. We can calculate the resistance R from the slope of each IV curve and plot it against the ion concentration. We should find an approximately linear relationship until the saturation point, at which point the resistance does not change with any further reduction in the ion concentration.

We can also 

# 4. Ion current rectification

Ion current rectification (ICR) refers to a difference in nanopore conductance at opposite voltage polarities, which looks something like this in an IV curve:




