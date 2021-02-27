from abc import ABC, abstractmethod


class Hero:
    """
    Initial hero class
    """

    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(ABC, Hero):
    """
    Abstract class interface
    """

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    """
    Abstract Positive class interface
    """

    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    """
    Abstract Negative class interface
    """

    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    """
    Positive buff spell
    """

    def get_stats(self):
        """
        Method will:
        Increase: Strength, Endurance, Agility, Luck on 7
        Decrease: Perception, Charisma, Intelligence on 3
        Add 50 HP
        """
        stats = self.base.get_stats()
        # increase: Strength, Endurance, Agility, Luck on 7
        stats['Strength'] += 7
        stats['Endurance'] += 7
        stats['Agility'] += 7
        stats['Luck'] += 7
        # decrease: Perception, Charisma, Intelligence on 3
        stats['Perception'] -= 3
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        # ddd 50 HP
        stats['HP'] += 50

        return stats

    def get_positive_effects(self):
        """
        Method will add Berserk to self.positive_effects list
        """
        return self.base.get_positive_effects() + ['Berserk']


class Blessing(AbstractPositive):
    """
    Positive buff spell
    """

    def get_stats(self):
        """
        Method will:
        Increase: Strength, Endurance, Agility, Luck, Perception, Charisma, Intelligence on 2
        """
        stats = self.base.get_stats()

        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2

        return stats

    def get_positive_effects(self):
        """
        Method will add Blessing to self.positive_effects list
        """
        return self.base.get_positive_effects() + ['Blessing']


class Weakness(AbstractNegative):
    """
    Negative buff spell
    """

    def get_stats(self):
        """
        Method will:
        Decrease: Strength, Endurance, Agility on 4
        """
        stats = self.base.get_stats()
        # уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4

        return stats

    def get_negative_effects(self):
        """
        Method will add Weakness to self.negative_effects list
        """
        return self.base.get_negative_effects() + ['Weakness']


class EvilEye(AbstractNegative):
    """
    Negative buff spell
    """

    def get_stats(self):
        """
        Method will:
        Decrease: Luck on 10
        """
        stats = self.base.get_stats()
        # уменьшает  характеристику Удача на 10.
        stats['Luck'] -= 10

        return stats

    def get_negative_effects(self):
        """
        Method will add EvilEye to self.negative_effects list
        """
        return self.base.get_negative_effects() + ['EvilEye']


class Curse(AbstractNegative):
    """
    Negative buff spell
    """

    def get_stats(self):
        """
        Method will:
        Decrease: Strength, Endurance, Agility, Luck, Perception, Charisma, Intelligence, on 2
        """
        stats = self.base.get_stats()

        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2

        return stats

    def get_negative_effects(self):
        """
        Method will add Curse to self.negative_effects list
        """
        return self.base.get_negative_effects() + ['Curse']


if __name__ == "__main__":
    hero = Hero()
    print(hero.get_stats())
    print(hero.get_negative_effects())
    print(hero.get_positive_effects())
    print('_________________________')

    brs1 = Berserk(hero)
    print(brs1.get_stats())
    print(brs1.get_negative_effects())
    print(brs1.get_positive_effects())
    print('_________________________')

    brs2 = Berserk(brs1)
    cur1 = Curse(brs2)

    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())

    cur1.base = brs1
    print(cur1.get_stats())
    print(cur1.get_positive_effects())
    print(cur1.get_negative_effects())
