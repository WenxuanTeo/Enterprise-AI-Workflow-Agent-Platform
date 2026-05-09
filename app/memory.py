class Memory:
    def __init__(self):
        self.store = {}

    def save(self, session_id, key, value):
        if session_id not in self.store:
            self.store[session_id] = {}
        self.store[session_id][key] = value

    def get(self, session_id, key):
        return self.store.get(session_id, {}).get(key)
