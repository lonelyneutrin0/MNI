# Monte Carlo Integration
Monte Carlo Integration provides a method to estimate complex integrals through the random sampling of points. For a function $f(\mathbf x)$, the integral over an open space $D$ can be defined as 
```math
I = \int_D f(\mathbf x) d \mathbf x
```
 This can be approximated as a Riemann sum through the random sampling of N points and the corresponding function values- 
```math
I \approx \frac{V}{N}\sum_{i=1}^N f(\mathbf x_i)
```
 where $V$ is the volume of $D$ and $N$ is the number of points sampled. <br/> 
The accuracy of the approximation improves as $N \to \infty$ as expected. However, it can also be improved by using a non uniform probability distribution curve. 

```math
I = \int{\frac{f(\mathbf x)}{p(\mathbf x)} d \mathbf x} \approx \frac{1}{N}\sum_{i=1}^N \frac{f(\mathbf x)}{p(\mathbf x)} 
```
 Ideally, the probability distribution function should resemble the shape of the curve.

 <br/> This class was created for use in my [Quantum Monte Carlo Methods](https://github.com/lonelyneutrin0/QMC) repository. 
