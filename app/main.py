class Animal:
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self._health = health
        self.hidden = hidden
        if self._health > 0 and self not in Animal.alive:
            Animal.alive.append(self)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        self._health = max(0, min(100, value))

        if self._health <= 0 and self in Animal.alive:
            Animal.alive.remove(self)
        elif self._health > 0 and self not in Animal.alive:
            Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}"
        )


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: "Animal") -> None:
        if (
                self.health > 0
                and isinstance(target, Herbivore)
                and not target.hidden
                and target.health > 0
        ):
            target.health -= 50


def bite(target: Animal) -> None:
    for animal in Animal.alive:
        if isinstance(animal, Carnivore):
            animal.bite(target)
            break
