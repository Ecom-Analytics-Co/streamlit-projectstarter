import os

def create_file(file_name, content):
    with open(file_name, 'w', encoding='utf-8') as file: # Specifying UTF-8 encoding
        file.write(content)

def main():
    # the missing indentation is intentional in this multi-line string
    env_example_content = """# If you add or remove a key in .env, make sure to make the change here as well
# ⚠️ Do not save any secret values in this file ⚠️
EXAMPLE_API_KEY=
"""

    # the missing indentation is intentional in this multi-line string
    env_content = """# 🔁 If you add or remove a key to .env, make sure to make the change in .env.example as well
EXAMPLE_API_KEY=your-api-key-goes-here
"""

    create_file('.env.example', env_example_content)
    create_file('.env', env_content)
    print('Files created successfully!')

if __name__ == "__main__":
    main()
