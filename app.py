import streamlit as st
import google.generativeai as genai

# Streamlit UI
st.title("AI-Powered Financial Assistant")

# Ask for Google Gemini API key input
api_key_input = st.text_input("Enter your Google Gemini API Key:", type="password")
if api_key_input:
    genai.configure(api_key=api_key_input)

    # Helper function to interact with Gemini's model
    def get_ai_response(prompt):
        model = genai.GenerativeModel('gemini-1.5-pro-latest')
        response = model.generate_content(prompt)
        return response.text

    # Define the financial areas
    areas = ["Personal Finance", "Investing", "Retirement Planning", "Tax Planning", "Wealth Management", "Entrepreneurship & Business Finance"]

    st.sidebar.title("Select a Financial Area")
    selected_area = st.sidebar.selectbox("Choose a category:", areas)

    if selected_area == "Personal Finance":
        st.header("Personal Finance Advisor")
        st.subheader("Get personalized advice on budgeting, saving, and managing debt.")

        # Inputs for Personal Finance
        income = st.number_input("Enter your monthly income:", min_value=0.0, step=100.0)
        expenses = st.number_input("Enter your monthly expenses:", min_value=0.0, step=100.0)
        debt = st.number_input("Enter your current debt amount:", min_value=0.0, step=100.0)
        goal = st.text_input("What are your financial goals? (e.g., Save for a house, pay off debt, etc.)")

        if st.button("Get Advice"):
            prompt = f"My monthly income is ${income}, expenses are ${expenses}, and my debt is ${debt}. My financial goal is {goal}. Give me a detailed personal finance plan."
            advice = get_ai_response(prompt)
            st.write(advice)

    elif selected_area == "Investing":
        st.header("Investment Advice")
        st.subheader("Get insights on stock market, risk management, and diversification.")

        # Inputs for Investing
        investment_amount = st.number_input("Enter amount available for investment:", min_value=0.0, step=100.0)
        risk_level = st.selectbox("Select your risk tolerance:", ["Low", "Medium", "High"])
        strategy = st.text_input("Describe your investment strategy or goals (e.g., long-term growth, dividend income):")

        if st.button("Get Investment Advice"):
            prompt = f"I have ${investment_amount} to invest. My risk tolerance is {risk_level}. My strategy is {strategy}. Give me a detailed investment plan."
            advice = get_ai_response(prompt)
            st.write(advice)

    elif selected_area == "Retirement Planning":
        st.header("Retirement Planning")
        st.subheader("Get advice on saving for retirement, tax-efficient withdrawals, and more.")

        # Inputs for Retirement Planning
        current_savings = st.number_input("Enter your current retirement savings:", min_value=0.0, step=100.0)
        age = st.number_input("Enter your age:", min_value=18, max_value=100, step=1)
        retirement_age = st.number_input("Desired retirement age:", min_value=50, max_value=80, step=1)

        if st.button("Get Retirement Plan"):
            prompt = f"I am {age} years old with ${current_savings} saved for retirement. I want to retire at {retirement_age}. Provide a retirement savings and investment plan."
            advice = get_ai_response(prompt)
            st.write(advice)

    elif selected_area == "Tax Planning":
        st.header("Tax Planning")
        st.subheader("Optimize your taxes with AI guidance.")

        # Inputs for Tax Planning
        income = st.number_input("Enter your annual income:", min_value=0.0, step=1000.0)
        tax_filing_status = st.selectbox("Choose your filing status:", ["Single", "Married", "Head of Household"])
        deductions = st.text_input("List any potential deductions or tax credits:")

        if st.button("Get Tax Advice"):
            prompt = f"My annual income is ${income}, filing status is {tax_filing_status}, and my deductions are {deductions}. Provide me with a tax optimization strategy."
            advice = get_ai_response(prompt)
            st.write(advice)

    elif selected_area == "Wealth Management":
        st.header("Wealth Management")
        st.subheader("Manage your wealth with estate planning and investment strategies.")

        # Inputs for Wealth Management
        net_worth = st.number_input("Enter your total net worth:", min_value=0.0, step=10000.0)
        assets = st.text_input("List your assets (e.g., properties, stocks, etc.):")
        goals = st.text_input("What are your wealth management goals? (e.g., preserving wealth, estate planning)")

        if st.button("Get Wealth Management Advice"):
            prompt = f"My net worth is ${net_worth}, I have the following assets: {assets}, and my goals are {goals}. Provide a detailed wealth management plan."
            advice = get_ai_response(prompt)
            st.write(advice)

    elif selected_area == "Entrepreneurship & Business Finance":
        st.header("Business Finance")
        st.subheader("Get advice on managing cash flow, business loans, and more.")

        # Inputs for Business Finance
        business_type = st.text_input("Describe your business:")
        revenue = st.number_input("Enter your annual revenue:", min_value=0.0, step=10000.0)
        expenses = st.number_input("Enter your annual expenses:", min_value=0.0, step=10000.0)

        if st.button("Get Business Finance Advice"):
            prompt = f"I run a {business_type} business with ${revenue} in revenue and ${expenses} in expenses. Provide financial advice for optimizing cash flow and business growth."
            advice = get_ai_response(prompt)
            st.write(advice)

else:
    st.warning("Please enter your Google Gemini API key to proceed.")
