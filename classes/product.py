class Product:
    def __init__(self, name: str, price: float, quantity: int, tags = []) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.tags = tags

    def storage_avaliable(self, value: int = 0) -> bool:
        if self.quantity >= value:
            return True
        else:
            return False

    def increment_storage(self, incoming: int) -> int:
        self.quantity += incoming

        return self.quantity

    def decrement_storage(self, outcoming: int) -> int:
        if not self.storage_avaliable(outcoming):
            raise ValueError("Not enough storage")

        self.quantity -= outcoming

        return self.quantity

    def storage_report(self) -> str:
        if self.quantity < 10:
            return 'Storage is CRITICAL LOW'
        elif self.quantity < 25:
            return 'Storage is LOW'
        elif self.quantity < 50:
            return 'Storage is MEDIUM'
        else:
            return 'Storage is OK'

    def show_tags(self, tagsToShow) -> str:
        if tagsToShow > len(self.tags):
            raise ValueError("Not enough tags")

        tag = 0

        while tag < tagsToShow:
            print(self.tags[tag])

        tag += 1

    def tag_is_in_position(self, tag, position: int) -> bool:
        if self.tags[position] == tag:
            return True
        else:
            return False

    def change_tag(self, oldTag, newTag):
        for index, tag in enumerate(self.tags):
            if tag == oldTag:
                self.tags[index] = newTag
                break

        return self.tags
