import os

def create_user(username):
    try:
        os.system(f'sudo adduser {username}')
        print(f"User {username} created successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    user = input("Enter the username to create: ")
    create_user(user)
