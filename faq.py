"""
=========================================================
AlgoPipX Educational Assistant
FAQ Manager
=========================================================
"""

from database import (
    add_faq,
    get_faqs,
    get_faq,
    delete_faq
)


# -------------------------------------------------------
# Get All FAQs
# -------------------------------------------------------

def load_faqs():

    return get_faqs()



# -------------------------------------------------------
# Add FAQ
# -------------------------------------------------------

def create_faq(question, answer):

    if not question or not answer:
        return False


    add_faq(
        question.strip(),
        answer.strip()
    )

    return True



# -------------------------------------------------------
# Delete FAQ
# -------------------------------------------------------

def remove_faq(faq_id):

    try:

        delete_faq(
            int(faq_id)
        )

        return True

    except Exception:

        return False



# -------------------------------------------------------
# Get Single FAQ
# -------------------------------------------------------

def fetch_faq(faq_id):

    return get_faq(
        int(faq_id)
    )



# -------------------------------------------------------
# Format FAQ Response
# -------------------------------------------------------

def format_faq(question, answer):

    return (

        f"❓ {question}\n\n"

        f"{answer}"

    )



# -------------------------------------------------------
# Default FAQs
# -------------------------------------------------------

DEFAULT_FAQS = [

    {
        "question":
        "What is algorithmic trading?",

        "answer":
        (
            "Algorithmic trading uses computer programs "
            "to analyse information and execute predefined "
            "rules based on a strategy."
        )
    },


    {
        "question":
        "Is this financial advice?",

        "answer":
        (
            "No. All content provided by this assistant "
            "is for educational purposes only and should "
            "not be considered financial or investment advice."
        )
    },


    {
        "question":
        "What topics are covered?",

        "answer":
        (
            "Topics include market analysis, trading "
            "automation concepts, risk management, and "
            "strategy development."
        )
    },


    {
        "question":
        "How can I contact support?",

        "answer":
        (
            "You can contact support using the Contact "
            "Support button in the main menu."
        )
    }

]



# -------------------------------------------------------
# Insert Default FAQs
# -------------------------------------------------------

def setup_default_faqs():

    existing = load_faqs()


    if len(existing) == 0:

        for item in DEFAULT_FAQS:

            create_faq(
                item["question"],
                item["answer"]
            )
