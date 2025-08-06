import secrets
import string


class Generator:
    def string_random(self, length: int):
        latters = (
            string.ascii_letters + string.digits + string.punctuation + string.digits
        )

        return "".join(secrets.choice(latters) for i in range(length))


gen = Generator()
