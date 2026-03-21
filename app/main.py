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
    def bite(self, target: Animal) -> None:
        # Check if the target is a Herbivore and not currently hidden
        if isinstance(target, Herbivore) and not target.hidden:
            target.health -= 50
            if target.health <= 0:
                # Remove from the registry if the animal is dead
                if target in Animal.alive:
                    Animal.alive.remove(target)


# THIS IS THE PART YOU NEED TO ADD AT THE BOTTOM
# It must be at the very left margin (not indented!)
def bite(target: Animal) -> None:
    # This finds a Carnivore in the list and makes it bite the target
    for animal in Animal.alive:
        if isinstance(animal, Carnivore):
            animal.bite(target)
            break
