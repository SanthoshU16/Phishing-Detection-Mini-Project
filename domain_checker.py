suspicious = input("Enter website: ").lower()

trusted_domains = ["google.com","chatgpt.com", "facebook.com", "amazon.com"]

def normalize(domain):
    return domain.replace("0", "o").replace("1", "l")

found_exact = False
found_similar = False

for trusted in trusted_domains:
    if suspicious == trusted:
        found_exact = True
    elif normalize(suspicious) == normalize(trusted):
        found_similar = True

if found_exact:
    print("Domain is safe")
elif found_similar:
    print("Suspicious domain")
else:
    print("Unknown domain")
