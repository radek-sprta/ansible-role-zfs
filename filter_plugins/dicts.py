"""Custom filters for dictionaries."""


class FilterModule(object):
    def filters(self):
        return {"remove_key": self.remove_key}

    def remove_key(self, dict_to_reduce, key_to_remove):
        """Filter to remove single given key from a dictionary."""
        return {k: v for k, v in dict_to_reduce.items() if k != key_to_remove}
