from extract import run_extract
from transform import run_transform
from load import run_load

def main():
    print("===Extract===")
    run_extract()

    print("===Transform===")
    run_transform()

    print("===Load===")
    run_load()

if __name__ == "__main__":
    main()