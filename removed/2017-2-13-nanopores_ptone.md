---
layout: post
title: Nanopores part 1
category: Physics, nanopores
comments: True
---

_This is the second entry in a multi-part introductory series on nanopores._



In the [first post](https://tphinkle.github.io/) we introduced the electrical double layer, a thin layer of counter ions that forms in the vicinity of a charged surface. In this post, we'll introduce electroosmosis, which describes how constant electric fields can induce a bulk flow of water. This idea, while counterintuitive, is a direct consequence of the formation of the electrical double layer.

Before jumping into a nanopore-like cylindrical channel geometry, let's consider the EDL near an infinite planar sheet as in the derivation in the first post. The EDL near the walls is comprised of a larger population of counterions (ions with the opposite charge polarity of the surface) than coions. In any case, positive or negative, the imbalance between the two creates a net charge, as in the figure below.

Now, suppose we apply a transverse electric field across the surface of the plane. The electric field causes migration of the ions in all parts of the solution. In the bulk, cations are pushed in one direction and anions in the other, and their migration in turn pushes on the solvent molecules. However, because cations and anions exist in equal numbers in the bulk, these forces are equal in magnitude and therefore result in no net charge. However, in the EDL there *is* a net charge, and there will be more counterions migrated than coions. Due to the imbalance in teh migration of the ions, there *is* a net force on the solvent, and the result of the counterions migrating in the electric field results in the net flow of water in the EDL. The flow of water in the EDL is transferred to the bulk solution due to viscous forces. The end result is that a constant electric field induces the net flow of water---a neutral molecule! What's even more interesting is that this effect, which is entirely due to the 1 nm thick EDL, extends well into the bulk. This is what the electroosmotic profiles look like in the vicinity of a planar surface.

We can back up this intuitive explanation with some math and equations. To describe the flow of solution, we use the Navier-Stokes equations which yield the fluid flow vectors of incompressible fluids under forces.

$$
\frac{\nabla\mathbf{u}}{\nabla t}+\left(\mathbf{u}\cdot\mathbf{\nabla}\right)\mathbf{u}-\nu\mathbf{\nabla}^{2}\mathbf{u}=-\mathbf{\nabla}w+\mathbf{g},
$$

where $\mathbf{u}$ is the fluid velocity vector, $\nu$ is the kinematic viscosity of the solution, $w$ is an external pressure term, and $\vec{g}$ is the gravitational acceleration vector. Obviously this equation isn't pretty, but we can drastically simplify the equation fro our situation and come up with an analytical solution. First, there are no external pressure forces in our system and that, as is the case in nano- and microsystems, that gravitational acceleration is negligible. Next, assume our system has settled into equilibrium so that the fluid velocity is constant, i.e. $\frac{\nabla\mathbf{u}}{\nabla t} = 0$. Those three terms drop out of the equation, yielding

$$
\left(\mathbf{u}\cdot\mathbf{\nabla}\right)\mathbf{u}-\nu\mathbf{\nabla}^{2}\mathbf{u}=0.
$$
