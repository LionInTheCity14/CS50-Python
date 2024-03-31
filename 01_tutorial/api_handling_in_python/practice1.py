import requests

def get_data(url):
    response = requests.get(url)
    response_data = response.json()
    if response.status_code == 200 and response_data['data']:
        products = response_data['data']['data']
        return products
    else:
        raise Exception()

def main():
    url = 'https://api.freeapi.app/api/v1/public/randomproducts'
    try:
        products = get_data(url)
        for product in products:
            print(f"product: {product['title']}, price: {product['price']}")
    except Exception as e:
        print(f'"INSIDE MAIN()" -> Error: {str(e)}')
    finally:
        print('finished')

if __name__ == '__main__':
    main()
