import shlex
def handle_echo(message):
    try:
        splitm = shlex.split(message)
    except ValueError as e:
        print(f"Error: {e}")
        return
    cleaned_message = []
    for part in splitm:
        if (part.startswith("'") and part.endswith("'")) or (part.startswith("\"") and part.endswith("\"")):
            cleaned_message.append(part[1:-1])
        else:
            cleaned_message.append(part)
    print(" ".join(cleaned_message))