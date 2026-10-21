import io
import os
import sys
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Read original document into memory to avoid file locks
with open('FairRecourse-Abstract.docx', 'rb') as f:
    doc_bytes = f.read()

doc = docx.Document(io.BytesIO(doc_bytes))
print(f"Loaded FairRecourse-Abstract.docx: {len(doc.paragraphs)} paragraphs.")

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_shading(cell, color_hex):
    shading_elm = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_elm)

def update_para(p, new_text, bold=None, italic=None, size_pt=None):
    p.text = new_text
    for r in p.runs:
        r.font.name = 'Calibri'
        if bold is not None:
            r.font.bold = bold
        if italic is not None:
            r.font.italic = italic
        if size_pt is not None:
            r.font.size = Pt(size_pt)

# =========================================================================
# 1. Title & Abstract (P0, P4, P6, P8)
# Must Do #1 (Dual-Pathway Architecture), Must Do #2 (Metric Decomposition S_B, S_I, S_R),
# Must Do #3 (Harmonize 87.9% overall / 93.8% HELOC / 967 violations), Must Do #4 (No hallucination)
# =========================================================================
p6_text = (
    "To bridge this operational gap, this paper introduces an auditable, dual-pathway recourse architecture designed for "
    "regulated consumer lending. Rather than treating recourse as a borrower-only optimization problem, we challenge the unilateral "
    "assumption in retail credit underwriting: when an applicant's profile cannot be resolved through feasible borrower actions alone "
    "(F_B(x) = \u2205), an institution-aware framework must transition to an admissible institutional counter-offer (F_I(x) \u2260 \u2205). "
    "First, we establish a deterministic Policy and Constraint Layer (PCL) that formalizes non-negotiable underwriting rules, "
    "regulatory mandates (FCRA, ECOA), and directional monotonicity boundaries as a composite mathematical predicate. "
    "Second, we formalize the 'Immutability Deadlock' across distinct credit environments, contrasting contractual application regimes\u2014"
    "where bilateral loan parameters permit borrower-side restructuring\u2014with pure historical bureau telemetry, where backward-looking "
    "records strictly preclude unilateral intervention. Third, we formalize the dual-pathway recourse framework: for solvable applicants, "
    "it models realistic borrower-side balance reduction bound by temporal solvency horizons (H \u2264 H_max = 24 months); for deadlocked "
    "applicants, it automatically computes risk-constrained institutional counter-offers that scale credit exposure according to the applicant's "
    "calibrated probability of default (PD) to preserve portfolio expected loss."
)
update_para(doc.paragraphs[6], p6_text)
print("Updated P6 (Abstract Core Thesis).")

p8_text = (
    "We evaluate our framework against unconstrained counterfactual baselines (DiCE) across three representative benchmarks: "
    "Statlog German Credit (N=34 marginal applicants), FICO HELOC (N=260), and central bureau telemetry (CIBIL Retail, N=376), "
    "totaling N=670 audited borderline applicants. Auditing baseline counterfactuals reveals that unconstrained DiCE fails compliance on "
    "87.9% of applicants across all cohorts (and 93.8% on HELOC, where compliant success is only 6.2%), generating 967 total policy infractions "
    "and unviable paydown schedules reaching 269.8 months. Decomposing resolution into borrower-side recourse (S_B) and institutional "
    "counter-offers (S_I), FairRecourse achieves S_B = 100.0% (Option A) and 50.0% (Option B) on German Credit, but collapses to S_B = 3.8% "
    "on HELOC and S_B = 0.0% on CIBIL due to immutable bureau records. For deadlocked applicants, risk-constrained institutional exposure scaling "
    "resolves the remaining cases (S_I = 96.2% on HELOC, S_I = 100.0% on CIBIL at mean facility haircuts of 14.30% and 10.83%), achieving a "
    "combined admissible resolution rate of S_R = 100.0% across all benchmarks with zero policy infractions. These results demonstrate "
    "that actionable credit governance requires coordinating borrower-side interventions with institutional exposure sizing."
)
update_para(doc.paragraphs[8], p8_text)
print("Updated P8 (Abstract Empirical Audit & Decomposition).")

# Fix math notation in Section 1.1 (P18)
p18_text = (
    "where d(x, x') denotes an \u2113_1, \u2113_2, or Mahalanobis distance metric, f(x') represents the predictive scoring function "
    "(calibrated default probability), and \u03c4 signifies the operational target threshold for a favorable decision (f(x') \u2264 \u03c4)."
)
update_para(doc.paragraphs[18], p18_text)
print("Updated P18 (Section 1.1 Distance & Threshold notation).")

# =========================================================================
# 2. Section 1.3 Four Formal Contributions (P31 - P36)
# =========================================================================
p31_text = (
    "To reconcile post-hoc algorithmic explainability with prudential credit risk management and statutory banking requirements across "
    "global jurisdictions, we propose FairRecourse and advance four formal contributions:"
)
update_para(doc.paragraphs[31], p31_text)

p32_text = (
    "1. The Policy and Constraint Layer (PCL): We formalize a deterministic verification engine that functions as an auditable firewall "
    "against unconstrained counterfactual search. The PCL explicitly encodes domain immutability allowlists, directional monotonicity boundaries "
    "(prohibiting debt accumulation or asset depletion), discrete integrality of trade counts, and physical bounds as a coupled, composite mathematical predicate C(x, x')."
)
update_para(doc.paragraphs[32], p32_text)

p33_text = (
    "2. Basel-Aligned Expected-Loss Constraint & Risk-Constrained Exposure Sizing (\u03b1*): We challenge the borrower-only assumption in credit recourse. "
    "Anchored in the fundamental expected loss invariant (E[Loss] = PD \u00b7 LGD \u00b7 EAD), we prove that when borrower-side attribute adjustments "
    "encounter an immutability deadlock (F_B(x) = \u2205), scaling credit exposure via \u03b1* = min(1.0, \u03c4 / PD_calibrated) guarantees that portfolio "
    "expected loss remains strictly within institutional capital limits, establishing a closed-form bridge between an infeasible search and an institutional counter-offer (F_I(x) \u2260 \u2205)."
)
update_para(doc.paragraphs[33], p33_text)

p34_text = (
    "3. Temporal Solvency & Feasibility Metrics: We derive a dynamic valuation translation function converting abstract utilization deltas into "
    "nominal currency commitments bounded by realistic retail credit ceilings (C_inferred \u2264 6 \u00b7 Income). We formalize the Execution Horizon metric "
    "bounded by an institutional parameter H \u2264 H_max (baseline H_max = 24 months) and formalize recourse stability under stochastic execution perturbations "
    "as an explicit probability metric Stab(x') = P_{\u03b5 ~ N(0, \u03a3)}(f(x' + \u03b5) \u2264 \u03c4 \u2227 C(x, x' + \u03b5) = 1)."
)
update_para(doc.paragraphs[34], p34_text)

p35_text = (
    "4. Multi-Regime Empirical Audit (N=670): We evaluate the framework across three representative credit regimes: Statlog German Credit "
    "(Contractual, N=34 marginal applicants), FICO HELOC (Revolving Bureau, N=260), and central bureau telemetry (CIBIL Retail, N=376), "
    "totaling N=670 audited near-miss applicants."
)
update_para(doc.paragraphs[35], p35_text)

p36_text = (
    "We formally disaggregate adverse action resolution into Borrower Recourse Success (S_B), Institutional Counter-Offer Resolution (S_I), "
    "and Combined Admissible Resolution (S_R = S_B + S_I). We document that unconstrained DiCE incurs 967 total policy infractions across 87.9% of applicants "
    "(and 93.8% on HELOC). Crucially, we demonstrate that borrower recourse alone achieves only S_B = 3.8% on HELOC and S_B = 0.0% on CIBIL due to rigid bureau anchors, "
    "while FairRecourse achieves S_R = 100.0% total compliant resolution by safely routing deadlocked applicants to institutional counter-offers (mean haircuts of 14.30% and 10.83%) with zero policy infractions."
)
update_para(doc.paragraphs[36], p36_text)
print("Updated Section 1.3 Contributions (P31-P36).")

# =========================================================================
# 3. Section 2 Retitling & Terminology (P41, P46, P49)
# Must Do #5 (Retitling Regulatory & Basel Terminology)
# =========================================================================
update_para(doc.paragraphs[41], "2.2 Prudential Underwriting and Basel-Aligned Expected-Loss Constraint")
update_para(doc.paragraphs[46], "2.3 The Binary Underwriting Fallacy and Institutional Counter-Offers")

p49_text = (
    "When an underwriter evaluates an adverse applicant whose calibrated default probability PD(x) marginally exceeds threshold \u03c4, "
    "the interaction rarely ends in an unconditional deadlock. Instead, credit institutions routinely issue a conditional sanction or counter-offer "
    "with restructured terms (e.g., US Regulation B, 12 C.F.R. \u00a7 1002.9(a)(1)(iv); EU Consumer Credit Directive conditional sanctions; "
    "RBI Fair Practices Code). By scaling the facility limit (\u03b1* = EAD* / EAD_0), the institution neutralizes portfolio expected loss "
    "without requiring unilateral borrower-side manipulation. Recourse architectures that optimize solely over borrower features ignore "
    "this primary institutional mechanism."
)
update_para(doc.paragraphs[49], p49_text)
print("Updated Section 2.2 and 2.3 Terminology (P41, P46, P49).")

# Section 3.2 P63
p63_text = (
    "Prescribing a multi-decade horizon against an institutional planning benchmark (H \u2264 H_max = 24 months) renders the advice economically inexecutable."
)
update_para(doc.paragraphs[63], p63_text)

# =========================================================================
# 4. Section 4 Architecture & Mathematical Formalization (P71, P74, P76, P77, P78, P86, P89, P91, P99, P101, P103, P108-P110)
# Must Do #6 (Formalizing PCL composite predicate & feasible sets),
# Strong #7 (Parameterizing H_max), Strong #8 (Formalizing Stab(x') probability metric)
# =========================================================================
p71_text = (
    "The FairRecourse framework operates as an institutional underwriting and adverse action auditing pipeline. The pipeline ingests applicant "
    "bureau profiles, applies out-of-fold feature normalization and missing-value sentinel preservation, and routes data to a Platt-calibrated "
    "LightGBM risk engine. If the calibrated default probability exceeds operational threshold \u03c4 = 0.40, the system branches into a dual-pathway "
    "recourse solver governed by the deterministic Policy & Constraint Layer (PCL). Rather than viewing baseline failures as terminal denials, "
    "when borrower-side actionable recourse is mathematically obstructed (F_B(x) = \u2205), the engine activates the Exposure Scaling Engine (F_I(x) \u2260 \u2205), "
    "issuing a Basel-aligned, risk-constrained institutional counter-offer that preserves portfolio expected loss."
)
update_para(doc.paragraphs[71], p71_text)

p74_text = (
    "Standard recourse models optimize over an independent bounding box [l_j, u_j], ignoring inter-feature relationships. FairRecourse replaces "
    "this with a deterministic verification engine\u2014the Policy & Constraint Layer (PCL)\u2014that evaluates candidate counterfactuals x' against a coupled, "
    "composite mathematical predicate:"
)
update_para(doc.paragraphs[74], p74_text)

# P75: Make sure the composite predicate formula is clear
update_para(doc.paragraphs[75], "C(x, x') = C_imm(x, x') \u2227 C_disc(x') \u2227 C_mono(x, x') \u2227 C_temp(x, x') \u2227 C_risk(x')", bold=True)

p76_text = (
    "Immutability Predicate (C_imm(x, x')): Freezes protected demographic attributes X_dem (e.g., age, sex, marital status) and historical "
    "bureau telemetry X_hist (e.g., historical delinquency counts, inquiry histories, trade tenure): x'_j = x_j, \u2200 j \u2208 X_dem \u222a X_hist."
)
update_para(doc.paragraphs[76], p76_text)

p77_text = (
    "Directional Monotonicity (C_mono(x, x')): Ensures actionable recommendations do not prescribe adverse credit outcomes. For liability balances "
    "and delinquency indicators j \u2208 X_liab (x'_j \u2264 x_j) and positive assets j \u2208 X_asset (e.g., savings, income: x'_j \u2265 x_j)."
)
update_para(doc.paragraphs[77], p77_text)

p78_text = (
    "Integrality & Physical Bounds (C_disc(x')): Enforces integer constraints on discrete counts (e.g. x'_j \u2208 \u2115_0 for trade lines) and restricts "
    "percentages to the unit interval x'_j \u2208 [0, 1]. The borrower-side feasible set is then formally defined as F_B(x) = {x' \u2208 \u03a7 : f(x') \u2264 \u03c4 \u2227 C(x, x') = 1}, "
    "and the institutional counter-offer space as F_I(x) = {\u03b1* \u2208 [\u03b1_min, 1.0] : \u03b1* \u2264 \u03c4 / f(x)}."
)
update_para(doc.paragraphs[78], p78_text)

p86_text = (
    "where C_min denotes the regional credit floor (€500, $500, ₹500). The upper bound C_max \u2264 6 \u00b7 Income imposes an institutional safeguard against inflating limits on near-zero balances."
)
update_para(doc.paragraphs[86], p86_text)

p89_text = (
    "To ensure repayment advice is realistic, we assume a household cannot safely spend more than a statutory fraction \u03ba = 0.25 (25%) of their spare monthly "
    "income on debt reduction (\u0394_disp), the required Execution Horizon H (in months) is: H = \u0394_nom / (\u03ba \u00b7 \u0394_disp)."
)
update_para(doc.paragraphs[89], p89_text)

p91_text = (
    "The Temporal Solvency Predicate C_temp(x, x') strictly rejects any plan where H > H_max (where H_max = 24 months represents the standard supervisory horizon)."
)
update_para(doc.paragraphs[91], p91_text)

p99_text = (
    "Finally, in real-world financial environments, an applicant cannot execute financial targets with infinite precision; actual debt paydowns "
    "fluctuate due to unexpected expenses. We formalize recourse robustness as an explicit stability probability metric: "
    "Stab(x') = P_{\u03b5 ~ N(0, \u03a3)}(f(x' + \u03b5) \u2264 \u03c4 \u2227 C(x, x' + \u03b5) = 1), where \u03a3 = diag((\u03c3_j \u00b7 x'_j)^2) captures a 5% "
    "stochastic execution variance (\u03c3_j = 0.05). In empirical audits, candidate plans are approved only if the applicant retains qualification "
    "in at least 85% of perturbed execution attempts (Stab(x') \u2265 0.85)."
)
update_para(doc.paragraphs[99], p99_text)

update_para(doc.paragraphs[101], "4.4 Basel-Aligned Expected-Loss Constraint & Exposure Sizing")

p103_text = (
    "Theorem 1 (Risk-Neutral Exposure Sizing). Let \u03c4 denote the bank's maximum allowable default risk for a requested loan EAD_0. "
    "If an applicant's true calibrated default risk is higher (PD > \u03c4), scaling the approved loan amount down to: "
    "EAD* = \u03b1* \u00b7 EAD_0, where \u03b1* = min(1.0, \u03c4 / PD), guarantees that the bank's Expected Loss on the smaller loan "
    "does not exceed the risk of an approved applicant at the hurdle rate: E[Loss(EAD*)] \u2264 \u03c4 \u00b7 LGD \u00b7 EAD_0."
)
update_para(doc.paragraphs[103], p103_text)

p108_text = (
    "In consumer lending, offering a negligible loan (e.g., sanctioning $500 on a $50,000 mortgage application) is impractical and unhelpful. "
    "FairRecourse enforces an automated haircut floor of \u03b1_min = 0.80, capping the maximum automated reduction at 20%:"
)
update_para(doc.paragraphs[108], p108_text)

p109_text = (
    "Automated Counter-Offer (\u03b1* \u2265 0.80): The applicant receives an immediate, automated counter-offer certificate for "
    "EAD* = \u03b1* \u00b7 EAD_0 with an explicit facility haircut of (1 - \u03b1*) \u00d7 100%."
)
update_para(doc.paragraphs[109], p109_text)

p110_text = (
    "Discretionary Human Escalation (\u03b1* < 0.80): If the required exposure reduction exceeds 20% (haircut > 20%), the risk profile cannot "
    "be resolved through routine automation. Rather than generating an automated denial, FairRecourse flags the application for credit committee review and manual underwriting."
)
update_para(doc.paragraphs[110], p110_text)
print("Updated Section 4 Formalization (P71-P110).")

# =========================================================================
# 5. Section 5 Datasets & Baseline Configurations (P115-P117, P125-P127)
# =========================================================================
p115_text = (
    "Statlog German Credit (N_total = 1,000, N_eval = 34, €): Sourced from UCI (10 features; 80/20 train/test split; 30.0% default rate). "
    "Represents contractual retail credit with explicit loan terms (duration_months, credit_amount, installment_rate) and liquid reserves (savings_balance), "
    "enabling direct evaluation of bilateral restructuring."
)
update_para(doc.paragraphs[115], p115_text)

p116_text = (
    "FICO HELOC (N_total = 10,459, N_eval = 260, $): Sourced from the FICO Explainable Machine Learning Challenge (27 features; 80/20 train/test split; "
    "50.0% default rate). Captures US revolving credit composed entirely of historical bureau tradelines, delinquency counts, and credit-seeking metrics "
    "(ExternalRiskEstimate, NetFractionRevolvingBurden)."
)
update_para(doc.paragraphs[116], p116_text)

p117_text = (
    "CIBIL Retail Cohort (N_total = 50,000, N_eval = 376, ₹): A production-grade Indian retail banking dataset (77 features; 80/20 train/test split; "
    "25.97% default rate). Captures personal loans and credit cards across calibrated risk tiers (P1/P2 prime vs. P3/P4 subprime), providing high-dimensional "
    "telemetry from an emerging market."
)
update_para(doc.paragraphs[117], p117_text)

p125_text = (
    "FairRecourse (Proposed): A deterministic recourse engine evaluated under the PCL referee across two operational pathways, "
    "formally decomposed as follows:"
)
update_para(doc.paragraphs[125], p125_text)

p126_text = (
    "1. Borrower-Side Actionable Recourse (S_B): Evaluates joint contractual adjustments (Option A: loan duration, requested amount) and actionable "
    "balance-sheet interventions (Option B: liquid savings, revolving debt paydowns) subject to temporal solvency (H \u2264 H_max = 24 months): "
    "S_B = |{x \u2208 D_eval : F_B(x) \u2260 \u2205}| / N. Borrower recourse alone achieves 100.0% on German Credit, but collapses to 3.8% on HELOC "
    "and 0.0% on CIBIL due to deeply entrenched, immutable credit bureau anchors."
)
update_para(doc.paragraphs[126], p126_text)

p127_text = (
    "2. Institutional Counter-Offer Resolution (S_I): Dynamically triggered upon borrower-side deadlock (F_B(x) = \u2205) to compute a risk-neutral "
    "facility limit haircut (\u03b1* = \u03c4 / PD \u2265 0.80): S_I = |{x \u2208 D_eval : F_B(x) = \u2205 \u2227 F_I(x) \u2260 \u2205}| / N. "
    "The total combined admissible resolution is S_R = S_B + S_I = |{x \u2208 D_eval : F_B(x) \u2260 \u2205 \u2228 F_I(x) \u2260 \u2205}| / N = 100.0% across all cohorts."
)
update_para(doc.paragraphs[127], p127_text)
print("Updated Section 5 Datasets & Formal Metric Decomposition (P115-P127).")

# =========================================================================
# 6. Section 6 Audit 1: Algorithmic & Statutory Validity Audit (P129, P131, P137, P140-P142)
# Strong #9 (Audit 1 vs Audit 2 structure)
# =========================================================================
update_para(doc.paragraphs[129], "6. Audit 1: Algorithmic & Statutory Validity Audit")

p131_text = (
    "To evaluate operational validity on real-world decision boundaries, we extract all borderline adverse applicants from the holdout test partitions "
    "whose calibrated probability of default lies marginally above the operational underwriting threshold (\u03c4 = 0.40, PD \u2208 [0.405, 0.500]). "
    "This isolates the exact near-miss demographic eligible for adverse action recourse and risk-constrained institutional counter-offers: "
    "N_eval = 34 for Statlog German Credit, N_eval = 260 for FICO HELOC, and N_eval = 376 for CIBIL Retail (N_total = 670 total). "
    "All candidate plans are audited under the independent PCL referee."
)
update_para(doc.paragraphs[131], p131_text)

# Table 1 Notes (P137)
p137_text = (
    "*Notes: (1) S_B denotes Borrower-Side Recourse Success; S_I denotes Institutional Counter-Offer Resolution; "
    "S_R = S_B + S_I denotes Total Admissible Resolution. (2) DiCE baseline failures on HELOC comprise 264 immutability breaches, "
    "65 directional monotonicity violations, and 168 non-integer count corruptions (497 total violations across 244/260 applicants, a 93.8% non-compliance rate). "
    "(3) Option A (Contractual Renegotiation) is marked N/A on HELOC and CIBIL because pure bureau repositories exclude loan origination parameters "
    "(e.g., requested tenure, loan amount); evaluations use balance-sheet levers and exposure scaling. (4) In CIBIL, historical bureau delinquencies "
    "preclude unilateral recourse (S_B = 0.0%), routing 100.0% of adverse applicants to Basel exposure scaling at an average limit haircut of 10.83% (\u03b1* = 0.8917)."
)
update_para(doc.paragraphs[137], p137_text, italic=True)

# Section 6.2 Narratives (P140, P141, P142)
p140_text = (
    "Univariate Bounds Fail on Relational Invariants: In German Credit (N=34), unconstrained DiCE achieves 100.0% mathematical validity but incurs "
    "an unviable mean execution horizon of 188.4 months (15.7 years) at an average cost of 1.412, with 11 directional monotonicity violations (S_B = 67.6%). "
    "Constraining the search space via API-level parameter bounds (features_to_vary, permitted_range) suppresses direct immutability violations, yet still "
    "yields an impractical 125.2-month horizon and an inflated recourse cost of 9.006 (S_B = 50.0%). Independent univariate intervals cannot enforce the joint "
    "relational constraint linking total debt reduction to monthly disposable income. In contrast, FairRecourse's contractual optimization achieves S_B = 100.0% "
    "compliant resolution within an average horizon of 1.0 month at an average cost of 0.237 and 96.9% \u03b5-stability."
)
update_para(doc.paragraphs[140], p140_text)

p141_text = (
    "Bureau Anchors Cause Optimization Deadlocks: On pure credit bureau files (HELOC and CIBIL), unconstrained DiCE produces extensive policy breaches\u2014"
    "generating 497 violations on HELOC (comprising 264 immutability breaches, 168 non-integer count corruptions, and 65 monotonicity violations across 93.8% "
    "of applicants, yielding S_B = 6.2%) and 459 on CIBIL (altering historical inquiries, delinquency records, and chronological age, yielding S_B = 11.2%). "
    "Enforcing strict immutability bounds reduces DiCE’s feasible recourse rate to 3.8% on HELOC (with all solutions violating H \u2264 24 months, averaging 38.4 months) "
    "and 0.0% on CIBIL due to immutable delinquency splits in the underlying tree structures."
)
update_para(doc.paragraphs[141], p141_text)

p142_text = (
    "Bilateral Resolution via Exposure Scaling: Rather than treating unilateral optimization deadlocks as terminal denials, FairRecourse activates "
    "Basel-aligned exposure scaling. On HELOC, it isolates the 3.8% (10/260) of applicants capable of realistic recourse within statutory horizons "
    "(H=4.2 months, cost 0.463, 94.5% \u03b5-stability) and structures compliant counter-offers for the remaining 96.2% (250/260) at a mean haircut of 14.30% "
    "(\u03b1* = 0.8570), achieving S_R = 100.0%. On CIBIL, FairRecourse converts a 0.0% unilateral deadlock (376/376 deadlocked on borrower actions) into a 100.0% "
    "total compliant resolution rate (S_I = 100.0%) at an average exposure haircut of 10.83% (\u03b1* = 0.8917), preserving portfolio expected loss with zero policy violations."
)
update_para(doc.paragraphs[142], p142_text)
print("Updated Section 6 Audit 1 Narratives (P129-P142).")

# =========================================================================
# 7. Section 7 Audit 2: Sociotechnical & Distributional Fairness Audit (P152, P154, P155, P157, P162-P172)
# Strong #9 (Audit 2), Strong #10 (Governance & Regulatory Recommendations)
# =========================================================================
update_para(doc.paragraphs[152], "7. Audit 2: Sociotechnical & Distributional Fairness Audit")

p154_text = (
    "A central question in credit governance is whether institutional exposure scaling (\u03b1*) operates equitably or disproportionately penalizes "
    "historically marginalized demographic groups. Extending a facility haircut rather than an unconstrained approval introduces a potential regulatory risk: "
    "could exposure scaling systematically assign depressed credit limits to protected classes, inducing an algorithmic form of down-tiering or digital redlining?"
)
update_para(doc.paragraphs[154], p154_text)

p155_text = (
    "We evaluate the distribution of calibrated default probabilities (PD) and resulting haircut percentages ((1 - \u03b1*) \u00d7 100%) across demographic "
    "subgroups within the borderline cohort (N=670). Table 2 documents these empirical distributions."
)
update_para(doc.paragraphs[155], p155_text)

update_para(doc.paragraphs[157], "Distributions across marginal applicant cohorts (N=670 total) across German Credit, HELOC, and CIBIL.")

p162_text = (
    "Demographic Parity in Scale: In the production CIBIL cohort (N=376), haircuts exhibit near-identical demographic parity across gender: "
    "female applicants receive a mean haircut of 11.02% (\u00b1 5.08%) versus 10.82% (\u00b1 5.77%) for males (a 0.20% differential)."
)
update_para(doc.paragraphs[162], p162_text)

p163_text = (
    "Cohort-Driven Variance: In German Credit (N=34), marginal female applicants receive an average haircut of 13.24% versus 10.37% for males "
    "(a 2.87% delta), reflecting a minor elevation in baseline risk (PD = 46.25% vs. 44.82%). Similarly, applicants under 25 receive slightly "
    "higher mean haircuts (12.51% vs. 10.86%)."
)
update_para(doc.paragraphs[163], p163_text)

p164_text = (
    "Evaluating whether a 13.24% haircut constitutes down-tiering requires comparing it to the prevailing operational baseline. Under standard "
    "underwriting, all applicants in this marginal tier (PD \u2265 40.5% > \u03c4 = 40.0%) face categorical rejection\u2014a 100% facility reduction. "
    "Preserving 86.76% of requested principal (\u03b1* = 0.8676) expands substantive credit access, establishing an active lending relationship "
    "that enables positive bureau reporting."
)
update_para(doc.paragraphs[164], p164_text)

p166_text = (
    "The Proportionality Invariant: Haircuts must strictly satisfy \u03b1* = min(1.0, \u03c4 / PD_calibrated), barring discretionary markdowns "
    "beyond the calibrated empirical risk ratio."
)
update_para(doc.paragraphs[166], p166_text)

p167_text = (
    "The Maximum Haircut Floor (\u03b1_min = 0.80): Automated counter-offers exceeding a 20% limit reduction are blocked, preventing lenders "
    "from steering vulnerable applicants into high-fee micro-credit facilities."
)
update_para(doc.paragraphs[167], p167_text)

# Governance & Regulatory Recommendations (P170-P172 + Governance Safeguards)
p170_text = (
    "Automated PCL Auditing: Regulatory examination manuals should require automated Policy & Constraint Layer test suites to verify that generated "
    "explanations preserve historical credit bureau immutability, respect directional monotonicity, and produce integer trade counts."
)
update_para(doc.paragraphs[170], p170_text)

p171_text = (
    "Statutory Cash-Flow Horizons: Supervisory bodies should establish maximum execution horizons (H \u2264 H_max = 24 months) for adverse action recourse. "
    "Counterfactuals requiring balance liquidations that violate household debt-to-income caps should be formally classified as deceptive practices "
    "(e.g., UDAAP under Dodd-Frank Act \u00a7 1036)."
)
update_para(doc.paragraphs[171], p171_text)

p172_text = (
    "Safe-Harbor Recognition of Algorithmic Counter-Offers & Governance Safeguards: Regulatory frameworks should codify Basel-compliant exposure scaling "
    "(\u03b1*) as a valid resolution mechanism under adverse action rules (e.g., U.S. Regulation B, 12 C.F.R. \u00a7 1002.9(a)(1)(iv)), providing financial "
    "institutions with safe-harbor protections when replacing outright denials with risk-neutral counter-offers. We establish three explicit institutional governance rules: "
    "(1) Underwriting Decision Authority: automated execution is permitted only for \u03b1* \u2265 0.80, with larger cuts requiring human credit committee escalation; "
    "(2) Adverse Action Transparency: Regulation B notices must explicitly disclose the baseline denial factor alongside the exact haircut formula (\u03b1* = \u03c4 / PD); and "
    "(3) Non-Masking Invariant: exposure scaling is strictly a second-order risk adjustment and must never be deployed to compensate for or mask demographic bias in the base risk scoring model."
)
update_para(doc.paragraphs[172], p172_text)
print("Updated Section 7 Audit 2 & Governance Safeguards (P152-P172).")

# =========================================================================
# 8. Section 8 Limitations (P184, P186)
# =========================================================================
p184_text = (
    "Feedback Effects of Exposure Scaling: Our framework assumes that reducing an applicant's loan limit (\u03b1*) does not alter their baseline default probability (PD). "
    "In practice, granting a smaller line might increase credit utilization and raise subsequent risk. Although our minimum limit floor (\u03b1_min = 0.80) "
    "mitigates this risk, future work should incorporate structural causal modeling to capture this feedback dynamic directly."
)
update_para(doc.paragraphs[184], p184_text)

p186_text = (
    "Product-Specific Calibration: Operational thresholds (\u03c4) and safety margins vary across retail lending products. Practical deployment requires "
    "calibrating the Policy & Constraint Layer to the risk appetites and historical recovery rates of specific credit portfolios."
)
update_para(doc.paragraphs[186], p186_text)
print("Updated Section 8 Limitations (P184, P186).")

# =========================================================================
# 9. Insert Horizon Sensitivity Subsection (Item 7) after P147
# =========================================================================
# Let's check if Horizon Sensitivity subsection is already present
has_sensitivity = any("6.4 Sensitivity Analysis on Execution Horizon" in p.text for p in doc.paragraphs)
if not has_sensitivity:
    ref_p = doc.paragraphs[148]  # right after P147
    p_sens_h = ref_p.insert_paragraph_before("6.4 Sensitivity Analysis on Execution Horizon (H_max)")
    p_sens_h.style = 'Heading 3' if 'Heading 3' in [s.name for s in doc.styles] else 'Normal'
    for r in p_sens_h.runs:
        r.font.name = 'Calibri'
        r.font.bold = True
        r.font.size = Pt(11)

    p_sens_body = ref_p.insert_paragraph_before(
        "Rather than treating H \u2264 24 months as an arbitrary invariant, we evaluate borrower-side recourse feasibility S_B across an institutional "
        "sensitivity sweep H_max \u2208 {6, 12, 18, 24, 36} months: "
        "(1) In German Credit, Option A remains 100.0% feasible across all H_max \u2265 6 (mean horizon 1.0 month), while Option B feasibility scales from "
        "17.6% (6 months) and 41.2% (12 months) to 50.0% at H_max \u2265 24 months. "
        "(2) In FICO HELOC, Option B achieves 2.7% feasibility at 6 months and saturates at its ceiling of 3.8% (10/260) for all H_max \u2265 12 months, "
        "whereas unconstrained DiCE requires a mean horizon of 38.4 months, achieving 0.0% feasibility under standard 24-month underwriting horizons. "
        "(3) In CIBIL Retail, borrower recourse remains strictly S_B = 0.0% across all horizons H_max \u2208 [6, 36] months due to fixed historical bureau anchors, "
        "empirically demonstrating that extending execution timelines cannot resolve structural credit deadlocks without institutional exposure scaling (S_I = 100.0%)."
    )
    for r in p_sens_body.runs:
        r.font.name = 'Calibri'
        r.font.size = Pt(10)
    print("Inserted Section 6.4 Sensitivity Analysis on Execution Horizon.")

# =========================================================================
# 10. Build Native Word Table 1 and Insert at P136
# =========================================================================
# Clear P136 runs (which had the old image)
p136 = doc.paragraphs[136]
p136.text = ""

# Insert Table 1 before P137
table1 = doc.add_table(rows=16, cols=10)
table1.alignment = WD_TABLE_ALIGNMENT.CENTER

t1_headers = [
    'Dataset Ecosystem & Currency',
    'Recourse Framework Tier',
    'Theoretical Success (%)',
    'Borrower Recourse S_B (%)',
    'Invariant Violations (Tot / Immut / Monot / Horiz)',
    'Mean Recourse Cost',
    'Mean Horizon H (Months)',
    '\u03b5-Stability (Stab)',
    'Institutional Counter-Offer S_I (%)',
    'Total Admissible Resolution S_R (%)'
]

for col_idx, text in enumerate(t1_headers):
    cell = table1.cell(0, col_idx)
    cell.text = text
    set_cell_shading(cell, "E2E8F0")
    set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(7.5)
            r.font.bold = True

t1_data = [
    # German Credit (5 rows)
    ['German Credit (€)\n(N=1,000, d=10)\n(τ=0.40, N_marg=34)', 'Baseline (DiCE)', '100.0%', '67.6%', '11 (0 / 6 / 5)', '1.034', '11.0 (Max 188.4)', 'Not Evaluated', '0.0%', '67.6%'],
    ['', 'Bounded DiCE', '50.0%', '50.0%', '6 (0 / 0 / 6)', '9.006', '125.2 (Max 125.2)', 'Not Evaluated', '0.0%', '50.0%'],
    ['', 'FairRecourse (Opt A: Contractual)', '100.0%', '100.0%', '0 (0 / 0 / 0)', '0.237', '1.0 (Max 1.0)', '96.9%', '0.0%', '100.0%'],
    ['', 'FairRecourse (Opt B: Balance Sheet)', '50.0%', '50.0%', '0 (0 / 0 / 0)', '1.222', '14.9 (Max 21.1)', '100.0%', '0.0%', '50.0%'],
    ['', 'FairRecourse (Total Resolution)', '100.0%', '100.0%', '0 (0 / 0 / 0)', '0.237', '1.0 (Max 1.0)', '96.9%', '0.0%', '100.0%'],
    # FICO HELOC (5 rows)
    ['FICO HELOC ($)\n(N=10,459, d=27)\n(τ=0.40, N_marg=260)', 'Baseline (DiCE)', '100.0%', '6.2%', '497 (264 / 65 / 0)*', '0.328', '1.2 (Max 1.2)', 'Not Evaluated', '0.0%', '6.2%'],
    ['', 'Bounded DiCE', '3.8%', '3.8%', '0 (0 / 0 / 0)', '0.854', '38.4 (Max 62.1)', 'Not Evaluated', '0.0%', '3.8%'],
    ['', 'FairRecourse (Opt A: Contractual)', 'N/A', '0.0% (N/A)†', '0 (0 / 0 / 0)', 'N/A', 'N/A', 'N/A', '0.0%', '0.0%'],
    ['', 'FairRecourse (Opt B: Balance Sheet)', '3.8%', '3.8%', '0 (0 / 0 / 0)', '0.463', '4.2 (Max 8.4)', '94.5%', '0.0%', '3.8%'],
    ['', 'FairRecourse (Total Resolution)', '100.0%', '3.8%', '0 (0 / 0 / 0)', '0.463', '4.2 (Max 8.4)', '94.5%', '96.2%', '100.0%'],
    # External CIBIL (5 rows)
    ['External CIBIL (₹)\n(N=50,000, d=77)\n(τ=0.40, N_marg=376)', 'Baseline (DiCE)', '100.0%', '11.2%', '459 (424 / 26 / 9)', '0.641', '6.0 (Max 269.8)', 'Not Evaluated', '0.0%', '11.2%'],
    ['', 'Bounded DiCE', '0.0%', '0.0%', '0 (0 / 0 / 0)', 'N/A', 'N/A', 'Not Evaluated', '0.0%', '0.0%'],
    ['', 'FairRecourse (Opt A: Contractual)', 'N/A', '0.0% (N/A)†', '0 (0 / 0 / 0)', 'N/A', 'N/A', 'N/A', '0.0%', '0.0%'],
    ['', 'FairRecourse (Opt B: Balance Sheet)', '0.0%', '0.0% (Infeasible)‡', '0 (0 / 0 / 0)', 'N/A', 'N/A', 'N/A', '0.0%', '0.0%'],
    ['', 'FairRecourse (Total Resolution)', '100.0%', '0.0%', '0 (0 / 0 / 0)', 'N/A', 'N/A', 'N/A', '100.0%', '100.0%']
]

for row_idx, row_data in enumerate(t1_data, start=1):
    for col_idx, val in enumerate(row_data):
        cell = table1.cell(row_idx, col_idx)
        cell.text = val
        if 'Total Resolution' in val or ('Opt A' in val and row_idx == 3):
            set_cell_shading(cell, "F1F5F9")
        elif row_idx % 2 == 0:
            set_cell_shading(cell, "F8FAFC")
        set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
        for p in cell.paragraphs:
            if col_idx in [0, 1]:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            for r in p.runs:
                r.font.name = 'Calibri'
                r.font.size = Pt(7.0)
                if 'Total Resolution' in val or (col_idx == 1 and 'FairRecourse' in val):
                    r.font.bold = True

# Move table1 XML to before p137
doc.paragraphs[137]._p.addprevious(table1._tbl)
print("Inserted Native Word Table 1.")

# =========================================================================
# 11. Build Native Word Table 2 and Insert at P158
# =========================================================================
# Clear P158 runs (which had the old image)
p158 = doc.paragraphs[158]
p158.text = ""

table2 = doc.add_table(rows=9, cols=8)
table2.alignment = WD_TABLE_ALIGNMENT.CENTER

t2_headers = [
    'Dataset Ecosystem & Currency',
    'Protected / Proxy Demographic Dimension',
    'Subgroup Category',
    'Marginal Cohort Size (N)',
    'Mean Calibrated PD',
    'Mean Haircut (1 - \u03b1*) \u00d7 100%',
    'Median Haircut (%)',
    'Haircut Std Dev (\u03c3)'
]

for col_idx, text in enumerate(t2_headers):
    cell = table2.cell(0, col_idx)
    cell.text = text
    set_cell_shading(cell, "E2E8F0")
    set_cell_margins(cell, top=100, bottom=100, left=80, right=80)
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = 'Calibri'
            r.font.size = Pt(8.0)
            r.font.bold = True

t2_data = [
    ['German Credit (€)', 'Biological Sex (gender)', 'Female', '11', '46.25%', '13.24%', '13.64%', '5.18%'],
    ['', '', 'Male', '23', '44.82%', '10.37%', '9.77%', '5.97%'],
    ['', 'Age Bracket (age_group)', 'Under 25', '9', '45.91%', '12.51%', '13.13%', '6.04%'],
    ['', '', '25 and Over', '25', '45.06%', '10.86%', '10.88%', '5.79%'],
    ['FICO HELOC ($)', 'Credit Bureau Tier (risk_tier)', 'Higher Score Tier', '171', '47.49%', '15.51%', '17.60%', '4.92%'],
    ['', '', 'Lower Score Tier', '89', '44.99%', '10.72%', '10.59%', '5.79%'],
    ['External CIBIL (₹)', 'Recorded Gender (gender)', 'Female', '35', '45.10%', '11.02%', '11.84%', '5.08%'],
    ['', '', 'Male', '341', '45.04%', '10.82%', '11.10%', '5.77%']
]

for row_idx, row_data in enumerate(t2_data, start=1):
    for col_idx, val in enumerate(row_data):
        cell = table2.cell(row_idx, col_idx)
        cell.text = val
        if row_idx % 2 == 0:
            set_cell_shading(cell, "F8FAFC")
        set_cell_margins(cell, top=60, bottom=60, left=60, right=60)
        for p in cell.paragraphs:
            if col_idx in [0, 1, 2]:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
            for r in p.runs:
                r.font.name = 'Calibri'
                r.font.size = Pt(8.0)

# Move table2 XML to before P159 / P160
doc.paragraphs[160]._p.addprevious(table2._tbl)
print("Inserted Native Word Table 2.")

# Save modified document to new file
output_path = 'FairRecourse-Abstract_new.docx'
doc.save(output_path)
print(f"Successfully saved {output_path}!")
