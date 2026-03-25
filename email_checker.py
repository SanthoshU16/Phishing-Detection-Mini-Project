email_text = input("Enter the email content: ").lower()

risky_words = ["urgent", "verify", "password", "bank", "click"]

if any(word in email_text for word in risky_words):
    print("Warning: This email may be risky")
else:
    print("This email looks safe")
