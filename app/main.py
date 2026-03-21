from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def __init__(
        self,
        name: str,
        health: int = 100,
        hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
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
    def bite(
        self,
        target: Animal
    ) -> None:
        # Carnivores can only bite herbivores that are not hiding
        if (
            isinstance(target, Herbivore)
            and not target.hidden
        ):
            target.health -= 50
            if target.health <= 0:
                Animal.alive.remove(target)


def bite(
    target: Animal
) -> None:
    # Logic to find a carnivore to perform the action
    # usually the last created carnivore in the alive list
    for animal in reversed(Animal.alive):
        if isinstance(animal, Carnivore):
            animal.bite(target)
            break
