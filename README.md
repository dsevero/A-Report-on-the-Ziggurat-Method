This repo. contains the results from my 3 month summer internship at the University of Toronto under the supervision of [Prof. Frank Kschischang](https://www.comm.utoronto.ca/~frank/) in 2014.

A Report on the Ziggurat Method
============
<!--ts-->
   * [A Report on the Ziggurat Method](#a-report-on-the-ziggurat-method)
   * [How to reference this repo.](#how-to-reference-this-repo)
   * [Files](#files)
   * [Compile LaTeX](#compile-latex)
   * [Abstract](#abstract)
   * [Related Work](#related-work)
   * [References](#references)

<!-- Added by: severo, at: Mon May 20 00:40:57 -03 2019 -->

<!--te-->

# How to reference this repo.
```
@misc{Severo2014,
  author = {Severo, D.},
  title = {A Report on the Ziggurat Method},
  year = {2014},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/dsevero/A-Report-on-the-Ziggurat-Method}},
  commit = {master}
}
```

# Files
- [Full report](pdf/A_Report_on_the_Ziggurat_Method.pdf)
- [Slides](pdf/A_Report_on_the_Ziggurat_Method-slides.pdf)

# Compile LaTeX
Run `make report` or `make slides` to compile the respective files from `tex/` to `build/`. You will need the following:

`apt install texlive latexmk texlive-fonts-extra texlive-pictures`

# Abstract
Pseudo-random number generators (PRNG's) are crucial in the context of simulating noise in communication channels. We present a report on an efficient method for generating pseudo-random samples from any decreasing probability distribution called the Ziggurat Method. The initial idea was developed by [1], but has been enhanced by Marsaglia, Tsang [3] and others. Specifically, we will show the latest and most efficient version presented by McFarland [4]. In the latter paper, the method shows a speedup of over 3 times compared to traditional algorithms such as Marsaglia's Polar Method [2]. We present a speed comparison in C implemented on an Intel i7-4790 clocked at 3.60 GHz. McFarland [4] provides all the necessary code to implement an _ad hoc_ version of the algorithm, as well as a ready-to-use C code for a univariate Gaussian. A proof that the samples from this method are truly Gaussian is also provided.

# Related Work
- [ZMG: Ziggurat Method Generator of Zero-Mean Gaussians.](https://www.comm.utoronto.ca/~frank/ZMG/)

# References
> [1] George Marsaglia, ”A convenient method for generating normal variables.”, SIAM Rev. 6, 260-264,1964.

> [2] George  Marsaglia,  Wai  Wan  Tsang,  ”A  fast,  easily  implemented  method  for  sampling  from  de-creasing or symmetric unimodal density functions”, SIAM Journ. Scient. and Statis. Computing,5, 349-359, 1984.

> [3] George  Marsaglia,  Wai  Wan  Tsang,  ”The  Ziggurat  Method  for  Generating  Random  Variables”,Journal of Statistical Software, 2000.

> [4]  Christopher  D.  McFarland,  ”A  modified  ziggurat  algorithm  for  generating  exponentially-  andnormally-distributed pseudorandom numbers.”, Apr. 2014.
