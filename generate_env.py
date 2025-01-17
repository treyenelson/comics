"""Generate a bash script that sets up environment variables if it doesn't already exist."""
import random


def get_random_string(length, allowed_chars):
    return ''.join(random.choice(allowed_chars) for _ in range(length))


def main():
    filepath = 'project.env'
    try:
        open(filepath, 'r')
        print(f"Environment file `{filepath}` already found. Skipping file generation.")
    except FileNotFoundError:
        response = ""
        while response not in ("y", "n"):
            response = input("Is this a dev environment (enable debug mode)? (y/N) ").strip().lower()
            if response == "":
                response = "n"
        if response == "y":
            debug_string = "DJANGO_DEBUG=1"
        else:
            debug_string = "DJANGO_DEBUG=0"

        domain = input("Domain (default: localhost): ").strip()
        if domain == "":
            domain = "localhost"

        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        with open(filepath, 'w') as outfile:
            outfile.write(f'''
DJANGO_PROJECT_DIR=comics
DJANGO_SECRET={get_random_string(50, chars)}
{debug_string}
SITE_DOMAIN={domain}
''')
        print("Created environment file successfully.")


if __name__ == "__main__":
    main()
