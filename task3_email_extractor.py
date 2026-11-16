import re

INPUT_FILE = "input.txt"
OUTPUT_FILE = "emails.txt"
PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"


def main():
    try:
        with open(INPUT_FILE, "r") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Create a file called {INPUT_FILE} with some text in it first.")
        return

    emails = sorted(set(re.findall(PATTERN, text)))

    with open(OUTPUT_FILE, "w") as f:
        f.write("\n".join(emails))

    print(f"Found {len(emails)} email(s). Saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()