import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def investment_calculator():
    """
    This function creates a Streamlit app to gather user input for investment planning with scoring.
    """
    # Title
    st.title("Investment Planning Assistant")

    # Income score
    income_options = {
        "Less than 5 lakhs": 1,
        "5-10 lakhs": 2,
        "10-20": 3,
        "20-30": 4,
        "30-40": 5,
        "40 above": 6,
    }
    income = st.selectbox("What is your annual income (USD)?", list(income_options.keys()))
    income_score = income_options[income]

    # Age score
    age_options = {
        "20-30": 6,
        "30-40": 4,
        "40-50": 2,
        "50 above": 1,
    }
    age = st.selectbox("What is your current age?", list(age_options.keys()))
    age_score = age_options[age]

    # Investment percentage score
    investment_percentage_options = {
        "5-10": 1,
        "10-15": 2,
        "15-20": 3,
        "20-25": 4,
        "25-30": 5,
        "30 above": 6,
    }
    investment_percentage = st.selectbox("What percentage of your income do you want to invest?", list(investment_percentage_options.keys()))
    investment_percentage_score = investment_percentage_options[investment_percentage]

    # Investment goals score
    investment_goals_options = {
        "Retirement planning": 4.5,
        "Major purchase": 5.5,
        "Child's education": 6,
        "Building wealth": 4,
        "Generating income": 5,
    }
    investment_goals = st.selectbox("What are your investment goals?", list(investment_goals_options.keys()))
    investment_goals_score = investment_goals_options[investment_goals]

    # Timeframe score (dummy values for now, replace with actual scores based on your strategy)
    timeframe_options = ["LT", "MT", "HT"]
    timeframe = st.selectbox("What is your investment timeframe?", timeframe_options)
    timeframe_score = 3  # Placeholder score for timeframe

    # Risk tolerance score
    risk_tolerance_options = {
        "No tolerance for losses": 1,
        "Minimize losses": 3,
        "Moderate fluctuations": 5,
        "Significant fluctuations": 6,
    }
    risk_tolerance = st.selectbox("What is your risk tolerance?", list(risk_tolerance_options.keys()))
    risk_tolerance_score = risk_tolerance_options[risk_tolerance]

    # Debt score
    debt_options = {
        "Nil": 6,
        "More": 2,
        "Some": 4,
    }
    debts = st.selectbox("Do you have any outstanding debts (USD)?", list(debt_options.keys()))
    debt_score = debt_options[debts]

    # Emergency fund score
    emergency_fund_options = {
        "Nil": 6,
        "Medium": 3,
        "More": 0,
    }
    emergency_fund = st.selectbox("Do you have an emergency fund (USD)?", list(emergency_fund_options.keys()))
    emergency_fund_score = emergency_fund_options[emergency_fund]

    # Job security score
    job_security_options = {
        "Secure": 6,
        "Mildly secure": 3,
        "Insecure": 0,
    }
    job_security = st.selectbox("How secure is your current job?", list(job_security_options.keys()))
    job_security_score = job_security_options[job_security]

    # Total score calculation
    total_score = (
        income_score + age_score + investment_percentage_score +
        investment_goals_score + timeframe_score + risk_tolerance_score +
        debt_score + emergency_fund_score + job_security_score
    )

    if st.button("Calculate Score"):
        st.write("Your total investment score is:", total_score)

    # Plot distribution of investment scores among different categories
    st.header("Distribution of Investment Scores")

    # Create a DataFrame for the scores
    scores_df = pd.DataFrame({
        "Category": ["Income", "Age", "Investment Percentage", "Investment Goals", "Risk Tolerance", "Debt", "Emergency Fund", "Job Security"],
        "Score": [income_score, age_score, investment_percentage_score, investment_goals_score, risk_tolerance_score, debt_score, emergency_fund_score, job_security_score]
    })

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(scores_df["Category"], scores_df["Score"])
    ax.set_ylabel("Score")
    ax.set_title("Distribution of Investment Scores")
    st.pyplot(fig)

    # Pie chart for investment goals
    st.header("Investment Goals Distribution")

    # Calculate the proportion of investment goals
    investment_goals_counts = pd.Series([1]*len(investment_goals_options), index=list(investment_goals_options.keys()))
    investment_goals_counts[investment_goals] += 1
    fig, ax = plt.subplots()
    ax.pie(investment_goals_counts, labels=investment_goals_counts.index, autopct='%1.1f%%')
    ax.set_title("Proportion of Investment Goals")
    st.pyplot(fig)

    # Line chart for trend of investment scores over time
    st.header("Trend of Investment Scores Over Time")

    # Dummy data for trend
    time_periods = ["Q1", "Q2", "Q3", "Q4"]
    income_scores = np.random.randint(1, 7, size=len(time_periods))
    age_scores = np.random.randint(1, 7, size=len(time_periods))
    investment_percentage_scores = np.random.randint(1, 7, size=len(time_periods))
    investment_goals_scores = np.random.randint(1, 7, size=len(time_periods))
    risk_tolerance_scores = np.random.randint(1, 7, size=len(time_periods))
    debt_scores = np.random.randint(1, 7, size=len(time_periods))
    emergency_fund_scores = np.random.randint(1, 7, size=len(time_periods))
    job_security_scores = np.random.randint(1, 7, size=len(time_periods))

    trend_df = pd.DataFrame({
        "Time Period": time_periods,
        "Income": income_scores,
        "Age": age_scores,
        "Investment Percentage": investment_percentage_scores,
        "Investment Goals": investment_goals_scores,
        "Risk Tolerance": risk_tolerance_scores,
        "Debt": debt_scores,
        "Emergency Fund": emergency_fund_scores,
        "Job Security": job_security_scores
    })

    # Plot the line chart
    fig, ax = plt.subplots()
    for column in trend_df.columns[1:]:
        ax.plot(trend_df["Time Period"], trend_df[column], label=column)
    ax.set_xlabel("Time Period")
    ax.set_ylabel("Score")
    ax.set_title("Trend of Investment Scores Over Time")
    ax.legend()
    st.pyplot(fig)

if __name__ == "__main__":
    investment_calculator()

