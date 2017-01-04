---
layout: post
title: Nanopores part 0, Introduction to nanopores and the electrical double layer
category: Science, Physics
comments: True
---

_This is part one of a multi-part introduction series on studying nanopore phenomena with COMSOL._

### Nanopore?
The most precise definition of nanopore: a hole with opening diameter on the order of 1 nm in size. I'll be the first to admit that this definition is a little dry, but there are a number of reasons, both academic and practical, that make nanopores worth studying. Nanopores exist naturally in nature, where they can be found in cells' membranes and act as channels that allow water, ions, and biomolecules to pass through. Many natural nanopores have interesting transport properties; for example, potassium ions diffuse freely through a potassium channel while sodium ions are blocked, despite the two ions being nearly identical in size and charge. This type of transport regulation is made possible by the pore's shape and its interior surface charge.

It is also possible to fabricate synthetic nanopores, which can be created using electron beam drilling, carbon nanotubes, and chemical etching, to name a few. One distinct advantage of synthetic pores is the ability to tailor their geometry to the application at hand; biological pores have a fixed size and shape. There are a number of different applications for both types of nanopores, including creating ionic circuits, water desalination, DNA sequencing, and biomolecule detection and characterization. Going back to the basic definition of nanopores 'a 1 nm in diameter hole', it is not immediately apparent why they are able to perform in all these applications. It turns out that the key is in something called the 'electrical double layer'. In the rest of this blog post we'll look into the properties of the nanopores, and in the [next post](https://tphinkle.github.io/blog/2016-11-1-nanopores_pt1) we'll explore why the EDL is responsible for nanopore's novel transport properties.

### The electrical double layer
In the bulk, a symmetric ion solution is composed of equal parts cation and anion and the total solution charge is neutral. As we approach a charged surface, the electric potential from the surface makes it more energetically favorable for ions of the opposite polarity--counterions--to populate the solution compared to coions. This region of net charge in the solution, approximately within ~1 nm of the surface, is known as the __electrical double layer__ or EDL. Suppose we have a charged cylindrical nanopore of variable radius; the following plot shows the fractional volume of the EDL compared to the bulk.

<img src="http://tphinkle.github.io/files/2017-1-3-nanopores_pt0/fractional_volume.png" alt="fractional volume" style="width: 480px;" align="middle"/>

Notice that at around 100 nm the fraction of the ion solution within the EDL becomes appreciable and rapidly increases as the pore shrinks further into the nanoscale. For this reason, even though we typically define nanopores as holes around 1 nm in size, nanopore-like behavior can exist for pores having diameters of tens of nanometers.

#### Derivation

We can understand the formation of the electrical double layer as a competition between diffusion (chemical potential) and electrostatic forces (electric potential). 

Consider an infinite planar surface with constant surface charge $$\sigma$$, and a solution composed of water and two types of oppositely charged ions with the same valency $$z$$ dissolved in the solution with bulk concentratoin $$C_{0}$$. We seek to find the number density of each ion species $$C^{+}$$ and $$C^{-}$$ in the solution. The relevant equations here are [Poisson's equation](https://en.wikipedia.org/wiki/Poisson's_equation) and the [Boltzmann distribution](https://en.wikipedia.org/wiki/Boltzmann_distribution).

$$
\begin{equation}
\tag{Poisson equation}
\nabla^{2}\psi=-\rho/\epsilon=-ze\left(C^{+}-C^{-}\right)/\epsilon
\end{equation}
$$

$$
\begin{equation}
\tag{Boltzmann distribution}
C^{\pm}=C_{0}e^{E^{\pm}/k_{B}T}=C_{0}e^{\mp ze\psi/k_{B}T}
\end{equation}
$$

In the above equations, $$\psi$$ is the electrostatic potential arising from the free ions and the surface charge, and $$\rho$$ is the net charge density at a given position. Note that because the boundary in our system is an infinite plane, we can reduce Poisson's equation to one-dimension, replacing the Laplace operator with a second derivative in one direction only, the $$x-$$direction. We combine the equations by inserting $$C^{\pm}$$ from the Boltzmann equation into the Poisson equation. Doing so, we arrive at the full __Debye-Hückel__ equation:

$$
\begin{equation}
\tag{Debye-H\"uckel equation}
\frac{d^2\psi}{dx^{2}}=\frac{2zeC_{0}}{\epsilon}\text{sinh}\left(\frac{ze\psi}{k_{B}T}\right)
\end{equation}
$$



