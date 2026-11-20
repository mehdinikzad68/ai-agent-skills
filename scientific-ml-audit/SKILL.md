---
name: scientific-ml-audit
description: Enforces rigorous scientific validity, experimental design auditing, data leakage prevention, and zero-hallucination citation rules for Machine Learning, Computer Vision, Spectroscopy, and Biology projects. Trigger this skill alongside coding or planning skills whenever dealing with datasets, model training, statistical evaluation, spectral/biological signals, or academic literature.
---

# Scientific Validity & ML Audit Skill

## 1. Core Mandate: Technical vs. Scientific Validity
A pipeline that runs without Python exceptions and achieves a $99\%$ accuracy score can still be scientifically invalid. Never confuse **technical execution** (code runs) with **scientific validity** (results are statistically sound, reproducible, and free of leakage or confounding).

---

## 2. Mandatory Experimental Audit Checklist
Whenever designing, reviewing, or debugging ML, Computer Vision, Spectroscopy, or Biological data pipelines, actively audit for the following threats:

### A. Splitting & Data Leakage (High Priority)
- **Entity/Sample Independence:** Ensure splits (`train` / `validation` / `test`) are grouped by **biological sample, patient, batch, or physical specimen** (`GroupKFold` / `StratifiedGroupKFold`), never by random row-level or frame-level splitting when multiple spectra, crops, or replicates come from the same physical source.
- **Preprocessing Leakage:** Verify that all scalers, normalizers, PCA, baseline corrections (e.g., SNV, Savitzky-Golay derivatives, EMSC in spectroscopy), and imputers are fitted **strictly on the training split** and only transformed on validation/test splits.

### B. Domain-Specific Confounders (Spectroscopy, CV, Biology)
- **Batch Effects & Instrument Drift:** Check if target labels correlate with measurement date, plate/run ID, ambient temperature, sensor calibration drift, illumination changes, or background substrate.
- **Spectral & CV Artifacts:** In spectroscopy, check whether the model is learning water/solvent absorption bands, cosmic spikes, or baseline scatter instead of chemical features. In CV, check if the model relies on background texture, vignette, or resolution differences rather than the biological region of interest (ROI).

### C. Reproducibility & Provenance Metadata
Require or enforce logging of the following metadata for any model evaluation:
1. **Dataset Provenance & Version:** Origin, filtering criteria, outlier removal justification, and hash/version.
2. **Split Strategy & Seeds:** Exact splitting logic, class distribution per split, and fixed random seeds (`random`, `numpy`, `torch`, etc.).
3. **Metric Alignment:** Ensure evaluation metrics match the scientific and clinical/industrial reality (e.g., Matthews Correlation Coefficient $\text{MCC}$, Precision-Recall AUC for imbalanced classes, $R^2$, $\text{RMSECV}$, $\text{RMSEP}$, and Ratio of Performance to Deviation $\text{RPD}$ for quantitative spectroscopy).
4. **Baseline Comparison:** Always compare complex models (Deep Learning/Transformers) against simple, interpretable domain baselines (e.g., PLS-DA, PLSR, Ridge/Lasso, Random Forest, or classical thresholding).

---

## 3. Zero-Hallucination Citation & Literature Policy
- **Absolute Prohibition:** Never guess, fabricate, or extrapolate DOIs, paper titles, author lists, publication years, statistical benchmarks, or biochemical/physical constants.
- **Verification Statement:** If a scientific claim, benchmark, or reference cannot be verified directly from provided project documents or live search tools, state explicitly:
  > *"این ادعا یا رفرنس نیازمند راستی‌آزمایی مستقل و جستجوی مستقیم در منابع علمی است (Requires independent verification or source search)."*
- **Distinguishing Evidence Levels:** Clearly label whether a recommendation is based on:
  - **[Empirical Data]:** Proven in the user's current dataset/logs.
  - **[Established Domain Standard]:** Standard chemometric/biostatistical methodology.
  - **[Hypothesis]:** A plausible scientific hypothesis requiring experimental validation.

---

## 4. Scientific Audit Output Block
When reviewing or planning an experiment, append a concise **Scientific Validity Gate** block:
- **Leakage Risk:** `[Low | Medium | High]` + Explanation of grouping/preprocessing boundary.
- **Confounder / Drift Risk:** Specific physical, biological, or instrumental variables to control.
- **Baseline & Metric Check:** Chosen baseline model and primary evaluation metrics.
- **Reproducibility Status:** Missing seeds, dataset versions, or pipeline logs required before trusting results.