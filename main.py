from extract import run_extract
from transform import run_transform
from load import run_load

def main():
    print("===Extract===")
    if not run_extract():
        print("Пайплайн остановлен: нет данных")
        return

    print("===Transform===")
    run_transform()

    print("===Load===")
    run_load()

if __name__ == "__main__":
    main()