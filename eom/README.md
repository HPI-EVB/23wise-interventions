# Effects of masks and other physical interventions

This project is mainly made up of the following Jupyter notebooks:

1. [`process_intranet.ipynb`](process_intranet.ipynb) \
   finds and analyzes interventions that were made at the hospital; produces a
   file `data/interventions.tsv` that is needed to use the other notebooks
2. [`interventions.ipynb`](interventions.ipynb) \
   creates a visual timeline of the interventions as found in the report (*figure
   1*)
3. [`employees.ipynb`](employees.ipynb) \
   visualizes and compares employee incidence with RKI data and produces the
   plot in *figure 2* of the report
4. [`analysis.ipynb`](analysis.ipynb) \
   runs the DID-model and plots the final results as found in *figure 3* of the
   report
