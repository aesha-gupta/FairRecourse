# Batch Audit Report: 15 Marginal Applicants per Dataset


# Dataset: GERMAN
================================================================================
Found 34 marginal borderline applicants!

## Evaluating Applicant #2
--------------------------------------------------------------------------------
Calibrated PD: 44.89% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4489

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (460.80 -> 5102.80).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 44.89%)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0002
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• savings_balance           : +0.2881 margin [Increases Default Risk]
• number_existing_credits   : +0.2755 margin [Increases Default Risk]
• duration_months           : +0.2090 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              1024.00            524.00             Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #3
--------------------------------------------------------------------------------
Calibrated PD: 44.05% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.171
Recourse Cost Metric         0.225              0.225                  1.567
Execution Horizon            1.0 mos            1.0 mos                19.9 mos
Epsilon-Stability            Not Evaluated      90%                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 44.05%)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0003
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.1%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5086 margin [Increases Default Risk]
• duration_months           : +0.4561 margin [Increases Default Risk]
• savings_balance           : +0.4070 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              3104.00            2604.00            Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0003
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.1%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5086 margin [Increases Default Risk]
• duration_months           : +0.4561 margin [Increases Default Risk]
• savings_balance           : +0.4070 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 19.9 Months
Monthly Commitment Required   : € 50.25 / month
Total Financial Shift         : € 1000.00
Composite Recourse Cost       : 1.567
Feasibility Score             : 0.171 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #23
--------------------------------------------------------------------------------
Calibrated PD: 48.02% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4097
Lowest PD reached by solver: 0.4044
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • duration_months                     : +0.4478 margin [Increases Default Risk]
  • monthly_income                      : +0.4383 margin [Increases Default Risk]
  • savings_balance                     : +0.3809 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 83.3% (16.69% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         4.608              N/A                    N/A
Execution Horizon            64.1 mos           N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (64.1 > 24.0 months)

## Evaluating Applicant #24
--------------------------------------------------------------------------------
Calibrated PD: 42.58% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.283
Recourse Cost Metric         3.946              0.225                  1.382
Execution Horizon            51.6 mos           1.0 mos                17.2 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (51.6 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0024
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 42.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4845 margin [Increases Default Risk]
• savings_balance           : +0.2827 margin [Increases Default Risk]
• monthly_income            : +0.2596 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              1795.00            795.00             Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0024
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 42.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4845 margin [Increases Default Risk]
• savings_balance           : +0.2827 margin [Increases Default Risk]
• monthly_income            : +0.2596 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 17.2 Months
Monthly Commitment Required   : € 29.07 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.382
Feasibility Score             : 0.283 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #36
--------------------------------------------------------------------------------
Calibrated PD: 45.71% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.450
Recourse Cost Metric         0.425              0.225                  1.106
Execution Horizon            1.0 mos            1.0 mos                13.2 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0036
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 45.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.3993 margin [Increases Default Risk]
• savings_balance           : +0.3887 margin [Increases Default Risk]
• duration_months           : +0.3119 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              4169.00            3669.00            Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0036
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 45.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.3993 margin [Increases Default Risk]
• savings_balance           : +0.3887 margin [Increases Default Risk]
• duration_months           : +0.3119 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 13.2 Months
Monthly Commitment Required   : € 37.88 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.106
Feasibility Score             : 0.45 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #41
--------------------------------------------------------------------------------
Calibrated PD: 49.69% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4316
Lowest PD reached by solver: 0.4969
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • duration_months                     : +0.5842 margin [Increases Default Risk]
  • savings_balance                     : +0.3827 margin [Increases Default Risk]
  • monthly_income                      : +0.2472 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.5% (19.5% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 46.74%)

## Evaluating Applicant #46
--------------------------------------------------------------------------------
Calibrated PD: 46.04% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4604
Lowest PD reached by solver: 0.4604
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • savings_balance                     : +0.3321 margin [Increases Default Risk]
  • monthly_income                      : +0.2903 margin [Increases Default Risk]
  • number_existing_credits             : +0.1985 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 86.9% (13.13% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature duration_months (18.00 -> 4.00).

## Evaluating Applicant #47
--------------------------------------------------------------------------------
Calibrated PD: 46.32% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.333
Recourse Cost Metric         0.225              0.225                  1.301
Execution Horizon            1.0 mos            1.0 mos                16.0 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature duration_months (30.00 -> 6.00).

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0047
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 46.3%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.4732 margin [Increases Default Risk]
• credit_amount             : +0.4291 margin [Increases Default Risk]
• savings_balance           : +0.2681 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              4280.00            2780.00            Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0047
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 46.3%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.4732 margin [Increases Default Risk]
• credit_amount             : +0.4291 margin [Increases Default Risk]
• savings_balance           : +0.2681 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            750.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 16.0 Months
Monthly Commitment Required   : € 31.25 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.301
Feasibility Score             : 0.333 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #53
--------------------------------------------------------------------------------
Calibrated PD: 49.25% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4733

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             PASSED
Feasibility Score [0-1]      0.000              N/A                    0.233
Recourse Cost Metric         0.425              N/A                    1.467
Execution Horizon            1.0 mos            N/A                    18.4 mos
Epsilon-Stability            Not Evaluated      N/A                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature duration_months (48.00 -> 60.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 47.48%)

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0053
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 49.3%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.6558 margin [Increases Default Risk]
• duration_months           : +0.5617 margin [Increases Default Risk]
• savings_balance           : +0.4350 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 18.4 Months
Monthly Commitment Required   : € 54.35 / month
Total Financial Shift         : € 1000.00
Composite Recourse Cost       : 1.467
Feasibility Score             : 0.233 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #54
--------------------------------------------------------------------------------
Calibrated PD: 44.13% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4413
Lowest PD reached by solver: 0.4413
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • savings_balance                     : +0.3237 margin [Increases Default Risk]
  • monthly_income                      : +0.3005 margin [Increases Default Risk]
  • number_existing_credits             : +0.2019 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 90.6% (9.36% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         4.614              N/A                    N/A
Execution Horizon            61.3 mos           N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (61.3 > 24.0 months)

## Evaluating Applicant #58
--------------------------------------------------------------------------------
Calibrated PD: 47.87% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.121              0.958                  0.204
Recourse Cost Metric         1.849              0.225                  1.515
Execution Horizon            21.1 mos           1.0 mos                19.1 mos
Epsilon-Stability            Not Evaluated      90%                    100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0058
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 47.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5422 margin [Increases Default Risk]
• savings_balance           : +0.3752 margin [Increases Default Risk]
• credit_amount             : +0.3253 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              4297.00            3797.00            Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0058
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 47.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5422 margin [Increases Default Risk]
• savings_balance           : +0.3752 margin [Increases Default Risk]
• credit_amount             : +0.3253 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 19.1 Months
Monthly Commitment Required   : € 52.36 / month
Total Financial Shift         : € 1000.00
Composite Recourse Cost       : 1.515
Feasibility Score             : 0.204 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #59
--------------------------------------------------------------------------------
Calibrated PD: 47.52% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4359
Lowest PD reached by solver: 0.4054
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • monthly_income                      : +0.5094 margin [Increases Default Risk]
  • savings_balance                     : +0.3509 margin [Increases Default Risk]
  • duration_months                     : +0.2742 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 84.2% (15.83% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (2330.55 -> 4102.69).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 46.84%)

## Evaluating Applicant #78
--------------------------------------------------------------------------------
Calibrated PD: 49.56% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4956
Lowest PD reached by solver: 0.4956
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • duration_months                     : +0.3939 margin [Increases Default Risk]
  • people_liable                       : +0.3246 margin [Increases Default Risk]
  • savings_balance                     : +0.3245 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.7% (19.29% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         7.888              N/A                    N/A
Execution Horizon            108.9 mos          N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (108.9 > 24.0 months)

## Evaluating Applicant #79
--------------------------------------------------------------------------------
Calibrated PD: 42.94% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.162
Recourse Cost Metric         0.225              0.225                  1.580
Execution Horizon            1.0 mos            1.0 mos                20.1 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 42.94%)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0079
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 42.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4883 margin [Increases Default Risk]
• savings_balance           : +0.4000 margin [Increases Default Risk]
• number_existing_credits   : +0.1623 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              2051.00            1551.00            Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.225
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-B
Applicant Case ID    : APP-0079
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 42.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4883 margin [Increases Default Risk]
• savings_balance           : +0.4000 margin [Increases Default Risk]
• number_existing_credits   : +0.1623 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 20.1 Months
Monthly Commitment Required   : € 24.88 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.58
Feasibility Score             : 0.162 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #80
--------------------------------------------------------------------------------
Calibrated PD: 48.27% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4573
Lowest PD reached by solver: 0.4827
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • savings_balance                     : +0.3664 margin [Increases Default Risk]
  • duration_months                     : +0.3437 margin [Increases Default Risk]
  • monthly_income                      : +0.2633 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 82.9% (17.14% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature duration_months (36.00 -> 25.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 45.76%)

# Dataset: HELOC
================================================================================
      Loaded local dataset file: heloc_dataset.arff
Found 253 marginal borderline applicants!

## Evaluating Applicant #6
--------------------------------------------------------------------------------
Calibrated PD: 41.63% (Threshold: 40.0%)
Lowest PD reached by solver: 0.3969
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.4499 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1747 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1510 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 96.1% (3.93% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades60Ever2DerogPubRec (1.00 -> 5.80).
  [X] Discrete count violation: NumTrades60Ever2DerogPubRec must be an integer, received 5.80.
  [X] Immutability violation: Cannot alter historical/demographic feature NumInqLast6M (0.00 -> 41.20).
  [X] Discrete count violation: NumInqLast6M must be an integer, received 41.20.

## Evaluating Applicant #13
--------------------------------------------------------------------------------
Calibrated PD: 46.93% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4640
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.3681 margin [Increases Default Risk]
  • AverageMInFile                      : +0.3327 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0700 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.2% (14.76% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         1.113              N/A                    N/A
Execution Horizon            10.2 mos           N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTotalTrades (11.00 -> 83.20).
  [X] Discrete count violation: NumTotalTrades must be an integer, received 83.20.
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 42.99%)

## Evaluating Applicant #31
--------------------------------------------------------------------------------
Calibrated PD: 49.75% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4722
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.0978 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0559 margin [Increases Default Risk]
  • savings_balance                     : +0.0246 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.4% (19.6% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature MSinceMostRecentTradeOpen (6.00 -> 372.60).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 47.63%)

## Evaluating Applicant #36
--------------------------------------------------------------------------------
Calibrated PD: 49.23% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4967
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.3304 margin [Increases Default Risk]
  • AverageMInFile                      : +0.2870 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.2490 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 81.3% (18.74% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature MSinceOldestTradeOpen (288.00 -> 140.80).
  [X] Immutability violation: Cannot alter historical/demographic feature NumInqLast6M (1.00 -> 7.60).
  [X] Discrete count violation: NumInqLast6M must be an integer, received 7.60.
  [X] Domain bounds violation: NetFractionInstallBurden must be within [0, 100]%, received 101.00%.
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 40.50%)

## Evaluating Applicant #38
--------------------------------------------------------------------------------
Calibrated PD: 49.28% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4675
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2997 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.2339 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.0503 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 81.2% (18.83% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades60Ever2DerogPubRec (1.00 -> 7.70).
  [X] Discrete count violation: NumTrades60Ever2DerogPubRec must be an integer, received 7.70.
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 49.92%)

## Evaluating Applicant #48
--------------------------------------------------------------------------------
Calibrated PD: 41.07% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4107
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.4113 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.2860 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.2729 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 97.4% (2.61% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTradesOpeninLast12M (0.00 -> 18.40).
  [X] Discrete count violation: NumTradesOpeninLast12M must be an integer, received 18.40.
  [X] Monotonicity violation: Adverse risk metric NetFractionInstallBurden cannot increase (74.00 -> 247.60).
  [X] Domain bounds violation: NetFractionInstallBurden must be within [0, 100]%, received 247.60%.

## Evaluating Applicant #79
--------------------------------------------------------------------------------
Calibrated PD: 49.19% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4819
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.1768 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.1302 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.1196 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 81.3% (18.69% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades60Ever2DerogPubRec (0.00 -> 3.90).
  [X] Discrete count violation: NumTrades60Ever2DerogPubRec must be an integer, received 3.90.
  [X] Immutability violation: Cannot alter historical/demographic feature NumRevolvingTradesWBalance (6.00 -> 6.60).
  [X] Discrete count violation: NumRevolvingTradesWBalance must be an integer, received 6.60.
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 48.39%)

## Evaluating Applicant #91
--------------------------------------------------------------------------------
Calibrated PD: 49.15% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4915
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3188 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.1936 margin [Increases Default Risk]
  • ExternalRiskEstimate                : +0.1420 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 81.4% (18.62% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades90Ever2DerogPubRec (0.00 -> 10.60).
  [X] Discrete count violation: NumTrades90Ever2DerogPubRec must be an integer, received 10.60.
  [X] Immutability violation: Cannot alter historical/demographic feature PercentInstallTrades (13.00 -> 19.80).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 49.08%)

## Evaluating Applicant #103
--------------------------------------------------------------------------------
Calibrated PD: 44.86% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4184
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2124 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1592 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.1472 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.2% (10.84% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 43.94%)

## Evaluating Applicant #105
--------------------------------------------------------------------------------
Calibrated PD: 43.72% (Threshold: 40.0%)
Lowest PD reached by solver: 0.3972
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2797 margin [Increases Default Risk]
  • AverageMInFile                      : +0.0984 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0853 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 91.5% (8.51% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumInqLast6Mexcl7days (0.00 -> 41.40).
  [X] Discrete count violation: NumInqLast6Mexcl7days must be an integer, received 41.40.
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 41.26%)

## Evaluating Applicant #112
--------------------------------------------------------------------------------
Calibrated PD: 49.93% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4603
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.1030 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0542 margin [Increases Default Risk]
  • savings_balance                     : +0.0509 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.1% (19.88% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature MSinceOldestTradeOpen (187.00 -> 545.80).
  [X] Immutability violation: Cannot alter historical/demographic feature NumBank2NatlTradesWHighUtilization (1.00 -> 18.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 42.68%)

## Evaluating Applicant #117
--------------------------------------------------------------------------------
Calibrated PD: 44.82% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4483
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.5338 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.1228 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.0639 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.2% (10.76% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTradesOpeninLast12M (3.00 -> 5.10).
  [X] Discrete count violation: NumTradesOpeninLast12M must be an integer, received 5.10.
  [X] Immutability violation: Cannot alter historical/demographic feature PercentInstallTrades (26.00 -> 53.90).

## Evaluating Applicant #120
--------------------------------------------------------------------------------
Calibrated PD: 40.73% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             PASSED
Feasibility Score [0-1]      0.000              N/A                    0.875
Recourse Cost Metric         0.225              N/A                    0.417
Execution Horizon            1.0 mos            N/A                    3.0 mos
Epsilon-Stability            Not Evaluated      N/A                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumBank2NatlTradesWHighUtilization (3.00 -> 15.40).
  [X] Discrete count violation: NumBank2NatlTradesWHighUtilization must be an integer, received 15.40.

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-HELOC-OPT-B
Applicant Case ID    : APP-0120
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 40.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• AverageMInFile            : +0.1824 margin [Increases Default Risk]
• NumSatisfactoryTrades     : +0.1593 margin [Increases Default Risk]
• MSinceMostRecentDelq      : +0.1483 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
NetFractionInstallBurden   67.00              37.00              Pay down balance / reduce utilization
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 3.0 Months
Monthly Commitment Required   : $ 485.82 / month
Total Financial Shift         : $ 1457.46
Composite Recourse Cost       : 0.417
Feasibility Score             : 0.875 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #126
--------------------------------------------------------------------------------
Calibrated PD: 41.01% (Threshold: 40.0%)
Lowest PD reached by solver: 0.3983
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentDelq                : +0.0997 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0607 margin [Increases Default Risk]
  • NetFractionInstallBurden            : +0.0591 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 97.5% (2.47% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTotalTrades (22.00 -> 56.10).
  [X] Discrete count violation: NumTotalTrades must be an integer, received 56.10.
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 41.13%)

## Evaluating Applicant #130
--------------------------------------------------------------------------------
Calibrated PD: 42.97% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4028
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.1614 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.0994 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.0902 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 93.1% (6.91% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentTradesNeverDelq (100.00 -> 63.80).

# Dataset: CIBIL
================================================================================
      Loaded local dataset file: External_Cibil_Dataset.xlsx
Found 376 marginal borderline applicants!

## Evaluating Applicant #37
--------------------------------------------------------------------------------
Calibrated PD: 42.28% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4228
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.0687 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.4535 margin [Increases Default Risk]
  • time_since_recent_enq               : +0.2410 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 94.6% (5.39% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_sub (0.00 -> 40.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 42.28%)

## Evaluating Applicant #76
--------------------------------------------------------------------------------
Calibrated PD: 44.61% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4461
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.1098 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.4975 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.3391 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.7% (10.33% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature time_since_first_deliquency (35.00 -> 22.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 44.61%)

## Evaluating Applicant #78
--------------------------------------------------------------------------------
Calibrated PD: 46.65% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4665
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.0968 margin [Increases Default Risk]
  • num_std                             : +0.2124 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.1481 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.7% (14.25% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 44.68%)

## Evaluating Applicant #95
--------------------------------------------------------------------------------
Calibrated PD: 42.80% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4280
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.4957 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3080 margin [Increases Default Risk]
  • num_std                             : +0.1528 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 93.5% (6.55% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature AGE (33.00 -> 21.00).
  [X] Monotonicity violation: Adverse risk metric PL_utilization cannot increase (0.00 -> 0.60).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 44.26%)

## Evaluating Applicant #127
--------------------------------------------------------------------------------
Calibrated PD: 43.57% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4357
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +0.4484 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.2465 margin [Increases Default Risk]
  • num_std                             : +0.2269 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 91.8% (8.2% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature max_recent_level_of_deliq (28.00 -> 668.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 43.57%)

## Evaluating Applicant #150
--------------------------------------------------------------------------------
Calibrated PD: 44.62% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4462
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +0.4093 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.3589 margin [Increases Default Risk]
  • num_std                             : +0.2811 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.6% (10.36% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_deliq_12mts (7.00 -> 12.00).
  [X] Immutability violation: Cannot alter historical/demographic feature time_since_recent_enq (8.00 -> 3321.00).

## Evaluating Applicant #203
--------------------------------------------------------------------------------
Calibrated PD: 46.95% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4695
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +2.1388 margin [Increases Default Risk]
  • num_std                             : +0.2111 margin [Increases Default Risk]
  • AGE                                 : +0.1400 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.2% (14.81% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature CC_enq_L12m (0.00 -> 3.00).
  [X] Immutability violation: Cannot alter historical/demographic feature time_since_recent_enq (0.00 -> 2714.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 46.02%)

## Evaluating Applicant #210
--------------------------------------------------------------------------------
Calibrated PD: 41.51% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4151
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.6396 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3147 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.1866 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 96.4% (3.63% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PL_enq (1.00 -> 5.00).
  [X] Immutability violation: Cannot alter historical/demographic feature AGE (25.00 -> 76.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 43.44%)

## Evaluating Applicant #218
--------------------------------------------------------------------------------
Calibrated PD: 48.66% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4866
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.2997 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.3624 margin [Increases Default Risk]
  • num_std                             : +0.1665 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 82.2% (17.8% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_std_12mts (2.00 -> 9.00).
  [X] Immutability violation: Cannot alter historical/demographic feature CC_enq_L6m (0.00 -> 13.00).

## Evaluating Applicant #262
--------------------------------------------------------------------------------
Calibrated PD: 41.80% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4180
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +0.9811 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.7173 margin [Increases Default Risk]
  • AGE                                 : +0.1151 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 95.7% (4.3% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_deliq_12mts (1.00 -> 0.00).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 41.80%)

## Evaluating Applicant #284
--------------------------------------------------------------------------------
Calibrated PD: 46.67% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4667
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.7476 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.3102 margin [Increases Default Risk]
  • time_since_recent_enq               : +0.1466 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.7% (14.29% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature first_prod_enq2_others (1.00 -> 0.20).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 46.67%)

## Evaluating Applicant #307
--------------------------------------------------------------------------------
Calibrated PD: 42.31% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4231
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.0190 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.4962 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.1367 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 94.5% (5.46% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric CC_utilization cannot increase (0.00 -> 14.80).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 42.31%)

## Evaluating Applicant #312
--------------------------------------------------------------------------------
Calibrated PD: 40.73% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4073
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +0.3714 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3349 margin [Increases Default Risk]
  • num_std                             : +0.2077 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 98.2% (1.79% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature tot_enq (2.00 -> 150.00).

## Evaluating Applicant #324
--------------------------------------------------------------------------------
Calibrated PD: 46.66% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4666
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +0.6208 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3460 margin [Increases Default Risk]
  • enq_L3m                             : +0.3291 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.7% (14.27% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature first_prod_enq2_HL (0.00 -> 0.20).
  [X] Convergence failure: Baseline solver failed to cross 40.0% threshold (Achieved PD: 46.66%)

## Evaluating Applicant #337
--------------------------------------------------------------------------------
Calibrated PD: 48.12% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4812
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +2.0165 margin [Increases Default Risk]
  • num_std                             : +0.1856 margin [Increases Default Risk]
  • num_std_12mts                       : +0.1082 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 83.1% (16.88% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature time_since_recent_payment (178.00 -> 4313.00).
  [X] Immutability violation: Cannot alter historical/demographic feature GENDER_M (1.00 -> 0.60).
