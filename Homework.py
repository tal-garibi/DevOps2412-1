import requests

def check_github_repositories(username):
    api_ur1 = f'https://api.github.com/users/{username}/repos'

    try:
        response = requests.get(api_ur1)

        if response.status_code == 200:
            repositories = response.json()

            if len(repositories) >= 5:
                print(f"{username} has at least 5 repositories.")
            else:
                print(f"{username} does not have enough repositories (less than 5).")

            else:
            print(f"Failed to retrieve repositories. Status code: {response.status_code}")

        except Exception as e:
        print(f"An error occurred: {e}")


# Replace 'avielb' with the GitHub username you want to check
check_github_repositories('avielb')