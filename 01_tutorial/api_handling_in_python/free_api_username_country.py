import requests


def fetch_random_user_freeapi(url):
    response = requests.get(url)
    data = response.json()

    if data['success'] and 'data' in data:
        user_data = data['data']
        username = user_data['login']['username']
        country = user_data['location']['country']
        return [username, country]
    else:
        raise Exception('Failed to fetch user data')

    

def main():
    url = 'https://api.freeapi.app/api/v1/public/randomusers/user/random'
    try:
       [username, country] = fetch_random_user_freeapi(url)
       print(f"Username: {username} \n Country: {country}")
    except Exception as e:
        print(str(e))
    finally:
        print('finished')

if __name__ == '__main__':
    main()