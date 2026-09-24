import os
import io
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


def load_and_preprocess_german_credit(test_size: float = 0.2, random_state: int = 42):
    """Downloads and prepares the Statlog German Credit benchmark dataset."""
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/german/german.data"
    column_names = [
        "status_checking", "duration_months", "credit_history", "purpose",
        "credit_amount", "savings_account", "present_employment_since",
        "installment_rate", "personal_status_sex", "other_debtors",
        "present_residence_since", "property", "age", "other_installment_plans",
        "housing", "number_existing_credits", "job", "people_liable",
        "telephone", "foreign_worker", "default"
    ]
    df = pd.read_csv(url, sep=" ", header=None, names=column_names)

    df["target"] = (df["default"] == 2).astype(int)
    df = df.drop(columns=["default"])

    df["gender"] = df["personal_status_sex"].apply(
        lambda x: "Female" if x in ["A92", "A95"] else "Male"
    )
    df["age_group"] = df["age"].apply(lambda x: "Under_25" if x < 25 else "25_and_Over")

    df["monthly_income"] = np.round((df["credit_amount"] / df["duration_months"]) * (100 / (df["installment_rate"] * 10)), 2)
    df["disposable_income"] = np.round(df["monthly_income"] * 0.35, 2)
    df["revolving_debt"] = np.round(df["credit_amount"] * 0.45, 2)

    savings_mapping = {"A61": 250.0, "A62": 750.0, "A63": 1250.0, "A64": 2500.0, "A65": 50.0}
    df["savings_balance"] = df["savings_account"].map(savings_mapping).fillna(100.0)

    underwriting_features = [
        "duration_months", "credit_amount", "installment_rate",
        "present_residence_since", "number_existing_credits", "people_liable",
        "monthly_income", "disposable_income", "revolving_debt", "savings_balance"
    ]

    X = df[underwriting_features]
    y = df["target"]
    A = df[["gender", "age_group", "age"]]

    return train_test_split(
        X, y, A, test_size=test_size, random_state=random_state, stratify=y
    )


def load_and_preprocess_heloc(test_size: float = 0.2, random_state: int = 42):
    """
    Loads HELOC from root or data/ directory, parsing either CSV or ARFF formats.
    """
    candidates = [
        "heloc_dataset_v1.csv", "heloc_dataset.csv", "heloc.csv",
        "heloc_dataset_v1 (1).csv", "heloc_dataset.arff", "heloc.arff",
        os.path.join("data", "heloc_dataset_v1.csv"),
        os.path.join("data", "heloc_dataset.csv"),
        os.path.join("data", "heloc_dataset.arff"),
    ]

    target_path = None
    for p in candidates:
        if os.path.exists(p):
            target_path = p
            break

    if target_path is None:
        for fname in os.listdir("."):
            if "heloc" in fname.lower() and (fname.endswith(".csv") or fname.endswith(".arff")):
                target_path = fname
                break

    if target_path is None:
        raise FileNotFoundError("Could not find a HELOC file (.csv or .arff) in root directory or data/ folder.")

    print(f"      Loaded local dataset file: {target_path}")

    if target_path.endswith(".arff"):
        with open(target_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        attributes, data_lines, is_data = [], [], False
        for line in lines:
            line_str = line.strip()
            if not line_str or line_str.startswith("%"):
                continue
            if line_str.lower().startswith("@attribute"):
                attributes.append(line_str.split()[1])
            elif line_str.lower().startswith("@data"):
                is_data = True
            elif is_data:
                data_lines.append(line_str)
        df = pd.read_csv(io.StringIO("\n".join(data_lines)), header=None, names=attributes)
    else:
        df = pd.read_csv(target_path)

    target_col = "RiskPerformance" if "RiskPerformance" in df.columns else df.columns[-1]
    if df[target_col].dtype == object:
        df["target"] = df[target_col].astype(str).str.strip().str.lower().map({"bad": 1, "good": 0, "1": 1, "0": 0}).fillna(0).astype(int)
    else:
        df["target"] = df[target_col].astype(int)

    if target_col in df.columns:
        df = df.drop(columns=[target_col])

    for col in df.columns:
        if col != "target":
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)
            df[col] = df[col].apply(lambda v: 0.0 if v < 0 else float(v))

    ext_col = "ExternalRiskEstimate" if "ExternalRiskEstimate" in df.columns else df.columns[0]
    median_score = df[ext_col].median()
    df["risk_tier"] = df[ext_col].apply(lambda s: "Higher_Score_Tier" if s >= median_score else "Lower_Score_Tier")

    revol_col = "NetFractionRevolvingBurden" if "NetFractionRevolvingBurden" in df.columns else df.columns[1]
    
    np.random.seed(random_state)
    # Risk-correlated income generation (ExternalRiskEstimate is typically 50-90)
    base_income = 1500.0 + (df[ext_col] * 40.0)
    df["monthly_income"] = np.round(np.clip(base_income + np.random.normal(0, 500, size=len(df)), 1500.0, 15000.0), 2)
    df["disposable_income"] = np.round(df["monthly_income"] * np.random.uniform(0.2, 0.4, size=len(df)), 2)
    df["savings_balance"] = np.round(np.clip(df["monthly_income"] * np.random.uniform(0.1, 1.5, size=len(df)), 100.0, 20000.0), 2)
    
    df["duration_months"] = 36.0
    df["revolving_debt"] = np.round(df[revol_col] * 35.0, 2)

    X = df[[c for c in df.columns if c not in ["target", "risk_tier"]]]
    y = df["target"]
    A = df[["risk_tier"]]

    return train_test_split(
        X, y, A, test_size=test_size, random_state=random_state, stratify=y
    )


def load_and_preprocess_cibil(test_size: float = 0.2, random_state: int = 42):
    """Loads and prepares the External CIBIL dataset for Indian credit audits."""
    target_path = "External_Cibil_Dataset.xlsx"
    if not os.path.exists(target_path):
        raise FileNotFoundError(f"Could not find {target_path}")

    print(f"      Loaded local dataset file: {target_path}")
    df = pd.read_excel(target_path)

    # Target mapping based on P1/P2/P3/P4
    if "Approved_Flag" in df.columns:
        df["target"] = df["Approved_Flag"].apply(lambda x: 0 if str(x) in ["P1", "P2"] else 1)
        df = df.drop(columns=["Approved_Flag"])
    else:
        df["target"] = 0

    if "PROSPECTID" in df.columns:
        df = df.drop(columns=["PROSPECTID"])

    # Replace bureau sentinel missing values (-99999) with 0
    for col in df.columns:
        if df[col].dtype in [np.float64, np.int64]:
            df[col] = df[col].replace(-99999, 0.0)

    cat_cols = df.select_dtypes(include=['object']).columns
    df_cat = df[cat_cols].copy() 

    if len(cat_cols) > 0:
        df = pd.get_dummies(df, columns=cat_cols, drop_first=True)
        for c in df.columns:
            if df[c].dtype == bool:
                df[c] = df[c].astype(float)

    # Fairness group A
    if "GENDER" in df_cat.columns:
        df["gender"] = df_cat["GENDER"]
    else:
        df["gender"] = "Unknown"
    A = df[["gender"]].copy()

    # Create explicit copy of X to prevent SettingWithCopyWarning
    X = df[[c for c in df.columns if c not in ["target", "gender", "Credit_Score"]]].copy()
    y = df["target"]

    X = X.fillna(0.0)

    # Dynamic Financial Feature Augmentation
    np.random.seed(random_state)
    if "NETMONTHLYINCOME" in X.columns and (X["NETMONTHLYINCOME"] > 0).any():
        X["monthly_income"] = X["NETMONTHLYINCOME"].replace(0.0, np.nan)
        median_inc = X["monthly_income"].median()
        X["monthly_income"] = X["monthly_income"].fillna(median_inc if not np.isnan(median_inc) else 25000.0)
    else:
        if "Credit_Score" in df.columns:
            # Handle bureau scores clipped between 300 and 900
            valid_score = df["Credit_Score"].replace(0.0, 600.0).clip(lower=300.0, upper=900.0)
            base_income = 12000.0 + (valid_score * 50.0) # INR scaling
        else:
            base_income = 35000.0 * np.ones(len(X))
        
        income_noise = np.random.normal(0, 3000, size=len(X))
        X["monthly_income"] = np.round(np.clip(base_income + income_noise, 10000.0, 200000.0), 2)

    X["disposable_income"] = np.round(X["monthly_income"] * np.random.uniform(0.20, 0.40, size=len(X)), 2)
    X["savings_balance"] = np.round(np.clip(X["monthly_income"] * np.random.uniform(0.10, 1.50, size=len(X)), 1000.0, 500000.0), 2)
    X["duration_months"] = 36.0

    if "CC_utilization" in X.columns:
        X["revolving_debt"] = np.round(X["CC_utilization"] * 100.0, 2)
    else:
        X["revolving_debt"] = 5000.0

    return train_test_split(
        X, y, A, test_size=test_size, random_state=random_state, stratify=y
    )