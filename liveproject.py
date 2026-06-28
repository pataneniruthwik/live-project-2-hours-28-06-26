#task 1: loading and reading of datasets
import pandas as pd

df = pd.read_csv("bangalore_tech_salaries (2).csv")
print(df.head())
print(df.shape) #data set shape
print(df.columns) #column names
print(df.dtypes)# data types
print(df.info()) #Dataset information
print(df.isnull().sum()) #Missing values
print(df.duplicated().sum()) #Duplicate rows
print(df.describe()) #statistical summary
#task 2: #cleaning of data starts to standardize 
print(df["Role "].unique()) # checking all unique job roles with different names 
role_dict = {
        "DS": "Data Scientist",
    "Data Scientist": "Data Scientist",
    "Data Science Engineer": "Data Scientist",

    "DA": "Data Analyst",
    "Data Analyst": "Data Analyst",
    "BI Analyst": "Data Analyst",

    "BA": "Business Analyst",
    "Business Analyst": "Business Analyst",
    "Business Systems Analyst": "Business Analyst",

    "DevOps": "DevOps Engineer",
    "DevOps Engineer": "DevOps Engineer",

    "SDE Backend": "SDE Backend",
    "SDE-Backend": "SDE Backend",
    "Backend Dev": "SDE Backend",
    "Backend Developer": "SDE Backend",
    "Backend Engineer": "SDE Backend",
    "BE": "SDE Backend",

    "SDE Frontend": "SDE Frontend",
    "SDE-Frontend": "SDE Frontend",
    "Frontend Dev": "SDE Frontend",
    "Frontend Developer": "SDE Frontend",
    "Frontend Engineer": "SDE Frontend",
    "FE": "SDE Frontend",

    "Full Stack Engineer": "Full Stack Engineer",
    "Fullstack": "Full Stack Engineer",
    "Fullstack Dev": "Full Stack Engineer",
    "SDE Full-Stack": "Full Stack Engineer",
    "SDE FS": "Full Stack Engineer",
    "FullStack": "Full Stack Engineer",

    "UI/UX": "UI/UX ",
    "UI Designer": "UI/UX ",
    "UX Designer": "UI/UX ",
    "Designer": "UI/UX ",

    "Product Lead": "Product Manager",
    "Product Manager": "Product Manager",
    "PM": "Product Manager",
    "Sr PM": "Product Manager",

    "Product Designer": "Product Designer",

    "Site Reliability Engineer": "Site Reliability Engineer",
    "SRE": "Site Reliability Engineer",

    "Infra Engineer": "Infra Engineer",

    "ML Engineer": "ML Engineer",

    "Analytics Engineer": "Analytics Engineer"
}
# now we are  Replacing different role names into one standard role names.
df["Role "] = df["Role "].replace(role_dict)
# Checking if the role names were standardized successfully.
print(df["Role "].value_counts())
print(df["Current_CTC"].head(20))
print(df["Previous_CTC"].head(20))
print(df["Current_CTC"].unique()) #checking all unique formats of current ctc
print(df["Previous_CTC"].unique()) # chceking all unique formats of previous ctc
# Removing "LPA" from the salary values.
df["Current_CTC"] = df["Current_CTC"].str.replace(" LPA", "", regex=False)
df["Previous_CTC"] = df["Previous_CTC"].str.replace(" LPA", "", regex=False)

# Removing the rupee symbol from the salary values.
df["Current_CTC"] = df["Current_CTC"].str.replace("₹", "", regex=False)
df["Previous_CTC"] = df["Previous_CTC"].str.replace("₹", "", regex=False)

# Removing commas from the salary values.
df["Current_CTC"] = df["Current_CTC"].str.replace(",", "", regex=False)
df["Previous_CTC"] = df["Previous_CTC"].str.replace(",", "", regex=False)

# Displaying the cleaned salary values.
print(df["Current_CTC"].head(20))
print(df["Previous_CTC"].head(20))
# Converting the salary columns from string to numeric values.
df["Current_CTC"] = pd.to_numeric(df["Current_CTC"], errors="coerce")
df["Previous_CTC"] = pd.to_numeric(df["Previous_CTC"], errors="coerce")

print(df["Current_CTC"].dtype)
print(df["Previous_CTC"].dtype)
df["Current_CTC"] = df["Current_CTC"].apply(lambda x: x / 100000 if x > 1000 else x)

df["Previous_CTC"] = df["Previous_CTC"].apply(lambda x: x / 100000 if x > 1000 else x)
# Checking the salary values after converting them into LPA.
print(df["Current_CTC"].head(20))
print(df["Previous_CTC"].head(20))

print(df["company_TYPE"].unique()) # Checking all unique company types before standardizing them.

company_dict = {
    "Unicorn": "Unicorn",
    "unicorn": "Unicorn",
    "UNICORN": "Unicorn",

    "MNC": "MNC",
    "mnc": "MNC",

    "Mid-size": "Mid-size",
    "mid-size": "Mid-size",
    "MID-SIZE": "Mid-size",

    "Early-stage": "Early-stage",
    "early-stage": "Early-stage",
    "EARLY-STAGE": "Early-stage"
}

# Replacing different company type names with standardized names.
df["company_TYPE"] = df["company_TYPE"].replace(company_dict)
# Checking company types after standardization.
print(df["company_TYPE"].value_counts())

print(df["Education_Tier"].unique()) # checking different education tier names before standardization
education_dict = {
    "Tier-1": "Tier-1",
    "Tier 1": "Tier-1",
    "T1": "Tier-1",
    "1": "Tier-1",

    "Tier-2": "Tier-2",
    "Tier 2": "Tier-2",
    "T2": "Tier-2",
    "2": "Tier-2",

    "Tier-3": "Tier-3",
    "Tier 3": "Tier-3",
    "T3": "Tier-3",
    "3": "Tier-3"
}
# Replacing different education tier values with standardized names.
df["Education_Tier"] = df["Education_Tier"].replace(education_dict)
# verifying education tier values after standardization.
print(df["Education_Tier"].value_counts())

print(df.isnull().sum()) # Checking missing values after cleaning the dataset.




# Filling missing values in Skills and Location.
#  we are Keeping Previous_CTC as it is mentioned in pdf that missing values belong to freshers.
df["Skills"] = df["Skills"].fillna("Not Available")
df["Location"] = df["Location"].fillna("Not Available")

#now checking null values again
# Checking the missing values after cleaning.
print(df.isnull().sum())

df = df.drop_duplicates() # removing duplicates from data set
# Checking duplicate rows after removing duplicates
print(df.duplicated().sum())

#now we are printing the correct cleaned data set
print(df.dtypes)

print("\nRole:")
print(df["Role "].value_counts())

print("\nCompany Type:")
print(df["company_TYPE"].value_counts())

print("\nEducation Tier:")
print(df["Education_Tier"].value_counts())



# TASK 3 : Answering business questions using the cleaned dataset.
# The aim of this task is to analyze the salary data and find useful insights from it.
# AI Assisted: Used ChatGPT to understand some pandas syntax and logic while implementing the solutions.

# Finding the median CTC for each role.
median_ctc = df.groupby("Role ")["Current_CTC"].median()
print(median_ctc.sort_values(ascending=False))
# Finding the mean CTC for each role.
mean_ctc = df.groupby("Role ")["Current_CTC"].mean()
print(mean_ctc.sort_values(ascending=False))
# Finding the minimum CTC for each role.
min_ctc = df.groupby("Role ")["Current_CTC"].min()
print(min_ctc.sort_values(ascending=False))
# Finding the maximum CTC for each role.
max_ctc = df.groupby("Role ")["Current_CTC"].max()
print(max_ctc.sort_values(ascending=False))

#Q3.1 :  Product Manager has the highest median CTC (31.30 LPA), while Data Analyst has the lowest median CTC (16.30 LPA). The mean salary is higher than the median for some roles, showing that a few high salaries increase the average.

#Q3.2: The median salary of SDE Backend professionals increases with experience. The highest median CTC is 40.40 LPA for professionals with 6+ years of experience, showing a steady salary growth as experience increases.

# Creating experience groups.
sde_backend = df[df["Role "] == "SDE Backend"]
sde_backend["Experience_Band"] = pd.cut(
    sde_backend["years_exp"],
    bins=[-1, 1, 3, 5, 100],
    labels=["0-1 Years", "2-3 Years", "4-5 Years", "6+ Years"]
)
median_exp = sde_backend.groupby("Experience_Band")["Current_CTC"].median()

print(median_exp)

# Calculating the salary growth between experience groups.
growth_1 = ((20.00 - 11.65) / 11.65) * 100
growth_2 = ((25.85 - 20.00) / 20.00) * 100
growth_3 = ((40.40 - 25.85) / 25.85) * 100

print("0-1 to 2-3 Years :", round(growth_1, 2), "%")
print("2-3 to 4-5 Years :", round(growth_2, 2), "%")
print("4-5 to 6+ Years :", round(growth_3, 2), "%")

#Q3.3:

sde = df[
    (df["Role "] == "SDE Backend") |
    (df["Role "] == "SDE Frontend") |
    (df["Role "] == "Full Stack Engineer")
]

with_aws = sde[sde["Skills"].str.contains("AWS", case=False, na=False)]

without_aws = sde[~sde["Skills"].str.contains("AWS", case=False, na=False)]

print("Median CTC with AWS :", with_aws["Current_CTC"].median())

print("Median CTC without AWS :", without_aws["Current_CTC"].median())


#Q3.3:among the selected skills, professionals with Kubernetes have a median CTC of 23.20 LPA, while those without Kubernetes have a median CTC of 21.50 LPA, giving a salary premium of 7.91%.
# Selecting SDE Backend, SDE Frontend and Full Stack Engineer roles.
sde = df[
    (df["Role "] == "SDE Backend") |
    (df["Role "] == "SDE Frontend") |
    (df["Role "] == "Full Stack Engineer")
]

# List of skills to compare.
skills = ["AWS", "ML", "System Design", "Kubernetes"]

# Checking the median salary with and without each skill.
for skill in skills:

    with_skill = sde[sde["Skills"].str.contains(skill, case=False, na=False)]

    without_skill = sde[~sde["Skills"].str.contains(skill, case=False, na=False)]

    median_with = with_skill["Current_CTC"].median()
    median_without = without_skill["Current_CTC"].median()

    premium = ((median_with - median_without) / median_without) * 100

    print("\nSkill :", skill)
    print("Median CTC with skill :", round(median_with,2))
    print("Median CTC without skill :", round(median_without,2))
    print("Skill Premium :", round(premium,2), "%")

    #Q3.4: For SDE Backend professionals, Unicorn companies offer the highest median CTC of 27.35 LPA, while Early-stage companies offer the lowest median CTC of 18.60 LPA. Unicorn companies provide a 33.74% higher median salary than MNCs for the same role.
    
backend = df[df["Role "] == "SDE Backend"]

# Finding the median salary for each company type.
company_ctc = backend.groupby("company_TYPE")["Current_CTC"].median()

print(company_ctc)
# Calculating the percentage premium of Unicorn over MNC.
unicorn = company_ctc["Unicorn"]
mnc = company_ctc["MNC"]

premium = ((unicorn - mnc) / mnc) * 100

print("Unicorn Premium over MNC :", round(premium,2), "%")
#Q3.5: Finding the most underpaid professionals by comparing  each employee's salary with the median salary of similar employees.
# Creating experience groups.

df["Experience_Band"] = pd.cut(
    df["years_exp"],
    bins=[-1,1,3,5,100],
    labels=["0-1 Years","2-3 Years","4-5 Years","6+ Years"]
)

# Finding the number of employees in each group.

group_size = df.groupby(
    ["Role ","company_TYPE","Experience_Band"]
)["Current_CTC"].transform("count")

df = df[group_size >= 10]
# Finding the median salary for each group.

df["Group_Median"] = df.groupby(
    ["Role ","company_TYPE","Experience_Band"]
)["Current_CTC"].transform("median")
# Calculating the salary gap.

df["Gap"] = df["Current_CTC"] - df["Group_Median"]
# Sorting employees by salary gap.

underpaid = df.sort_values("Gap").head(5)

print(
    underpaid[
        [
            "Employee_ID",
            "Role ",
            "company_TYPE",
            "years_exp",
            "Current_CTC",
            "Group_Median",
            "Gap"
        ]
    ]
)

#3.5 FINAL INSIGHT : The employees listed above earn the lowest salaries compared to the median salary of professionals with the same role, company type, and experience group. These professionals have the highest negative salary gap in the dataset.



## task 4:
# Printing the final report.



print("=" * 70)
print("                 BANGALORE TECH SALARY DECODER")
print("Built by: Pataneni Ruthwik | The Unlox Academy | 2-Hour Live Project")
print("=" * 70)

print("\nDataset : 1,000 Bengaluru Tech Professionals (Synthetic)")
print("Period  : 2024 Employment Snapshot")

# =========================================================

print("\n----- MEDIAN CTC BY ROLE (in LPA) -----")

for role, value in median_ctc.sort_values(ascending=False).items():
    print(f"{role:<30}{value:.2f} LPA")

# =========================================================

print("\n----- SDE BACKEND CTC BY EXPERIENCE BAND -----")

print(f"0-1 Years : {median_exp['0-1 Years']:.2f} LPA median")
print(f"2-3 Years : {median_exp['2-3 Years']:.2f} LPA median (+71.67% growth)")
print(f"4-5 Years : {median_exp['4-5 Years']:.2f} LPA median (+29.25% growth)")
print(f"6+ Years  : {median_exp['6+ Years']:.2f} LPA median (+56.29% growth)")

# =========================================================

print("\n----- SKILL PREMIUM FOR SDEs (Median CTC) -----")

print(f"{'Skill':<18}{'With Skill':<15}{'Without':<15}{'Premium'}")

skills = ["AWS", "ML", "System Design", "Kubernetes"]

for skill in skills:

    with_skill = sde[sde["Skills"].str.contains(skill, case=False, na=False)]

    without_skill = sde[
        ~sde["Skills"].str.contains(skill, case=False, na=False)
    ]

    with_median = with_skill["Current_CTC"].median()

    without_median = without_skill["Current_CTC"].median()

    skill_premium = ((with_median - without_median) / without_median) * 100

    print(
        f"{skill:<18}"
        f"{with_median:<15.2f}"
        f"{without_median:<15.2f}"
        f"{skill_premium:.2f}%"
    )

# =========================================================

print("\n----- COMPANY TYPE PREMIUM (SDE Backend) -----")

for company, value in company_ctc.items():
    print(f"{company:<15}{value:.2f} LPA")

print(f"\nUnicorn Premium over MNC : {premium:.2f}%")

# =========================================================

print("\n----- TOP 5 MOST UNDERPAID PROFESSIONALS -----")

print(f"{'ID':<10}{'Role ':<25}{'Company':<15}{'Exp':<10}{'Gap'}")

for _, row in underpaid.iterrows():

    print(
        f"{row['Employee_ID']:<10}"
        f"{row['Role ']:<25}"
        f"{row['company_TYPE']:<15}"
        f"{str(row['years_exp']) + ' yrs':<10}"
        f"{row['Gap']:.2f} LPA"
    )

print("\n" + "=" * 70)

#task 5:  KEY INSIGHTS

#1. Product Manager has the highest median CTC of 31.30 LPA, while Data Analyst has the lowest median CTC of 16.30 LPA. Students aiming for higher salaries can consider product management roles.

#2. The median CTC of SDE Backend professionals increases from 11.65 LPA (0–1 years) to 40.40 LPA (6+ years), showing strong salary growth with experience.

#3. Unicorn companies offer a median CTC of 27.35 LPA for SDE Backend professionals, which is 33.74% higher than MNCs. Students targeting higher salaries can focus on Unicorn companies.
#Task 6 AI Disclosure
# AI-assisted: Used ChatGPT to understand pandas syntax,
# debug Python code, and understand the data cleaning
# and analysis logic used in this project.


# AI-assisted: Used ChatGPT for understanding some pandas syntax,
# debugging a few issues, and clarifying concepts during the project.
# Most of the implementation and testing were done by me.
#only for senetence formation on insights after caluculating i took help of ai to get sentences for insights with accurate grammar and forming which i already know but due to less time to do the project i used for insight sentence formation at task 3
