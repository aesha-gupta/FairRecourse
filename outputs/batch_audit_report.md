# Batch Audit Report: 30 Marginal Applicants per Dataset


# Dataset: GERMAN
================================================================================
Found 34 marginal borderline applicants!

## Evaluating Applicant #2
--------------------------------------------------------------------------------
Calibrated PD: 44.89% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4489

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

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
Recourse Cost Metric         3.245              0.225                  1.567
Execution Horizon            44.3 mos           1.0 mos                19.9 mos
Epsilon-Stability            Not Evaluated      85%                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (44.3 > 24.0 months)

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
Lowest PD reached by solver: 0.4044

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.425              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0023
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 48.0%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4478 margin [Increases Default Risk]
• monthly_income            : +0.4383 margin [Increases Default Risk]
• savings_balance           : +0.3809 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            24.00              12.00              Restructure tenure
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

## Evaluating Applicant #24
--------------------------------------------------------------------------------
Calibrated PD: 42.58% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.283
Recourse Cost Metric         0.225              0.225                  1.382
Execution Horizon            1.0 mos            1.0 mos                17.2 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

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
Recourse Cost Metric         0.225              0.225                  1.106
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
Lowest PD reached by solver: 0.4969

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.225              0.425                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0041
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 49.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.5842 margin [Increases Default Risk]
• savings_balance           : +0.3827 margin [Increases Default Risk]
• monthly_income            : +0.2472 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            48.00              42.00              Restructure tenure
credit_amount              3060.00            560.00             Target parameter adjustment
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : € 0.00 / month
Total Financial Shift         : € 0.00
Composite Recourse Cost       : 0.425
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #46
--------------------------------------------------------------------------------
Calibrated PD: 46.04% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4604

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         9.859              0.225                  N/A
Execution Horizon            137.6 mos          1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (137.6 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0046
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 46.0%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• savings_balance           : +0.3321 margin [Increases Default Risk]
• monthly_income            : +0.2903 margin [Increases Default Risk]
• number_existing_credits   : +0.1985 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            18.00              6.00               Restructure tenure
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

## Evaluating Applicant #47
--------------------------------------------------------------------------------
Calibrated PD: 46.32% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.333
Recourse Cost Metric         0.225              0.225                  1.301
Execution Horizon            1.0 mos            1.0 mos                16.0 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

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

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.233
Recourse Cost Metric         2.054              0.225                  1.467
Execution Horizon            27.0 mos           1.0 mos                18.4 mos
Epsilon-Stability            Not Evaluated      85%                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (27.0 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
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
duration_months            48.00              36.00              Restructure tenure
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

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (508.95 -> 667.29).

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0054
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.1%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• savings_balance           : +0.3237 margin [Increases Default Risk]
• monthly_income            : +0.3005 margin [Increases Default Risk]
• number_existing_credits   : +0.2019 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            18.00              6.00               Restructure tenure
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

## Evaluating Applicant #58
--------------------------------------------------------------------------------
Calibrated PD: 47.87% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.279              0.958                  0.204
Recourse Cost Metric         1.390              0.225                  1.515
Execution Horizon            17.3 mos           1.0 mos                19.1 mos
Epsilon-Stability            Not Evaluated      75%                    100%
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
Lowest PD reached by solver: 0.4054

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0059
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 47.5%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5094 margin [Increases Default Risk]
• savings_balance           : +0.3509 margin [Increases Default Risk]
• duration_months           : +0.2742 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            36.00              12.00              Restructure tenure
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

## Evaluating Applicant #78
--------------------------------------------------------------------------------
Calibrated PD: 49.56% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4956

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         3.220              0.225                  N/A
Execution Horizon            41.0 mos           1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (41.0 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0078
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 49.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.3939 margin [Increases Default Risk]
• people_liable             : +0.3246 margin [Increases Default Risk]
• savings_balance           : +0.3245 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            24.00              6.00               Restructure tenure
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

## Evaluating Applicant #79
--------------------------------------------------------------------------------
Calibrated PD: 42.94% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.162
Recourse Cost Metric         0.425              0.225                  1.580
Execution Horizon            1.0 mos            1.0 mos                20.1 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

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
Lowest PD reached by solver: 0.4827

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         4.860              0.225                  N/A
Execution Horizon            64.9 mos           1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (64.9 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0080
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 48.3%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• savings_balance           : +0.3664 margin [Increases Default Risk]
• duration_months           : +0.3437 margin [Increases Default Risk]
• monthly_income            : +0.2633 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            36.00              12.00              Restructure tenure
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

## Evaluating Applicant #82
--------------------------------------------------------------------------------
Calibrated PD: 48.57% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.787
Recourse Cost Metric         0.225              0.225                  0.550
Execution Horizon            1.0 mos            1.0 mos                5.1 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0082
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 48.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.6437 margin [Increases Default Risk]
• savings_balance           : +0.3880 margin [Increases Default Risk]
• duration_months           : +0.3238 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              8086.00            7586.00            Target parameter adjustment
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
Applicant Case ID    : APP-0082
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 48.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.6437 margin [Increases Default Risk]
• savings_balance           : +0.3880 margin [Increases Default Risk]
• duration_months           : +0.3238 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            750.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 5.1 Months
Monthly Commitment Required   : € 98.04 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 0.55
Feasibility Score             : 0.787 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #84
--------------------------------------------------------------------------------
Calibrated PD: 48.06% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4806

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0084
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 48.1%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5771 margin [Increases Default Risk]
• credit_amount             : +0.3475 margin [Increases Default Risk]
• number_existing_credits   : +0.2879 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            12.00              6.00               Restructure tenure
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

## Evaluating Applicant #97
--------------------------------------------------------------------------------
Calibrated PD: 41.81% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.342
Recourse Cost Metric         0.425              0.225                  1.285
Execution Horizon            1.0 mos            1.0 mos                15.8 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0097
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.8%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.4659 margin [Increases Default Risk]
• savings_balance           : +0.3808 margin [Increases Default Risk]
• duration_months           : +0.2539 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            27.00              15.00              Restructure tenure
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
Applicant Case ID    : APP-0097
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.8%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.4659 margin [Increases Default Risk]
• savings_balance           : +0.3808 margin [Increases Default Risk]
• duration_months           : +0.2539 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 15.8 Months
Monthly Commitment Required   : € 31.65 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.285
Feasibility Score             : 0.342 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #116
--------------------------------------------------------------------------------
Calibrated PD: 44.33% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4433

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.438              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0116
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.3%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4493 margin [Increases Default Risk]
• monthly_income            : +0.1607 margin [Increases Default Risk]
• savings_balance           : +0.1186 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            45.00              39.00              Restructure tenure
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

## Evaluating Applicant #122
--------------------------------------------------------------------------------
Calibrated PD: 40.63% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.438
Recourse Cost Metric         4.038              0.225                  1.130
Execution Horizon            52.9 mos           1.0 mos                13.5 mos
Epsilon-Stability            Not Evaluated      95%                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (52.9 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0122
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 40.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4589 margin [Increases Default Risk]
• savings_balance           : +0.4134 margin [Increases Default Risk]
• monthly_income            : +0.2516 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              3416.00            2916.00            Target parameter adjustment
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
Applicant Case ID    : APP-0122
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 40.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4589 margin [Increases Default Risk]
• savings_balance           : +0.4134 margin [Increases Default Risk]
• monthly_income            : +0.2516 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 13.5 Months
Monthly Commitment Required   : € 37.04 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.13
Feasibility Score             : 0.438 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #124
--------------------------------------------------------------------------------
Calibrated PD: 40.91% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.558
Recourse Cost Metric         0.225              0.225                  0.931
Execution Horizon            1.0 mos            1.0 mos                10.6 mos
Epsilon-Stability            Not Evaluated      95%                    100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0124
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 40.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.6026 margin [Increases Default Risk]
• savings_balance           : +0.3777 margin [Increases Default Risk]
• duration_months           : +0.2520 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              5152.00            3652.00            Target parameter adjustment
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
Applicant Case ID    : APP-0124
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 40.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.6026 margin [Increases Default Risk]
• savings_balance           : +0.3777 margin [Increases Default Risk]
• duration_months           : +0.2520 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 10.6 Months
Monthly Commitment Required   : € 47.17 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 0.931
Feasibility Score             : 0.558 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #134
--------------------------------------------------------------------------------
Calibrated PD: 42.28% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4228

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         13.351             0.225                  N/A
Execution Horizon            188.4 mos          1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (188.4 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0134
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 42.3%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.4808 margin [Increases Default Risk]
• duration_months           : +0.2839 margin [Increases Default Risk]
• number_existing_credits   : +0.2664 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              1358.00            358.00             Target parameter adjustment
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

## Evaluating Applicant #135
--------------------------------------------------------------------------------
Calibrated PD: 44.82% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.121
Recourse Cost Metric         0.425              0.225                  1.650
Execution Horizon            1.0 mos            1.0 mos                21.1 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (439.20 -> 6812.58).

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0135
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.8%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5199 margin [Increases Default Risk]
• savings_balance           : +0.3433 margin [Increases Default Risk]
• duration_months           : +0.3206 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            18.00              12.00              Restructure tenure
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
Applicant Case ID    : APP-0135
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 44.8%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.5199 margin [Increases Default Risk]
• savings_balance           : +0.3433 margin [Increases Default Risk]
• duration_months           : +0.3206 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 21.1 Months
Monthly Commitment Required   : € 47.39 / month
Total Financial Shift         : € 1000.00
Composite Recourse Cost       : 1.65
Feasibility Score             : 0.121 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #137
--------------------------------------------------------------------------------
Calibrated PD: 45.86% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4586

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0137
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 45.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• people_liable             : +0.3223 margin [Increases Default Risk]
• savings_balance           : +0.3170 margin [Increases Default Risk]
• duration_months           : +0.3099 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            24.00              6.00               Restructure tenure
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

## Evaluating Applicant #138
--------------------------------------------------------------------------------
Calibrated PD: 41.66% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.887
Recourse Cost Metric         0.225              0.225                  0.385
Execution Horizon            1.0 mos            1.0 mos                2.7 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0138
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.4796 margin [Increases Default Risk]
• savings_balance           : +0.3337 margin [Increases Default Risk]
• duration_months           : +0.2959 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              4272.00            3772.00            Target parameter adjustment
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
Applicant Case ID    : APP-0138
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.4796 margin [Increases Default Risk]
• savings_balance           : +0.3337 margin [Increases Default Risk]
• duration_months           : +0.2959 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 2.7 Months
Monthly Commitment Required   : € 185.19 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 0.385
Feasibility Score             : 0.887 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #143
--------------------------------------------------------------------------------
Calibrated PD: 41.39% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4139

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         0.425              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (1098.90 -> 6353.56).

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0143
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.4%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.3784 margin [Increases Default Risk]
• savings_balance           : +0.3726 margin [Increases Default Risk]
• people_liable             : +0.2700 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            27.00              15.00              Restructure tenure
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

## Evaluating Applicant #145
--------------------------------------------------------------------------------
Calibrated PD: 47.58% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4758

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         0.425              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (341.55 -> 1355.80).

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0145
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 47.6%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• monthly_income            : +0.6009 margin [Increases Default Risk]
• credit_amount             : +0.3475 margin [Increases Default Risk]
• number_existing_credits   : +0.2879 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            12.00              6.00               Restructure tenure
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

## Evaluating Applicant #156
--------------------------------------------------------------------------------
Calibrated PD: 43.21% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 PASSED
Feasibility Score [0-1]      0.000              0.958                  0.258
Recourse Cost Metric         4.997              0.225                  1.423
Execution Horizon            66.9 mos           1.0 mos                17.8 mos
Epsilon-Stability            Not Evaluated      100%                   100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Exceeds max execution horizon (66.9 > 24.0 months)

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0156
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 43.2%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4073 margin [Increases Default Risk]
• savings_balance           : +0.3756 margin [Increases Default Risk]
• number_existing_credits   : +0.1998 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
duration_months            30.00              12.00              Restructure tenure
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
Applicant Case ID    : APP-0156
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 43.2%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• duration_months           : +0.4073 margin [Increases Default Risk]
• savings_balance           : +0.3756 margin [Increases Default Risk]
• number_existing_credits   : +0.1998 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            250.00             750.00             Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 17.8 Months
Monthly Commitment Required   : € 28.09 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 1.423
Feasibility Score             : 0.258 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #159
--------------------------------------------------------------------------------
Calibrated PD: 41.69% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4169

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.958              0.958                  N/A
Recourse Cost Metric         0.425              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0159
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.7%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• savings_balance           : +0.2731 margin [Increases Default Risk]
• duration_months           : +0.2331 margin [Increases Default Risk]
• credit_amount             : +0.0663 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              1199.00            699.00             Target parameter adjustment
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

## Evaluating Applicant #164
--------------------------------------------------------------------------------
Calibrated PD: 49.87% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.717
Recourse Cost Metric         0.225              0.225                  0.666
Execution Horizon            1.0 mos            1.0 mos                6.8 mos
Epsilon-Stability            Not Evaluated      95%                    100%
----------------------------------------------------------------------------------------

>>> [OPTION A: CONTRACTUAL RESTRUCTURING CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-GERMAN-OPT-A
Applicant Case ID    : APP-0164
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 49.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.7523 margin [Increases Default Risk]
• duration_months           : +0.4420 margin [Increases Default Risk]
• savings_balance           : +0.3188 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
credit_amount              10144.00           7644.00            Target parameter adjustment
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
Applicant Case ID    : APP-0164
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 49.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• credit_amount             : +0.7523 margin [Increases Default Risk]
• duration_months           : +0.4420 margin [Increases Default Risk]
• savings_balance           : +0.3188 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
savings_balance            750.00             1250.00            Accumulate liquidity
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 6.8 Months
Monthly Commitment Required   : € 73.53 / month
Total Financial Shift         : € 500.00
Composite Recourse Cost       : 0.666
Feasibility Score             : 0.717 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

# Dataset: HELOC
================================================================================
      Loaded local dataset file: heloc_dataset.arff
Found 260 marginal borderline applicants!

## Evaluating Applicant #13
--------------------------------------------------------------------------------
Calibrated PD: 44.02% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4437
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.4585 margin [Increases Default Risk]
  • AverageMInFile                      : +0.2711 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0697 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 90.9% (9.14% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentInstallTrades (20.00 -> 84.80).

## Evaluating Applicant #22
--------------------------------------------------------------------------------
Calibrated PD: 46.65% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4513
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.6305 margin [Increases Default Risk]
  • NumInqLast6M                        : +0.1090 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.0763 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.7% (14.25% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumInqLast6Mexcl7days (0.00 -> 10.70).
  [X] Discrete count violation: NumInqLast6Mexcl7days must be an integer, received 10.70.

## Evaluating Applicant #31
--------------------------------------------------------------------------------
Calibrated PD: 48.29% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4799
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.0980 margin [Increases Default Risk]
  • MSinceMostRecentTradeOpen           : +0.0589 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0403 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 82.8% (17.16% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Quality metric savings_balance cannot decrease (5326.53 -> 2953.55).
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (980.00 -> 3992.00).

## Evaluating Applicant #36
--------------------------------------------------------------------------------
Calibrated PD: 47.58% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4574
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3116 margin [Increases Default Risk]
  • MSinceMostRecentInqexcl7days        : +0.2666 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.2275 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 84.1% (15.93% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Domain bounds violation: NetFractionInstallBurden must be within [0, 100]%, received 101.00%.
  [X] Immutability violation: Cannot alter historical/demographic feature NumBank2NatlTradesWHighUtilization (0.00 -> 9.70).
  [X] Discrete count violation: NumBank2NatlTradesWHighUtilization must be an integer, received 9.70.

## Evaluating Applicant #38
--------------------------------------------------------------------------------
Calibrated PD: 45.12% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4493
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2854 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.1716 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0607 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 88.7% (11.34% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades90Ever2DerogPubRec (0.00 -> 5.10).
  [X] Discrete count violation: NumTrades90Ever2DerogPubRec must be an integer, received 5.10.
  [X] Immutability violation: Cannot alter historical/demographic feature NumRevolvingTradesWBalance (7.00 -> 30.20).
  [X] Discrete count violation: NumRevolvingTradesWBalance must be an integer, received 30.20.

## Evaluating Applicant #87
--------------------------------------------------------------------------------
Calibrated PD: 41.48% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             PASSED
Feasibility Score [0-1]      0.000              N/A                    0.958
Recourse Cost Metric         0.225              N/A                    0.236
Execution Horizon            1.0 mos            N/A                    1.0 mos
Epsilon-Stability            Not Evaluated      N/A                    100%
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Quality metric savings_balance cannot decrease (6800.32 -> 3216.13).

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-HELOC-OPT-B
Applicant Case ID    : APP-0087
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 41.5%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• ExternalRiskEstimate      : +0.4037 margin [Increases Default Risk]
• NetFractionRevolvingBurden : +0.2057 margin [Increases Default Risk]
• PercentTradesNeverDelq    : +0.0941 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
NetFractionInstallBurden   96.00              86.00              Pay down balance / reduce utilization
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 1.0 Months
Monthly Commitment Required   : $ 100.00 / month
Total Financial Shift         : $ 100.00
Composite Recourse Cost       : 0.236
Feasibility Score             : 0.958 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #98
--------------------------------------------------------------------------------
Calibrated PD: 49.64% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4869
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.0888 margin [Increases Default Risk]
  • MSinceMostRecentTradeOpen           : +0.0503 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0399 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.6% (19.42% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Quality metric monthly_income cannot decrease (4382.56 -> 2262.43).

## Evaluating Applicant #102
--------------------------------------------------------------------------------
Calibrated PD: 44.29% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4362
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.3028 margin [Increases Default Risk]
  • MSinceMostRecentInqexcl7days        : +0.1691 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1588 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 90.3% (9.68% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (175.00 -> 1505.00).

## Evaluating Applicant #103
--------------------------------------------------------------------------------
Calibrated PD: 41.84% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4126
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2383 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1542 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.0319 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 95.6% (4.39% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentTradesWBalance (18.00 -> 62.40).

## Evaluating Applicant #105
--------------------------------------------------------------------------------
Calibrated PD: 43.65% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4259
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.3117 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1374 margin [Increases Default Risk]
  • NumInqLast6M                        : +0.1094 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 91.6% (8.36% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentTradesNeverDelq (67.00 -> 86.60).
  [X] Monotonicity violation: Adverse risk metric NetFractionRevolvingBurden cannot increase (40.00 -> 82.70).

## Evaluating Applicant #112
--------------------------------------------------------------------------------
Calibrated PD: 49.57% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4862
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.1054 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0402 margin [Increases Default Risk]
  • MSinceMostRecentTradeOpen           : +0.0374 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.7% (19.3% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.958              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------

## Evaluating Applicant #117
--------------------------------------------------------------------------------
Calibrated PD: 42.20% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4009
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.3965 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0562 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.0389 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 94.8% (5.21% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentTradesNeverDelq (78.00 -> 96.00).

## Evaluating Applicant #120
--------------------------------------------------------------------------------
Calibrated PD: 43.10% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4112
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NumSatisfactoryTrades               : +0.2020 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1943 margin [Increases Default Risk]
  • monthly_income                      : +0.0913 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 92.8% (7.19% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades90Ever2DerogPubRec (0.00 -> 2.40).
  [X] Discrete count violation: NumTrades90Ever2DerogPubRec must be an integer, received 2.40.
  [X] Monotonicity violation: Quality metric savings_balance cannot decrease (4880.61 -> 1345.23).

## Evaluating Applicant #126
--------------------------------------------------------------------------------
Calibrated PD: 43.24% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4219
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.0932 margin [Increases Default Risk]
  • NetFractionInstallBurden            : +0.0435 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0397 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 92.5% (7.48% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades90Ever2DerogPubRec (0.00 -> 6.60).
  [X] Discrete count violation: NumTrades90Ever2DerogPubRec must be an integer, received 6.60.
  [X] Immutability violation: Cannot alter historical/demographic feature NumRevolvingTradesWBalance (3.00 -> 3.10).
  [X] Discrete count violation: NumRevolvingTradesWBalance must be an integer, received 3.10.

## Evaluating Applicant #130
--------------------------------------------------------------------------------
Calibrated PD: 40.89% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             INFEASIBLE             PASSED
Feasibility Score [0-1]      0.958              N/A                    0.650
Recourse Cost Metric         0.225              N/A                    0.643
Execution Horizon            1.0 mos            N/A                    8.4 mos
Epsilon-Stability            Not Evaluated      N/A                    100%
----------------------------------------------------------------------------------------

>>> [OPTION B: BALANCE SHEET & LIQUIDITY CERTIFICATE]
================================================================================
                    FAIRRECOURSE UNDERWRITING AUDIT LOG                         
================================================================================
Audit Reference      : FR-2026-HELOC-OPT-B
Applicant Case ID    : APP-0130
Model Assessment     : Risk Threshold Exceeded
Calibrated PD        : 40.9%  [Operational Threshold: 40.0%]
Recourse Target      : < 40.0%

PRIMARY ADVERSE DETERMINATION DRIVERS (TreeSHAP Local Attribution)
--------------------------------------------------------------------------------
• ExternalRiskEstimate      : +0.1156 margin [Increases Default Risk]
• NumSatisfactoryTrades     : +0.0755 margin [Increases Default Risk]
• PercentTradesNeverDelq    : +0.0681 margin [Increases Default Risk]

FEASIBILITY-OPTIMIZED RECOURSE INTERVENTION
--------------------------------------------------------------------------------
Variable                   Current Value      Target Recourse    Intervention Plan
--------------------------------------------------------------------------------
NetFractionInstallBurden   100.00             10.00              Pay down balance / reduce utilization
--------------------------------------------------------------------------------

RECOURSE FEASIBILITY & TEMPORAL AUDIT
--------------------------------------------------------------------------------
Estimated Execution Horizon   : 8.4 Months
Monthly Commitment Required   : $ 202.50 / month
Total Financial Shift         : $ 1701.00
Composite Recourse Cost       : 0.643
Feasibility Score             : 0.65 / 1.000
Deterministic Constraint Check: PASSED (Zero Violations)

DISCLAIMER: This certificate reports the mathematical criteria required to satisfy
the calibrated risk model. It does not constitute a legally binding credit offer;
final underwriting is subject to human-in-the-loop audit and regulatory compliance.
================================================================================

## Evaluating Applicant #131
--------------------------------------------------------------------------------
Calibrated PD: 44.52% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4314
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3218 margin [Increases Default Risk]
  • MSinceOldestTradeOpen               : +0.0982 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0786 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.8% (10.16% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature MSinceOldestTradeOpen (280.00 -> 520.90).

## Evaluating Applicant #136
--------------------------------------------------------------------------------
Calibrated PD: 49.71% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4876
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.1135 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0403 margin [Increases Default Risk]
  • MSinceMostRecentTradeOpen           : +0.0378 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.5% (19.53% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades90Ever2DerogPubRec (0.00 -> 6.20).
  [X] Discrete count violation: NumTrades90Ever2DerogPubRec must be an integer, received 6.20.

## Evaluating Applicant #138
--------------------------------------------------------------------------------
Calibrated PD: 42.94% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4294
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.2856 margin [Increases Default Risk]
  • NumInqLast6M                        : +0.0836 margin [Increases Default Risk]
  • MSinceOldestTradeOpen               : +0.0813 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 93.2% (6.84% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentTradesNeverDelq (88.00 -> 70.30).

## Evaluating Applicant #143
--------------------------------------------------------------------------------
Calibrated PD: 49.43% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4848
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.1052 margin [Increases Default Risk]
  • MSinceMostRecentTradeOpen           : +0.0498 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0406 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.9% (19.07% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumInqLast6Mexcl7days (1.00 -> 44.50).
  [X] Discrete count violation: NumInqLast6Mexcl7days must be an integer, received 44.50.

## Evaluating Applicant #144
--------------------------------------------------------------------------------
Calibrated PD: 47.69% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4769
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.2818 margin [Increases Default Risk]
  • MSinceMostRecentInqexcl7days        : +0.2439 margin [Increases Default Risk]
  • monthly_income                      : +0.0747 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 83.9% (16.13% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumRevolvingTradesWBalance (5.00 -> 7.60).
  [X] Discrete count violation: NumRevolvingTradesWBalance must be an integer, received 7.60.

## Evaluating Applicant #166
--------------------------------------------------------------------------------
Calibrated PD: 49.58% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4837
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3278 margin [Increases Default Risk]
  • NumInqLast6M                        : +0.0949 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0817 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.7% (19.33% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature AverageMInFile (106.00 -> 95.50).

## Evaluating Applicant #170
--------------------------------------------------------------------------------
Calibrated PD: 41.00% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4020
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.3659 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1789 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.0667 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 97.5% (2.45% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades90Ever2DerogPubRec (0.00 -> 0.50).
  [X] Discrete count violation: NumTrades90Ever2DerogPubRec must be an integer, received 0.50.
  [X] Immutability violation: Cannot alter historical/demographic feature PercentInstallTrades (59.00 -> 18.50).

## Evaluating Applicant #182
--------------------------------------------------------------------------------
Calibrated PD: 47.08% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4627
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.4370 margin [Increases Default Risk]
  • AverageMInFile                      : +0.3074 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.1674 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.0% (15.04% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades60Ever2DerogPubRec (1.00 -> 3.50).
  [X] Discrete count violation: NumTrades60Ever2DerogPubRec must be an integer, received 3.50.

## Evaluating Applicant #186
--------------------------------------------------------------------------------
Calibrated PD: 47.58% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4681
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3434 margin [Increases Default Risk]
  • NumInqLast6M                        : +0.0823 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.0803 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 84.1% (15.94% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTotalTrades (23.00 -> 37.40).
  [X] Discrete count violation: NumTotalTrades must be an integer, received 37.40.

## Evaluating Applicant #201
--------------------------------------------------------------------------------
Calibrated PD: 47.87% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4760
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3350 margin [Increases Default Risk]
  • NumInqLast6M                        : +0.1073 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.1045 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 83.6% (16.44% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumRevolvingTradesWBalance (5.00 -> 12.20).
  [X] Discrete count violation: NumRevolvingTradesWBalance must be an integer, received 12.20.

## Evaluating Applicant #203
--------------------------------------------------------------------------------
Calibrated PD: 47.58% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4707
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.2579 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.2425 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.0738 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 84.1% (15.93% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades60Ever2DerogPubRec (0.00 -> 15.20).
  [X] Discrete count violation: NumTrades60Ever2DerogPubRec must be an integer, received 15.20.

## Evaluating Applicant #217
--------------------------------------------------------------------------------
Calibrated PD: 44.80% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4206
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.3471 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1694 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.0766 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.3% (10.71% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PercentInstallTrades (56.00 -> 98.50).

## Evaluating Applicant #218
--------------------------------------------------------------------------------
Calibrated PD: 49.57% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4939
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.3099 margin [Increases Default Risk]
  • AverageMInFile                      : +0.2413 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1191 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.7% (19.3% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTrades60Ever2DerogPubRec (1.00 -> 17.40).
  [X] Discrete count violation: NumTrades60Ever2DerogPubRec must be an integer, received 17.40.

## Evaluating Applicant #220
--------------------------------------------------------------------------------
Calibrated PD: 48.80% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4880
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • AverageMInFile                      : +0.3809 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.1094 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.0636 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 82.0% (18.03% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature NumTradesOpeninLast12M (4.00 -> 4.60).
  [X] Discrete count violation: NumTradesOpeninLast12M must be an integer, received 4.60.
  [X] Immutability violation: Cannot alter historical/demographic feature NumInqLast6Mexcl7days (0.00 -> 24.00).

## Evaluating Applicant #222
--------------------------------------------------------------------------------
Calibrated PD: 49.22% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4811
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.1205 margin [Increases Default Risk]
  • MSinceMostRecentTradeOpen           : +0.0433 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0405 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 81.3% (18.74% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature MSinceMostRecentTradeOpen (999.00 -> 976.60).

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
Deterministic Feasibility    PASSED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.958              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------

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

## Evaluating Applicant #349
--------------------------------------------------------------------------------
Calibrated PD: 41.34% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4156
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +0.7787 margin [Increases Default Risk]
  • max_deliq_12mts                     : +0.4239 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.3789 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 96.7% (3.25% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature time_since_recent_payment (52.00 -> 649.00).
  [X] Immutability violation: Cannot alter historical/demographic feature enq_L12m (3.00 -> 63.00).

## Evaluating Applicant #377
--------------------------------------------------------------------------------
Calibrated PD: 42.93% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4293
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.1185 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.8985 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.1252 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 93.2% (6.83% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature enq_L12m (2.00 -> 75.00).
  [X] Monotonicity violation: Adverse risk metric revolving_debt cannot increase (0.00 -> 2450.30).

## Evaluating Applicant #379
--------------------------------------------------------------------------------
Calibrated PD: 42.48% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4248
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.1460 margin [Increases Default Risk]
  • num_std                             : +0.2328 margin [Increases Default Risk]
  • enq_L3m                             : +0.1483 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 94.2% (5.84% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature CC_enq_L12m (0.00 -> 6.00).

## Evaluating Applicant #393
--------------------------------------------------------------------------------
Calibrated PD: 44.59% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4459
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.6875 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.4379 margin [Increases Default Risk]
  • num_std                             : +0.1928 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 89.7% (10.3% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature last_prod_enq2_ConsumerLoan (1.00 -> 0.50).

## Evaluating Applicant #437
--------------------------------------------------------------------------------
Calibrated PD: 49.62% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4962
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_of_active_TLs_ever              : +0.3776 margin [Increases Default Risk]
  • enq_L3m                             : +0.2746 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.2722 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 80.6% (19.4% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.958              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------

## Evaluating Applicant #456
--------------------------------------------------------------------------------
Calibrated PD: 41.31% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4131
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • max_deliq_12mts                     : +1.3501 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.4147 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.1831 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 96.8% (3.16% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature pct_CC_enq_L6m_of_ever (0.00 -> 0.10).
  [X] Immutability violation: Cannot alter historical/demographic feature last_prod_enq2_ConsumerLoan (0.00 -> 1.00).

## Evaluating Applicant #487
--------------------------------------------------------------------------------
Calibrated PD: 42.04% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4204
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.4493 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.8663 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.1043 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 95.1% (4.86% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         15.784             N/A                    N/A
Execution Horizon            269.8 mos          N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature max_recent_level_of_deliq (0.00 -> 303.00).
  [X] Exceeds max execution horizon (269.8 > 24.0 months)

## Evaluating Applicant #526
--------------------------------------------------------------------------------
Calibrated PD: 46.86% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4686
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +2.0180 margin [Increases Default Risk]
  • num_std                             : +0.1862 margin [Increases Default Risk]
  • num_std_12mts                       : +0.1075 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 85.4% (14.64% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.958              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------

## Evaluating Applicant #559
--------------------------------------------------------------------------------
Calibrated PD: 45.37% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4537
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.7525 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.4070 margin [Increases Default Risk]
  • num_std                             : +0.1912 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 88.2% (11.84% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PL_enq_L6m (0.00 -> 34.00).
  [X] Immutability violation: Cannot alter historical/demographic feature GENDER_M (0.00 -> 0.50).

## Evaluating Applicant #564
--------------------------------------------------------------------------------
Calibrated PD: 48.25% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4825
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.1976 margin [Increases Default Risk]
  • num_std                             : +0.2209 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.1429 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 82.9% (17.1% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_dbt (0.00 -> 7.00).

## Evaluating Applicant #619
--------------------------------------------------------------------------------
Calibrated PD: 48.82% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4882
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +2.5976 margin [Increases Default Risk]
  • num_std                             : +0.1383 margin [Increases Default Risk]
  • num_std_12mts                       : +0.1041 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 81.9% (18.06% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_deliq_6mts (0.00 -> 9.00).

## Evaluating Applicant #620
--------------------------------------------------------------------------------
Calibrated PD: 40.68% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4068
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.2840 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.5579 margin [Increases Default Risk]
  • num_std                             : +0.2357 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 98.3% (1.67% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature num_dbt_12mts (0.00 -> 9.00).
  [X] Immutability violation: Cannot alter historical/demographic feature first_prod_enq2_PL (0.00 -> 0.10).

## Evaluating Applicant #625
--------------------------------------------------------------------------------
Calibrated PD: 41.21% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4121
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.6390 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.2945 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.2131 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 97.1% (2.93% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.425              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature PL_enq_L6m (3.00 -> 30.00).
  [X] Immutability violation: Cannot alter historical/demographic feature GENDER_M (1.00 -> 0.40).

## Evaluating Applicant #693
--------------------------------------------------------------------------------
Calibrated PD: 44.24% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4424
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +0.6812 margin [Increases Default Risk]
  • enq_L3m                             : +0.3239 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.2985 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 90.4% (9.59% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.958              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------

## Evaluating Applicant #715
--------------------------------------------------------------------------------
Calibrated PD: 42.20% (Threshold: 40.0%)
Lowest PD reached by solver: 0.4220
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.1636 margin [Increases Default Risk]
  • num_std                             : +0.2006 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.1474 margin [Increases Default Risk]
Action: Escalate to credit committee.
-> EXPOSURE SCALING ANALYSIS: Approved under an Exposure Scaling Cap of 94.8% (5.22% facility limit haircut) preserving portfolio risk neutral tolerance.

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             INFEASIBLE             INFEASIBLE
Feasibility Score [0-1]      0.000              N/A                    N/A
Recourse Cost Metric         0.225              N/A                    N/A
Execution Horizon            1.0 mos            N/A                    N/A
Epsilon-Stability            Not Evaluated      N/A                    N/A
----------------------------------------------------------------------------------------
BASELINE VIOLATIONS CAUGHT BY PCL:
  [X] Immutability violation: Cannot alter historical/demographic feature pct_PL_enq_L6m_of_L12m (1.00 -> 0.20).
