This repo. contains the results from my 3 month summer internship at the University of Toronto under the supervision of [Prof. Frank Kschischang](https://www.comm.utoronto.ca/~frank/) in 2014.

A Report on the Ziggurat Method
============
<!--ts-->
   * [A Report on the Ziggurat Method](#a-report-on-the-ziggurat-method)
   * [Files](#files)
   * [Abstract](#abstract)
   * [Related Work](#related-work)
   * [References](#references)

<!-- Added by: severo, at: Fri May 17 00:25:31 -03 2019 -->

<!--te-->

# Files
- [Full report](pdf/A_Report_on_the_Ziggurat_Method.pdf)
- [Slides](pdf/A_Report_on_the_Ziggurat_Method-slides.pdf)

# Abstract
Pseudo-random number generators (PRNG’s) are crucial in the context of simulating noise in communication channels. We present a report on an efficient method for generating pseudo-random samples from any decreasing probability distribution called the Ziggurat Method. The initial idea was developed by , but has been enhanced by Marsaglia, Tsang and others. Specifically, we will show the latest and most efficient version presented by McFarland . In the latter paper, the method shows a speedup of over 3 times compared to traditional algorithms such as Marsaglia’s Polar Method . We present a speed comparison in C implemented on an Intel i7-4790 clocked at 3.60 GHz. McFarland provides all the necessary code to implement an *ad hoc* version of the algorithm, as well as a ready-to-use C code for a univariate Gaussian. A proof that the samples from this method are truly Gaussian is also provided.

# Related Work
- [ZMG: Ziggurat Method Generator of Zero-Mean Gaussians.](https://www.comm.utoronto.ca/~frank/ZMG/)

# References
[1] George Marsaglia, ”A convenient method for generating normal variables.”, SIAM Rev. 6, 260-264,1964.
[2] George  Marsaglia,  Wai  Wan  Tsang,  ”A  fast,  easily  implemented  method  for  sampling  from  de-creasing or symmetric unimodal density functions”, SIAM Journ. Scient. and Statis. Computing,5, 349-359, 1984.
[3] George  Marsaglia,  Wai  Wan  Tsang,  ”The  Ziggurat  Method  for  Generating  Random  Variables”,Journal of Statistical Software, 2000.
[4]  Christopher  D.  McFarland,  ”A  modified  ziggurat  algorithm  for  generating  exponentially-  andnormally-distributed pseudorandom numbers.”, Apr. 2014.
