def generate_response(state):

    issue = state["issue_type"]


    if issue == "Refund Issue":

        response = (
            "Your refund request has been forwarded "
            "to our billing department."
        )


    elif issue == "Payment Issue":

        response = (
            "Please verify your payment details "
            "and try again."
        )


    elif issue == "Login Issue":

        response = (
            "Please use the 'Forgot Password' "
            "option to reset your password."
        )


    elif issue == "Order Issue":

        response = (
            "Our order support team is checking "
            "your delivery status."
        )


    else:

        response = (
            "Our support team will contact you shortly."
        )


    return {
        "response": response
    }