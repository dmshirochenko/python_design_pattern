from abc import ABC, abstractmethod


class ObservableEngine(Engine):  # Наблюдаемая система
    def __init__(self):
        self.__subscribers = set()  # При инициализации множество подписчиков задается пустым

    def subscribe(self, subscriber):
        # Для того чтобы подписать пользователя, он добавляется во множество подписчиков
        self.__subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)  # Удаление подписчика из списка

    def notify(self, message):
        for subscriber in self.__subscribers:
            subscriber.update(message)  # Отправка уведомления всем подписчикам


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, message):
        """
        message: {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}
        """
        self.achievements.add(message['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, message):
        if message not in self.achievements:
            self.achievements.append(message)



if __name__ == '__main__':
    print('Start!')
    manager = ObservableEngine()
    printer1 = ShortNotificationPrinter()
    printer2 = FullNotificationPrinter()

    manager.subscribe(printer1)
    manager.subscribe(printer2)

    manager.notify({"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"})

    print(printer1.achievements)
    print(printer2.achievements)
