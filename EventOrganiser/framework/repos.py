class Repo:

    _items = []

    def __init__(self, *items):
        self._items = [item for item in items]


    def get_items(self):
        return self._items

    def add(self, *items):
        for item in items:
            self.get_items().append(item)

    def remove(self, item):
        try:
            self.get_items().remove(item)
        except Exception as ex:
            raise Exception(ex)

    def index_of(self, item):
        return self.get_items().index(item)

    def swap(self, item1, item2):
        self.get_items()[self.index_of(item1)] = item2

    def get_item_with_field_name_and_value(self, field_name, value):
        for item in self.get_items():
            if item.get_field_with_name(field_name) != None:
                return item
        raise Exception("No item found!")
