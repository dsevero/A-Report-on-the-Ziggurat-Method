Introduction
============

Pseudo-random number generators (PRNG’s) are crucial in the context of simulating noise in communication channels. We present a report on an efficient method for generating pseudo-random samples from any decreasing probability distribution called the Ziggurat Method. The initial idea was developed by , but has been enhanced by Marsaglia, Tsang and others. Specifically, we will show the latest and most efficient version presented by McFarland . In the latter paper, the method shows a speedup of over 3 times compared to traditional algorithms such as Marsaglia’s Polar Method . We present a speed comparison in C implemented on an Intel i7-4790 clocked at 3.60 GHz. McFarland provides all the necessary code to implement an *ad hoc* version of the algorithm, as well as a ready-to-use C code for a univariate Gaussian. A proof that the samples from this method are truly Gaussian is also provided.

Uniform region sampling
=======================

Prior to explaining the method, a prelude into a simple, yet important, mathematical result in probability theory is due. Most pseudorandom number generators operate on the principle that sampling a point *x* directly from the distribution in question, call it *g*, is equivalent to the following:

1.  Divide the region *A* under *g* into subregions *A*<sub>*i*</sub> such that $\\{A\_i, \\dotsb, A\_N\\}$ is a partition[1] of *A*.

2.  Randomly select a region *A*<sub>*i*</sub> with probability proportional to it’s area, *μ*(*A*<sub>*i*</sub>).

3.  Uniformly sample a point *p* = (*x*, *y*) from the selected region *A*<sub>*i*</sub>.

4.  Return *x*, since it will have distribution *g*.

The validity of this method can be simply proven. Let *I* be a random variable with distribution *f*<sub>*I*</sub>(*i*)=*μ*(*A*<sub>*i*</sub>)/*μ*(*A*)=*μ*(*A*<sub>*i*</sub>) that represents part 2. of the method presented above. If *P* = (*X*, *Y*) represents the points uniformly sampled in each region, then *f*<sub>*P*|*I*</sub>(*p*|*i*)=𝟙{*p* ∈ *A*<sub>*i*</sub>}/*μ*(*A*<sub>*i*</sub>).[2] We can now calculate *f*<sub>*P*</sub>(*p*)=*f*<sub>*X*, *Y*</sub>(*x*, *y*):
$$f\_P(p)=\\sum\_i f\_{P,I}(p,i)=\\sum\_i f\_I(i)f\_{P|I}(p|i)=\\sum\_i \\mu(A\_i)\\frac{\\mathbb{1}\\{p \\in A\_i\\}}{\\mu(A\_i)}=\\sum\_i \\mathbb{1}\\{p \\in A\_i\\}$$
 A specific point *p* can only belong to one subregion, since *A*<sub>*i*</sub> ∩ *A*<sub>*j*</sub> = ∅, ∀*i* ≠ *j*. Hence, we have that:
$$f\_P(p)=\\sum\_i \\mathbb{1}\\{p \\in A\_i\\} = \\mathbb{1}\\{p \\in A\_1\\} + \\mathbb{1}\\{p \\in A\_2\\} + \\dotsb + \\mathbb{1}\\{p \\in A\_N\\} = 1$$
*f*<sub>*X*</sub>(*x*)=∫<sub>*y*</sub>*f*<sub>*X*, *Y*</sub>(*x*, *y*)*d**y* = ∫<sub>0</sub><sup>*g*(*x*)</sup>*d**y* = *g*(*x*)
 The Ziggurat Method takes advantage of this result, by partitioning the region under *g* into subregions that are easier to sample from than *g* itself. A dataset generated from this method will have distribution *g* up to machine precision.

The Ziggurat Method
===================

The Ziggurat method uses the result from section \[ugs\] to quickly generate pseudorandom numbers from any decreasing distribution. The density in question, we will denote it as *g*, is partitioned into small rectangular layers of equal area such as in figure \[fig:zig\].

; coordinates <span>(2.3221253415052108722, 0.053829996928147945431) (0, 0.053829996928147945431)</span>; coordinates <span>(2.3221253415052108722, 0.053829996928147945431) (2.3221253415052108722, 0)</span>;

coordinates <span>(1.9563286553575721702, 0.11772519145881991813) (0, 0.11772519145881991813)</span>; coordinates <span>(1.9563286553575721702, 0.11772519145881991813) (1.9563286553575721702, 0.053829996928147945431)</span>;

coordinates <span>(1.6886556366482920007, 0.19174857271380732284) (0, 0.19174857271380732284)</span>; coordinates <span>(1.6886556366482920007, 0.19174857271380732284) (1.6886556366482920007, 0.11772519145881991813)</span>;

coordinates <span>(1.4526281686201162346, 0.27779949937230677675) (0, 0.27779949937230677675)</span>; coordinates <span>(1.4526281686201162346, 0.27779949937230677675) (1.4526281686201162346, 0.19174857271380732284)</span>;

coordinates <span>(1.2169036475136748573, 0.38051921777843910984) (0, 0.38051921777843910984)</span>; coordinates <span>(1.2169036475136748573, 0.38051921777843910984) (1.2169036475136748573, 0.27779949937230677675)</span>;

coordinates <span>(0.93836855027265858619, 0.51372913829813168844) (0, 0.51372913829813168844)</span>; coordinates <span>(0.93836855027265858619, 0.51372913829813168844) (0.93836855027265858619, 0.38051921777843910984)</span>;

coordinates <span>(0, 0.51372913829813168844)</span>;

coordinates <span>(0, 0.38051921777843910984)</span>;

coordinates <span>(0, 0.27779949937230677675)</span>; coordinates <span>(0, 0.19174857271380732284)</span>;

coordinates <span>(0, 0.11772519145881991813)</span>;

coordinates <span>(0, 0.053829996928147945431)</span>;

coordinates <span>(0.93836855027265858619, 0)</span>;

coordinates <span>(1.2169036475136748573, 0)</span>;

coordinates <span>(1.4526281686201162346, 0)</span>; coordinates <span>(1.6886556366482920007, 0)</span>;

coordinates <span>(1.9563286553575721702, 0)</span>;

coordinates <span>(2.3221253415052108722, 0)</span>;

Initially we must choose a number *N* of layers each with area 1/*N*. Given that the total area the layers occupy is equal to the area under *g*, we can not fit all of them under the curve *g*. We now define *L*<sub>*m**a**x*</sub> as the total number of layers that can be inserted under *g*. The leftover regions to the right of each layer, including the cap and tail of the distribution, now represent 1 − *L*<sub>*m**a**x*</sub>/*N* of the area under the distribution.

In the light of section \[ugs\], we may now think of this problem as region sampling under a defined distribution *g*, with *L*<sub>*m**a**x*</sub> rectangular regions, $R\_1, \\dotsb, R\_{L\_{max}}$ and one residual region *A*<sub>*R*</sub> representing all regions that remain outside the rectangles, such that:
$$A\_R=\\bigcup\_{i=1}^{L\_{max}+1} A\_i$$
 where *A*<sub>*i*</sub> are the actual leftover regions (one for each rectangular region), cap included. The method then has 2 levels, first it randomly chooses to sample either from a layer or from the residual region. If a rectangular layer is chosen, it returns a uniform sample. If the residual region is select, it then must first randomly pick a leftover region to sample from. For these regions, with the exception of the tail, rejection sampling is applied (see Appendix \[rsampling\]) to generate a uniform sample. If the tail is chosen, we use a fallback algorithm.

For the sake of illustration, we give an example for *N* = 256. We will denote the borders of each rectangular layer as *x*<sub>*i*</sub>, where the top layer (under the cap) is *x*<sub>*L*<sub>*m**a**x*</sub> + 1</sub> and the one that has the tail to the right of it is *x*<sub>1</sub>. The area of each rectangle will be 1/256. From simulations with the code provided in section \[implementation\]. we know that *L*<sub>*m**a**x*</sub> = 253, so the total residual area will be 3/256. We now do the following:

1.  Sample an integer *i* uniformly between 1 and *N* = 256.

2.  If *i* ∈ \[1, *L*<sub>*m**a**x*</sub> = 253\], return *x* uniformly from region \[0, *x*<sub>*i*</sub>). (This represents the layers).

3.  Else, sample an integer *j* ∈ \[1, 254\] with probability *p*(*j*)=*μ*(*A*<sub>*j*</sub>)/*μ*(*A*<sub>*R*</sub>).

    1.  If *j* = 1, return a sample *x* from the tail.

    2.  Else, apply Rejection Sampling to get a uniform sample *x* from region *j*.

To implement this method we require 3 look-up tables. One for the ziggurat lengths *x*<sub>*i*</sub> and heights *y*<sub>*i*</sub> = *g*(*x*<sub>*i*</sub>), as well as the area of leftover regions *A*<sub>*j*</sub>. We also need a uniform generator to output the values of *i*, *j* and *x*.

Since each region is selected with probability proportional to it’s area, the method will generate samples *x* with distribution *g*, according to section \[ugs\].

Implementation and Speed
========================

McFarland has made available all the necessary codes to be used in C, Python and MATLAB. It can be found at <https://bitbucket.org/cdmcfarland/fast_prng>. We have also uploaded a Python script that generates all the necessary tables (*x*<sub>*i*</sub>, *y*<sub>*i*</sub> = *g*(*x*<sub>*i*</sub>) and *A*<sub>*j*</sub>) for any given bin size *N*: <https://www.dropbox.com/s/lk2bj8vxk04pnzj/generate_tables.py>.

The header file *normal.h* that has been made available by , and is available at the hyperlink above, can be readily inserted into any C code. It provides a function *normal\_setup()* that must be called to initialize the pseudo-random number generator and *normal()* can be used to sample numbers from a univariate Gaussian distribution (*μ* = 0 and *σ*<sup>2</sup> = 1). The area of the bins used to generate this specific code was 1/256.

With respect to speed, the Ziggurat algorithm implemented in C for *N* = 256, is over 4 times faster than the tradition polar method , running on an Intel i7-4790 clocked at 3.60 GHz with 16 GB of RAM. Since *normal()* generates a univariate Gaussian, we compared the speed of computing *σ* \* *n**o**r**m**a**l*() + *μ* (also in C) to the one of reapplying the Ziggurat algorithm to a *μ*,*σ* Gaussian. No significant performance improvements were seen. McFarland provides other speed comparisons in different programming languages.

Appendix
========

Here we present some useful results, with proofs, related to Rejection Sampling and hand-picked probability distributions. We assume that the reader is familiar with introductory level calculus and probability theory.

Rejection Sampling
------------------

; ; coordinates <span>(-0.1, 0.50025) (-0.1, 0)</span>; coordinates <span>(-0.1, 0.36) (-0.1, 0)</span>; ; ; \[g\_label\] coordinates <span>(-0.1, 0.50025)</span>; coordinates <span>(-0.1, 0.2)</span>; coordinates <span>(-0.1, 0)</span>;

Given two known distributions *g* and *h* defined over the same interval *A* ⊆ ℝ. We can create a dataset distributed according to *h*, by sampling only from *g*, if the following is done:

1.  Choose a number *k* ∈ ℝ<sup>+</sup> such that *k**g*(*a*)≥*h*(*a*),∀*a* ∈ *A*.

2.  Sample a point *x* from *g*.

3.  Sample a number *y* from the distribution *U**n**i**f**o**r**m*\[0, *k**g*(*x*)\].

4.  If *y* &lt; *h*(*x*) add it to the dataset, otherwise discard it.

We will call this the *Rejection Sampling Algorithm (RSA)*.

To show that the resulting dataset is distributed according to *h*, we may represent the sample points previously mentioned, *x* and *y*, by the random variables *X* ∼ *f*<sub>*X*</sub>(*x*)≡*g*(*x*) and *Y*, defined over a conditional distribution *f*<sub>*Y*|*X*</sub>(*y*|*x*)=*U**n**i**f**o**r**m*\[0, *k**g*(*x*)\], respectively. Also, define *Z* = 𝟙{*Y* &lt; *h*(*X*)} such that if the sample *y* is under the curve *h*, then *Z* takes on the value 1, otherwise 0. Now, since *Y* obeys a uniform distribution, we have that:

$$f\_{Z|X}(z=1|x)=\\frac{h(x)}{kg(x)}$$

Consider now the pair (*X*, *Z*) where (*X*, *Z* = 1) represents the sample points *X* that we will keep according to the RSA. Looking at the joint distribution:
$$f\_{X,Z}(x,z=1)=f\_X(x)f\_{Z|X}(z=1|x)=g(x)\\frac{h(x)}{kg(x)}=\\frac{1}{k}h(x)$$
 we find that it distributes according to a multiple of *h*(*x*), hence the dataset will have distribution *h*.

We may now discuss some interesting observations related to the Rejection Sampling Algorithm. Consider first the probability of keeping a generated value:
$$f\_Z(z=1)=\\int\_A f\_{X,Z}(x,z=1)dx=\\frac{1}{k}\\int\_A h(x)dx=\\frac{1}{k}$$
 Knowing this, it is interesting to define *k* = min<sub>*κ* ∈ ℝ<sup>+</sup></sub>(*κ**g*(*a*)≥*h*(*a*),∀*a* ∈ *A*), i.e. as the smallest *k* ∈ ℝ<sup>+</sup> such that *g* is still above *h*. This way, we maximize the probability of keeping a generated value, thus minimizing computational efforts.
Let *P* = (*X*, *Y*) be a random variable taking on values *p* ∈ *A* × \[0, *k**g*(*x*)\], i.e. *P* takes on values under curve *g* (union of red and green regions of figure \[fig:RSA\]). The joint distribution of *P* is:
$$f\_P(p)=f\_{X,Y}(x,y)=f\_X(x)f\_{Y|X}(y|x)=g(x)\\frac{1}{kg(x)}=\\frac{1}{k}$$
 from which we conclude that the RSA is equivalent to uniformly sampling points (*x*, *y*) under *g* and keeping only those that also fall under *h*. The *x* coordinates of the stored points will have distribution *h*.

Piecewise sampling
------------------

Consider the following problem statement: given a distribution *g*, is it possible to divide *g* into functions *g*<sub>1</sub>, ..., *g*<sub>*N*</sub> such that sampling from these functions (in a specific way) is equivalent to sampling from *g*? Initially we will consider that $g=\\sum\_{i=1}^N g\_i$ and we denote each region as *A*<sub>*i*</sub> ⊆ *A* as well as the area under each curve *g*<sub>*i*</sub> as *π*<sub>*i*</sub>. Also the support of *g* is $A=\\bigcup\_{i=1}^N A\_i$.

coordinates <span>(-0.15, 0.31856) (-0.15, 0)</span>; coordinates <span>(-0.3, 0.16219) (-0.3, 0)</span>; coordinates <span>(0.1, 0.3609) (0.1, 0)</span>; coordinates <span>(0.38, 0.09414) (0.38, 0)</span>; ; coordinates <span>(-0.4, 0)</span>; coordinates <span>(-0.225, 0)</span>; coordinates <span>(-0.015, 0)</span>; coordinates <span>(0.245, 0)</span>; coordinates <span>(0.44, 0)</span>;

We propose that the following algorithm solves the problem in question:

1.  Sample *ω* from *g*

2.  For *ω* ∈ *A*<sub>*i*</sub>, sample *x* from *g*<sub>*i*</sub>/*π*<sub>*i*</sub>.

If the above algorithm is followed, then *X* will have distribution *g*. To prove that this is so, we define a random variable *Z* taking on values $z\\in\\{1,\\dotsb,N\\}$ such that if *ω* ∈ *A*<sub>*i*</sub> then *z* = *i*. In other words, *Z* indicates to which region *ω* belongs to. Now, we know that:
*f*<sub>*Z*</sub>(*z*)=*P*\[*ω* ∈ *A*<sub>*z*</sub>\]=∫<sub>*A*<sub>*z*</sub></sub>*g*(*x*)*d**x* = ∫<sub>*A*<sub>*z*</sub></sub>*g*<sub>*z*</sub>(*x*)*d**x* = *π*<sub>*z*</sub>
 Also, the joint distribution of *Z* and *X* is:
$$f\_{Z,X}(z,x)=f\_Z(z)f\_{X|Z}(x|z)=\\pi\_z\\frac{g\_z(x)}{\\pi\_z}=g\_z(x)$$
 Since *X* is what we are interested in, we now investigate it’s distribution:
$$f\_X(x)=\\sum\_z f\_{Z,X}(z,x)=\\sum\_{z=1}^N g\_z(x)=g(x)$$
 This result shows that we may sample from the decompositions $g\_1,\\dotsb,g\_N$ and still obtain a dataset with distribution *g*. Although this result is general, it says nothing of how it could be used to efficiently generate numbers from *g* since part 1. of the algorithm requires that we sample from *g* itself. This can be solved by considering the particular case in which the areas *π*<sub>*i*</sub> all have the same value. This area can be trivially calculated in the following way: since *g* is a distribution we know that:
$$\\int\_A g(x)dx=\\int\_A \\sum\_{i=1}^N g\_i(x)dx=\\sum\_{i=1}^N \\int\_{A\_i} g\_i(x)dx=N\\int\_{A\_i} g\_i(x)dx=1$$
$$\\int\_{A\_i} g\_i(x)dx=\\frac{1}{N}$$
 Since each region now has equal area, sampling *y* from *g* and checking the region in which *y* has fallen into is equivalent to randomly generating an integer from the set $\\{1,\\dotsb,N\\}$ and using it as *z*. We can now rewrite the original algorithm as:

1.  Sample *z* uniformly from $\\{1,\\dotsb,N\\}$.

2.  Sample *x* from *N**g*<sub>*z*</sub>

The formal verification of this algorithm is straightforward:
$$f\_Z(z)=\\frac{1}{N}$$
*f*<sub>*X*|*Z*</sub>(*x*|*z*)=*N**g*<sub>*z*</sub>(*x*)
$$f\_X(x)=\\sum\_z f\_{X,Z}(x,z) = \\sum\_z f\_Z(z)f\_{X|Z}(x|z)=\\sum\_z \\frac{1}{N}Ng\_z(x)=g(x)$$
 This result is useful as long as it is easier to sample from $g\_1,\\dotsb,g\_N$ than it is from *g*. The Ziggurat method takes advantage of this and the fact that very efficient uniform pseudorandom number generators are available in most programming languages to create a simple algorithm to quickly generate samples from any decreasing density .

<span>9</span>

George Marsaglia, “A convenient method for generating normal variables.”, SIAM Rev. 6, 260-264, 1964.

George Marsaglia, Wai Wan Tsang, “A fast, easily implemented method for sampling from decreasing or symmetric unimodal density functions”, SIAM Journ. Scient. and Statis. Computing, 5, 349-359, 1984.

George Marsaglia, Wai Wan Tsang, “The Ziggurat Method for Generating Random Variables”, Journal of Statistical Software, 2000.

Christopher D. McFarland, “A modified ziggurat algorithm for generating exponentially- and normally-distributed pseudorandom numbers.”, Apr. 2014.

[1] This means that $A=\\bigcup\_{i=1}^N A\_i$ and *A*<sub>*i*</sub> ∩ *A*<sub>*j*</sub> = ∅ for all *i* ≠ *j*.

[2] 𝟙{*x*}=1 if *x* is true and 0 if it is false.
