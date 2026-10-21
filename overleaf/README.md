# Overleaf Project: FairRecourse FAccT Paper

This directory contains the complete, compilation-ready LaTeX package for the research paper:  
**"Beyond the Illusion of Recourse: An Auditable Dual-Pathway Architecture for Actionable Credit Governance"**  
prepared for the **ACM Conference on Fairness, Accountability, and Transparency (ACM FAccT)** under the official ACM single-column anonymous review format (`\documentclass[manuscript,screen,review,anonymous]{acmart}`).

---

## 🚀 How to Import into Overleaf

### Option 1: Direct Zip Upload (Fastest & Recommended)
1. Download or locate [`overleaf/FairRecourse_FAccT_Overleaf.zip`](file:///c:/Users/aeshi/Desktop/FairRecourse/overleaf/FairRecourse_FAccT_Overleaf.zip).
2. Go to [Overleaf](https://www.overleaf.com/).
3. Click **New Project** $\to$ **Upload Project**.
4. Drag and drop `FairRecourse_FAccT_Overleaf.zip`.
5. In Overleaf project settings, ensure:
   - **Compiler:** `pdfLaTeX` (or `XeLaTeX` / `LuaLaTeX`)
   - **TeX Live Version:** `2023` or `2024`
   - **Main document:** `main.tex`
6. Click **Recompile**. Overleaf automatically includes `acmart.cls`.

### Option 2: Copy-Paste
1. Create a **Blank Project** in Overleaf named `FairRecourse_FAccT`.
2. Replace the contents of `main.tex` with the contents of [`overleaf/main.tex`](file:///c:/Users/aeshi/Desktop/FairRecourse/overleaf/main.tex).
3. Create a new file named `references.bib` in Overleaf and paste the contents of [`overleaf/references.bib`](file:///c:/Users/aeshi/Desktop/FairRecourse/overleaf/references.bib).
4. Click **Recompile**.

---

## 📄 Structure & Content Alignment

- **Document Format:**
  - `\documentclass[manuscript,screen,review,anonymous]{acmart}` (ACM single-column anonymous review format).
  - Authors and affiliations are anonymized for double-blind review.
  - Zero unresolved citation placeholders (`[?]`).

- **Section Breakdown (10 Research Sections):**
  1. **Section 1: Introduction:** Operationalization gap, Optimization Deadlock, locked research questions (RQ1, RQ2, RQ3), sociotechnical framing (allocating the burden of recourse).
  2. **Section 2: Background and Related Work:** Algorithmic recourse foundations, causal & actionable recourse, credit governance (ECOA/Reg B, FCRA, EU AI Act, GDPR Art. 22, RBI, Basel III/IV IRB Expected Loss), Table 1 Literature Matrix.
  3. **Section 3: Problem Formulation:** Scoring function, Definition 1 (Borrower Feasible Set), Definition 2 (Immutability Deadlock), Definition 3 (Institutional Feasible Set), Definition 4 (Dual-Pathway Recourse $R(x)$).
  4. **Section 4: FairRecourse Architecture:** Figure 1 (TikZ dual-pathway architecture diagram), coupled constraint set explanation, PCL referee (immutability, monotonicity, integrality, bounds), Temporal Solvency & execution horizon ($H_{\max} = 24$), $\epsilon$-stability with $\mathcal{R}_{\text{stab}}$ formula, Theorem 1 (Expected-Loss Preserving Exposure Sizing) + Proof Sketch.
  5. **Section 5: Experimental Methodology:** Table 2 (Dataset Overview: German Credit EUR, FICO HELOC USD, CIBIL Retail INR), data provenance and ethics statement, out-of-fold preprocessing & FICO sentinel preservation, baselines (Unconstrained DiCE, Bounded DiCE, FairRecourse), and metric decomposition ($S_B, S_I, S_H, S_R$).
  6. **Section 6: Results:** Table 3 (Primary Recourse Benchmark across all 670 applicants), explicit answers to RQ1, RQ2, RQ3 with denominators, Table 4 (Execution Horizon Sensitivity Analysis across $H_{\max} \in \{6, 12, 18, 24, 36\}$).
  7. **Section 7: Fairness and Sociotechnical Analysis:** Table 5 (Descriptive Subgroup Audit across gender, age, credit score tiers), mathematical analysis of the exposure disparity mechanism ($1 - \alpha^* = 1 - \tau/PD$), down-tiering vs. economic utility, governance standards (proportionality invariant, $\alpha_{\min} \ge 0.80$ floor).
  8. **Section 8: Limitations:** Risk-independence assumption, macroeconomic shifts, product calibration.
  9. **Section 9: Discussion:** Bilateral coordination between borrower agency and institutional capacity.
  10. **Section 10: Conclusion:** Summary of findings and paradigm shift for algorithmic recourse.
- **Acknowledgments:** Generative AI usage statement as required by ACM.
- **Appendices:**
  - **Appendix A:** Full algebraic proof of Theorem 1 (Expected-Loss-Constrained Exposure Scaling).
  - **Appendix B:** Table of exhaustive implementation rules of the Policy and Constraint Layer (PCL).
  - **Appendix C:** Comprehensive Metric Verification and Audit Traceability Table grounding every figure ($81/670$, $589/670$, $967$ violations, $269.8$ months, $1.3\%$–$19.8\%$, $670/670$).
