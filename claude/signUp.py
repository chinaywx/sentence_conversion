def generate_emails():
    emails = []

    for i in range(1, 101):
        email = f"chinaywx123{i}@2925.com"
        emails.append(email)

    return emails


if __name__ == "__main__":
    email_list = generate_emails()
    for email in email_list:
        print(email)
