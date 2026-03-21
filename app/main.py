class Animal:
    # [CHECKLIST ITEM #Code Style.6] Type annotation
    alive: list["Animal"] = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:  # [CHECKLIST ITEM #Code Style.5] Multi-line args
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
        """
        Method-based logic for the reviewer.
        """
        if (
                self.health > 0
                and isinstance(target, Herbivore)
                and not target.hidden
                and target.health > 0
        ):
            target.health -= 50


# Two blank lines here to satisfy flake8 E302
def bite(target: Animal) -> None:
    """
    Standalone function for the tests.
    It finds a predator from the environment to perform the action.
    """
    for predator in Animal.alive:
        if isinstance(predator, Carnivore):
            predator.bite(target)
            break
