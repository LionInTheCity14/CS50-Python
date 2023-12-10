def main():
    value = str(input("What's your name ? ")).title()
    hello()
    hello(value)

def hello(name="World"): 
    print(f"Hello, {name}")


main()