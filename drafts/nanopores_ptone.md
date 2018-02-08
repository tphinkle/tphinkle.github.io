---
layout: post
title: Nanopores part 1
category: Physics, nanopores
comments: True
---

_This is the second entry in a multi-part introductory series on nanopores._



In the [first post](https://tphinkle.github.io/) we introduced the electrical double layer, a thin layer of counterions that forms in the vicinity of a charged surface. In this post, we'll introduce electroosmosis, which describes how constant electric fields can induce a bulk flow of water. This idea, while counterintuitive, is a direct consequence of the formation of the electrical double layer.

Before jumping into a nanopore-like cylindrical channel geometry, let's consider the EDL near an infinite planar sheet as in the derivation in the first post. The EDL near the walls is comprised of a larger population of counterions (ions with the opposite charge polarity of the surface) than coions. In any case, positive or negative, the imbalance between the two creates a net charge, as in the figure below.

Now, suppose we apply a transverse electric field across the surface of the plane. The electric field causes migration of the ions in all parts of the solution. In the bulk, cations are pushed in one direction and anions in the other, and their migration in turn pushes on the solvent molecules. However, because cations and anions exist in equal numbers in the bulk, these forces are equal in magnitude and therefore result in no net charge. However, in the EDL there *is* a net charge, and there will be more counterions migrated than coions. Due to the imbalance in teh migration of the ions, there *is* a net force on the solvent, and the result of the counterions migrating in the electric field results in the net flow of water in the EDL. The flow of water in the EDL is transferred to the bulk solution due to viscous forces. The end result is that a constant electric field induces the net flow of water---a neutral molecule! What's even more interesting is that this effect, which is entirely due to the 1 nm thick EDL, extends well into the bulk. This is what the electroosmotic profiles look like in the vicinity of a planar surface.

We can back up this intuitive explanation with some math and equations. The flow of the solution is described by the [Navier-Stokes](www.navier-stokes.com) equation:

$$
\rho\left(\frac{\nabla\vec{u}}{\nabla t}+\vec{u}\cdot\vec{\nabla}\vec{u}\right)=-\vec{\nabla}p+\vec{\nabla}\cdot\left(\mu(\vec{\nabla}\vec{u}+\left(\vec{\nabla}\vec{u}\right)^{T}\right)+\vec{F}
$$

where $\rho$ is the density of the fluid, $\mathbf{u}$ is the fluid velocity vector, $\nu$ is the kinematic viscosity of the solution, $w$ is an external pressure term, and $\vec{F}$ is the force vector. Obviously this equation isn't pretty, but we can drastically simplify it by making some assumptions. First, assume that the system has settled into a steady-state, i.e. there is no time-dependence in the fluid flow, so that the derivative term drops out. Next, since we are at the micro/nanoscale we assume that viscous forces dominate inertial forces; in this case, the first term is negligible and can be struck from the equation. Finally, in our infinite-plane geometry we need only solve for the velocity of the fluid in the direction of the electric field, i.e., instead of solving for $\vec{u\left(x,y,z\right)}$ we solve for $u_{x}\left(z\right)$. Under these assumptions, the Navier-Stokes equation becomes:

$$
\left(\mathbf{u}\cdot\mathbf{\nabla}\right)\mathbf{u}-\nu\mathbf{\nabla}^{2}\mathbf{u}=0.
$$

The general solution to this differential equation is:

. To find the exact solution, we subject the above equation to the boundary conditions of our system:

1. $u\left(z=0\right)=0$ (no-slip boundary condition)

2. $\frac{\nabla u\left(z\right)}{\nabla z}\abs_{z->\infty} = 0$.

Finally, applying these boundary conditions to our system yields the final function form of the fluid velocity along the plane as a function of the perpendicular distance from the charged surface:

$Equation$

Qualitatively, a 'plug-flow' fluid velocity profile develops, which is basically just an exponential increase in the velocity away from the surface which asymptotes to the bulk velocity. Again, notice that counterintuitively the velocity does *not* die away from the surface. The reason for this is the constant force on the fluid in the electrical double layer, which propogates away from the surface due to viscous forces. The total work done by the electric forces in the electrical double layer is exactly cancelled by the viscous forces, as the following derivation shows:

$ Derivation $

I should mention that the above derivation, again, was for an infinite plate but can be generalized to ~largish nanopores. In reality, if we were to solve this problem for a nanopore system we would have to do so numerically: due to the non-trivial nature of the geometry, the ion distributions---and therefore the electric force on the fluid--- is more complicated. Conceptually however, the idea is the same.

Something else that should be pointed out is that in our above solution we assumed htat the fluid velocity is zero on the surface. This is the so-called 'no-slip' condition, which is implicitly assumed to be true in most systems but which is recently being challenged in some systems such as carbon nanotubes. Basically, the no-slip condition arises due to the collisions of the solvent molecules with the surface of the wall. At the atomic level, if these surfaces are jagged then on average we will have a random dispersion of water molecule momenta after collision---some reflect forward, others backward, but there is not net motion of water molecules at hte wal. However, this argument does not hold for surfaces that are atomically smooth, as is the case with non-defective crystalline structures, like in a carbon nanotube. Changing our non-slip boundary condition to a slip-condition, we find that the electroosmotic velocities take on teh same form, but with the potential with *far* greater magnitudes in the bulk solution. This has huge implications for transport in systems where non-slip does not hold up, as the water may flow so fast that it becomes the dominant force in teh system.
