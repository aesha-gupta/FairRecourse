# Batch Audit Report: 15 Marginal Applicants per Dataset


# Dataset: GERMAN
================================================================================
Found 34 marginal borderline applicants!

## Evaluating Applicant #2
--------------------------------------------------------------------------------
Calibrated PD: 44.89% (Threshold: 40.0%)

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         0.425              0.225                  N/A
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
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.171
Recourse Cost Metric         0.425              0.225                  1.567
Execution Horizon            1.0 mos            1.0 mos                19.9 mos
Epsilon-Stability            Not Evaluated      95%                    100%
----------------------------------------------------------------------------------------

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
Feasibility Score [0-1]      0.062              0.958                  0.283
Recourse Cost Metric         1.949              0.225                  1.382
Execution Horizon            22.5 mos           1.0 mos                17.2 mos
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
Feasibility Score [0-1]      0.867              0.958                  0.450
Recourse Cost Metric         0.419              0.225                  1.106
Execution Horizon            3.2 mos            1.0 mos                13.2 mos
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

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         2.883              0.425                  N/A
Execution Horizon            36.1 mos           1.0 mos                N/A
Epsilon-Stability            Not Evaluated      80%                    N/A
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

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    PASSED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.325              0.958                  N/A
Recourse Cost Metric         1.512              0.225                  N/A
Execution Horizon            16.2 mos           1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

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
Feasibility Score [0-1]      0.263              0.958                  0.333
Recourse Cost Metric         1.615              0.225                  1.301
Execution Horizon            17.7 mos           1.0 mos                16.0 mos
Epsilon-Stability            Not Evaluated      90%                    100%
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
credit_amount              4280.00            3780.00            Target parameter adjustment
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
Deterministic Feasibility    PASSED             PASSED                 PASSED
Feasibility Score [0-1]      0.958              0.958                  0.233
Recourse Cost Metric         0.425              0.225                  1.467
Execution Horizon            1.0 mos            1.0 mos                18.4 mos
Epsilon-Stability            Not Evaluated      95%                    100%
----------------------------------------------------------------------------------------

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
Feasibility Score [0-1]      0.958              0.958                  0.204
Recourse Cost Metric         0.425              0.225                  1.515
Execution Horizon            1.0 mos            1.0 mos                19.1 mos
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

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         4.675              0.225                  N/A
Execution Horizon            65.1 mos           1.0 mos                N/A
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
Recourse Cost Metric         0.225              0.225                  1.580
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

Audit Metric / Feature       Baseline (DiCE)    FairRecourse (Opt A)   FairRecourse (Opt B)
----------------------------------------------------------------------------------------
Deterministic Feasibility    FAILED             PASSED                 INFEASIBLE
Feasibility Score [0-1]      0.000              0.958                  N/A
Recourse Cost Metric         0.225              0.225                  N/A
Execution Horizon            1.0 mos            1.0 mos                N/A
Epsilon-Stability            Not Evaluated      100%                   N/A
----------------------------------------------------------------------------------------

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

# Dataset: HELOC
================================================================================
      Loaded local dataset file: heloc_dataset.arff
Found 266 marginal borderline applicants!

## Evaluating Applicant #6
--------------------------------------------------------------------------------
Calibrated PD: 40.93% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.4991 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1699 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1239 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #13
--------------------------------------------------------------------------------
Calibrated PD: 47.02% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.3500 margin [Increases Default Risk]
  • AverageMInFile                      : +0.2738 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0585 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #31
--------------------------------------------------------------------------------
Calibrated PD: 48.72% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.4950 margin [Increases Default Risk]
  • savings_balance                     : +0.1762 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.1520 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #36
--------------------------------------------------------------------------------
Calibrated PD: 48.19% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2608 margin [Increases Default Risk]
  • AverageMInFile                      : +0.2139 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.2009 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #38
--------------------------------------------------------------------------------
Calibrated PD: 46.89% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2989 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.2445 margin [Increases Default Risk]
  • NumTradesOpeninLast12M              : +0.0661 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #57
--------------------------------------------------------------------------------
Calibrated PD: 44.99% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.4950 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.1520 margin [Increases Default Risk]
  • savings_balance                     : +0.1427 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #63
--------------------------------------------------------------------------------
Calibrated PD: 41.35% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2444 margin [Increases Default Risk]
  • NumSatisfactoryTrades               : +0.1814 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.0771 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #79
--------------------------------------------------------------------------------
Calibrated PD: 46.17% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • PercentTradesNeverDelq              : +0.1410 margin [Increases Default Risk]
  • ExternalRiskEstimate                : +0.1200 margin [Increases Default Risk]
  • AverageMInFile                      : +0.1196 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #80
--------------------------------------------------------------------------------
Calibrated PD: 48.22% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.2471 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1265 margin [Increases Default Risk]
  • savings_balance                     : +0.0736 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #98
--------------------------------------------------------------------------------
Calibrated PD: 48.77% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.4950 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.1520 margin [Increases Default Risk]
  • savings_balance                     : +0.1484 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #103
--------------------------------------------------------------------------------
Calibrated PD: 48.35% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2336 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.1405 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.1182 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #105
--------------------------------------------------------------------------------
Calibrated PD: 42.47% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.2409 margin [Increases Default Risk]
  • NetFractionRevolvingBurden          : +0.0901 margin [Increases Default Risk]
  • AverageMInFile                      : +0.0818 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #112
--------------------------------------------------------------------------------
Calibrated PD: 48.77% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • NetFractionRevolvingBurden          : +0.4950 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.1520 margin [Increases Default Risk]
  • savings_balance                     : +0.1484 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #117
--------------------------------------------------------------------------------
Calibrated PD: 43.05% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • MSinceMostRecentInqexcl7days        : +0.4908 margin [Increases Default Risk]
  • MSinceMostRecentDelq                : +0.1418 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0600 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #130
--------------------------------------------------------------------------------
Calibrated PD: 43.16% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • ExternalRiskEstimate                : +0.1371 margin [Increases Default Risk]
  • PercentTradesNeverDelq              : +0.1363 margin [Increases Default Risk]
  • PercentInstallTrades                : +0.0599 margin [Increases Default Risk]
Action: Escalate to credit committee.

# Dataset: CIBIL
================================================================================
      Loaded local dataset file: External_Cibil_Dataset.xlsx
Found 370 marginal borderline applicants!

## Evaluating Applicant #37
--------------------------------------------------------------------------------
Calibrated PD: 42.33% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.0380 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.4554 margin [Increases Default Risk]
  • time_since_recent_enq               : +0.2362 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #76
--------------------------------------------------------------------------------
Calibrated PD: 44.37% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.0915 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.4772 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.3485 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #78
--------------------------------------------------------------------------------
Calibrated PD: 46.23% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.0972 margin [Increases Default Risk]
  • num_std                             : +0.2068 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.1429 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #95
--------------------------------------------------------------------------------
Calibrated PD: 44.09% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.5123 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3294 margin [Increases Default Risk]
  • num_std                             : +0.1567 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #127
--------------------------------------------------------------------------------
Calibrated PD: 44.28% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +0.4380 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.2774 margin [Increases Default Risk]
  • time_since_recent_enq               : +0.2348 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #150
--------------------------------------------------------------------------------
Calibrated PD: 43.70% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +0.4120 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.3547 margin [Increases Default Risk]
  • num_std                             : +0.2733 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #203
--------------------------------------------------------------------------------
Calibrated PD: 47.20% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +2.1559 margin [Increases Default Risk]
  • num_std                             : +0.2056 margin [Increases Default Risk]
  • AGE                                 : +0.1559 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #210
--------------------------------------------------------------------------------
Calibrated PD: 40.60% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +1.6335 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3208 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_L12m              : +0.1821 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #218
--------------------------------------------------------------------------------
Calibrated PD: 47.30% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.2793 margin [Increases Default Risk]
  • pct_PL_enq_L6m_of_ever              : +0.3700 margin [Increases Default Risk]
  • num_std                             : +0.1723 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #262
--------------------------------------------------------------------------------
Calibrated PD: 42.68% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +0.9842 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.6970 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.1182 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #273
--------------------------------------------------------------------------------
Calibrated PD: 40.70% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.7060 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.4050 margin [Increases Default Risk]
  • num_std_12mts                       : +0.1677 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #284
--------------------------------------------------------------------------------
Calibrated PD: 46.24% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • time_since_recent_deliquency        : +1.7440 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.3164 margin [Increases Default Risk]
  • time_since_recent_enq               : +0.1584 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #307
--------------------------------------------------------------------------------
Calibrated PD: 41.98% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +1.0182 margin [Increases Default Risk]
  • time_since_recent_deliquency        : +0.4922 margin [Increases Default Risk]
  • time_since_first_deliquency         : +0.1358 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #312
--------------------------------------------------------------------------------
Calibrated PD: 40.63% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • enq_L3m                             : +0.3741 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3541 margin [Increases Default Risk]
  • num_std                             : +0.2037 margin [Increases Default Risk]
Action: Escalate to credit committee.

## Evaluating Applicant #324
--------------------------------------------------------------------------------
Calibrated PD: 46.74% (Threshold: 40.0%)
AUDIT ASSESSMENT: RECOURSE MATHEMATICALLY INFEASIBLE
  • pct_PL_enq_L6m_of_ever              : +0.6265 margin [Increases Default Risk]
  • pct_of_active_TLs_ever              : +0.3578 margin [Increases Default Risk]
  • enq_L3m                             : +0.3408 margin [Increases Default Risk]
Action: Escalate to credit committee.
