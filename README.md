# EFMW Research Program: Wright's Emergence Question

**Author:** Matthew Chenoweth Wright  
**Status:** Proposed research program; mathematical and experimental validation pending.

This flat-root GitHub repository defines a falsifiable program linking the corrected *I Have Guts. Eureka.* Einstein–Maxwell baseline, the Monolithic Zoo audit, the FieldSpace 165-triplet atlas, and Wright's proposed recursive-coherence dynamics.

## Central question

Does recursive emergence supply an independently identifiable physical mechanism, or is it a useful computational description of already-established dynamics?

## Sources

- [FieldSpace](https://github.com/enuminous/FieldSpace): 11 sectors, 165 triplets; physical current/stress closure and empirical validation outstanding.
- [Monolithic Zoo Lean4](https://github.com/enuminous/Monolithic-Zoo-Lean4): 46 operational contracts; README describes the formalization as an uncompiled draft.
- [Post-156 Zoo Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit): distinguishes kernel-checked structural claims from physical laws.
- [Original January 2025 paper](https://medium.com/@enuminous/i-have-guts-eureka-69981769787e).

## Files

- `index.html`: GitHub Pages landing page.
- `PAPER.md`: full proposal with equations, assumptions, and falsification gates.
- `PROTOCOL.md`: experimental plan and ablation matrix.
- `MODEL.py`: executable illustrative numerical toy model.
- `test_model.py`: tests for the toy model.
- `requirements.txt`: dependencies (none; Python standard library only).
- `CITATION.cff`: citation metadata.

## Run

```bash
python3 MODEL.py
python3 -m unittest -v test_model.py
```

## Scope boundary

The synthetic model does **not** demonstrate a new force, quantum gravity, a novel physical law, or AGI. The 165→45→9 reduction is a structural filter, not empirical rejection. An effective coherence field must have a defined observable and action-derived coupling before claiming gravitational backreaction.

## GitHub Pages

Upload all files to the root of `enuminous/Research-Program`, then enable Pages from `main` / root.
