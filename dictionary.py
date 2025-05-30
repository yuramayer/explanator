"""Dictionary class for the answers"""

from typing import List, Union
from difflib import get_close_matches, SequenceMatcher
from data_loader import load_data


class Dictionary:
    """
    Класс для поиска определений слов и обработки опечаток
    с использованием словаря из JSON-файла.
    """

    def __init__(self, json_path: str):
        """
        Загружает словарь и настраивает список утвердительных ответов.
        
        :param json_path: Путь к JSON-файлу со словарём.
        """
        self.data = load_data(json_path)
        self.affirmatives = {"yes", "y", "yeah", "yep"}

    def translate_word(self, word: str) -> Union[List[str], str]:
        """
        Пытается найти точное совпадение слова в словаре.
        Если не находит — вызывает подбор похожих слов.

        :param word: Слово, которое ввёл пользователь.
        :return: Список определений или строка с сообщением об ошибке.
        """
        for form in [word.lower(), word.capitalize(), word.upper()]:
            if form in self.data:
                return self.data[form]
        return self.suggest_similar_words(word)

    def suggest_similar_words(self, word: str) -> str:
        """
        Ищет наиболее похожие слова, если точного совпадения нет.

        :param word: Слово с возможной опечаткой.
        :return: Сообщение с предложением замены или об ошибке.
        """
        candidates = get_close_matches(word, self.data.keys(), n=3, 
                                       cutoff=0.75)
        if candidates:
            best = max(candidates,
                       key=lambda w: SequenceMatcher(None, word, w).ratio())
            return self.confirm_suggestion(best, word)
        return f"Я не знаю слово '{word}' :("

    def confirm_suggestion(self, suggestion: str, original: str
                           ) -> Union[List[str], str]:
        """
        Спрашивает пользователя, имел ли он в виду предложенное похожее слово.

        :param suggestion: Предполагаемое правильное слово.
        :param original: Исходное слово пользователя.
        :return: Определения найденного слова или сообщение об ошибке.
        """
        answer = input(
            f"Вы имели в виду '{suggestion}'? "
            "Введите 'yes' для подтверждения: ").strip().lower()
        if answer in self.affirmatives:
            return self.data[suggestion]
        return f"Я не знаю слово '{original}' :("
