import streamlit as st

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


if __name__ == "__main__":
    investment_calculator()
