"""The front page of the app"""

from dictionary import Dictionary


def main():
    """Main func for the app"""
    dict_tool = Dictionary("data.json")
    print("👋 Привет! Я помогу найти значение слов. "
          "Введите exit() для выхода.\n")

    while True:
        user_input = input("Введите слово: ").strip()
        if user_input == "exit()":
            print("До свидания!")
            break

        result = dict_tool.translate_word(user_input)
        if isinstance(result, list):
            for i, line in enumerate(result, 1):
                print(f"{i}. {line}")
        else:
            print(result)
        print("")


if __name__ == "__main__":
    main()
