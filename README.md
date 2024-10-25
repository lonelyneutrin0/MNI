# Monte Carlo Integration
Monte Carlo Integration provides a method to estimate complex integrals through the random sampling of points. For a function $f(\mathbf x)$, the integral over an open space $D$ can be defined as $$I = \int_D f(\mathbf x) \mathbf \dd x$$. This can be approximated as a Riemann sum through the random sampling of N points and the corresponding function values- $$I \approx \frac{V}{N}\sum_{i=0}^N f(\mathbf x_i)$$ where $V$ is the volume of $D$ and $N$ is the number of points sampled. <br/> 
The accuracy of the approximation improves as $N \to \infty$ as expected. However, it can also be improved by using a non uniform probability distribution curve. 

$$ I \approx \int{\frac{f(\mathbf x)}{p(\mathbf x)} \dd \mathbf x} $$ Ideally, the probability distribution function should resemble the shape of the curve.
