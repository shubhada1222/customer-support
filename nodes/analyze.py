def analyze_issue(state):

    query = state["user_query"]


    if "refund" in query.lower():

        issue = "Refund Issue"


    elif "payment" in query.lower():

        issue = "Payment Issue"


    elif (
        "password" in query.lower()
        or "login" in query.lower()
        or "signin" in query.lower()
    ):

        issue = "Login Issue"


    elif "order" in query.lower():

        issue = "Order Issue"


    else:

        issue = "General Support"


    return {
        "issue_type": issue
    }