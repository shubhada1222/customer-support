import streamlit as st

from graph import graph


# Page Title
st.title("AI Customer Support Assistant")


# Description
st.write(
    "Describe your issue below and "
    "our AI assistant will help you."
)


# User Input
user_query = st.text_area(
    "Enter your issue"
)


# Submit Button
if st.button("Submit"):


    # Empty Input Check
    if user_query.strip() == "":

        st.warning("Please enter your issue.")


    else:

        # Run LangGraph Workflow
        result = graph.invoke({

            "user_query": user_query

        })


        # Display Results
        st.subheader("Issue Type")

        st.success(result["issue_type"])


        st.subheader("Support Response")

        st.info(result["response"])