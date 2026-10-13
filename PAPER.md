# The Wright Question: Recursive Coherence as a Testable Extension of Einstein–Maxwell Dynamics

**Matthew Chenoweth Wright**  
Research proposal · October 2026

## Abstract

We define a falsifiable research program to test whether a proposed coherence state improves predictive modeling of interacting gravitational and electromagnetic systems. The program uses Einstein–Maxwell theory as the established baseline, applies Monolithic Zoo-style consistency gates, narrows the FieldSpace triplet atlas by explicit sector requirements, and performs interleaved ablations. A phenomenological reaction–diffusion model is introduced as a *candidate* coherence dynamics model. No new physical interaction is assumed established.

## 1. Established baseline

With signature (-,+,+,+), Einstein–Maxwell theory obeys

\[
G_{\mu\nu}+\Lambda g_{\mu\nu}=\frac{8\pi G}{c^4}(T^{EM}_{\mu\nu}+T^{other}_{\mu\nu}),
\]

\[
T^{EM}_{\mu\nu}=\frac1{\mu_0}\left(F_{\mu\alpha}F_{\nu}{}^\alpha-\frac14g_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right).
\]

In four dimensions, `T^EM` is traceless; for pure EM stress, `R=4Λ`, not `R∝radiation density`. The correct geodesic-deviation observable depends on `R^i_{0j0}`. Radiation-dominated flat FLRW cosmology with negligible Λ has `a(t)∝sqrt(t)`; it is a benchmark, not a novel EFMW prediction.

## 2. Wright's hypothesis

Wright's Emergentology proposes that feedback, constraint balancing and iterative correction organize collective dynamics. Define a **dimensionless** coarse-grained coherence variable `C(x,t)` and a **dimensionless, operationally specified** interaction observable `I[E,M](x,t)`. A candidate phenomenological equation is

\[
\partial_t C=D_C\nabla^2C-\gamma C+\alpha\,\mathcal I[E,M]-\beta C^3.
\]

Dimensions: `[D_C]=L²/T`, `[γ]=[α]=1/T`, `[β]=1/T` when `C` and `I` are dimensionless. The coefficients are not assumed universal. Boundary conditions and the definition of `I` must be preregistered per experiment.

This equation is **not** derived from Einstein–Maxwell or the original paper. Its value is in making an additional hypothesis testable.

## 3. Physical coupling and conservation gate

An auxiliary `C` that does not backreact on `g` or `F` is only a diagnostic or predictive state. A physical extension requires a diffeomorphism-invariant, dimensionally consistent action `S[g,A,C,...]` and variations with respect to the metric and gauge potential. The resulting stress tensor must obey the appropriate covariant conservation identity **jointly with** the other fields; gauge symmetry, causality, stability, and the GR limit must be checked. No such action is asserted here.

## 4. Zoo audit gates

1. Correct tensor rank and dimensions.
2. Trace and conservation consistency.
3. Well-posed initial/boundary value problem.
4. Numerical convergence and reproducibility.
5. Explicit counterexamples and limiting cases.
6. A priori baselines and independent test data.
7. Parameter identifiability and falsifiability.
8. Lean formalization of precisely stated mathematical propositions where useful; formal proofs alone do not validate nature.

The existing Zoo repo reports 46 animal modules but describes them as an uncompiled draft. This paper does not claim to have executed a complete 46-animal pass.

## 5. FieldSpace structural reduction

FieldSpace has 11 sectors: E (gravity), M (electromagnetism), S (gauge), and eight scalar sectors F,W,T,I,R,H,P,A. The 165 distinct triplets comprise all `C(11,3)` combinations. Exactly `C(10,2)=45` contain E. Exactly 9 contain both E and M: E–M–S and E–M–X for each of the eight scalars. This is a **selection criterion** for the GUTS question, not evidence that other triplets are false. The E+M two-sector baseline is not itself one of the triplets.

## 6. Ablation sequence

- B0: Einstein–Maxwell reference model without added coherence state.
- B1: diagnostic `C`, `α=0` (no interaction driving).
- B2: diagnostic `C`, `α≠0`, no physical backreaction.
- B3: candidate action-derived backreaction, only if a conserved, gauge-consistent formulation is provided.
- B4: one FieldSpace E–M–X extension at a time, subject to the same gates.

All models must be compared on common observables and held-out data. An increase in predictive accuracy for B2 is not evidence of a fifth force; B3 must yield a new, independently measured physical effect.

## 7. Model comparison

For comparable Gaussian measurement errors, use `χ²` with documented covariance and penalize parameter count (e.g. AIC=`χ²+2k` or BIC=`χ²+k ln n` under their assumptions). Prefer predictive log-likelihood on held-out datasets. Require confidence intervals and robust sensitivity to geometry, noise and numerical resolution.

## 8. Falsification and reporting

Reject or revise a candidate if it violates conservation or dimensions, fails preregistered tests, cannot beat a simpler baseline on independent data, or its extra coupling is unidentifiable. Report null results and parameter degeneracies. Distinguish mathematical theorem, numerical observation, and empirical physical result in every publication.

## Conclusion

Wright's question is whether recursive coherence offers a **distinct and measurable** mechanism. The proposed path does not assume that it does; it defines the evidence needed to decide.
