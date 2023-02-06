from django.contrib.auth.hashers import (
    BasePasswordHasher,
    mask_hash,
    must_update_salt,
)
from django.utils.crypto import constant_time_compare
from django.utils.translation import gettext_noop as _

import crypt


class SHA512PasswordHasher(BasePasswordHasher):
    """
    """

    algorithm = "6"
    iterations = 399999

    def encode(self, password, salt):
        assert password is not None
        assert salt and '$' not in salt
        self._check_encode_args(password, salt)
        hash = crypt.crypt(password, f'$6$rounds={self.iterations}${salt}')
        return hash

    def decode(self, encoded):
        algorithm, rounds, salt, hash = encoded.split("$")[1:]
        rounds = rounds.split('=')[-1]
        assert algorithm == self.algorithm
        return {
            "algorithm": algorithm,
            "hash": hash,
            'rounds': rounds,
            "salt": salt,
        }

    def verify(self, password, encoded):
        decoded = self.decode(encoded)
        encoded_2 = self.encode(password, decoded["salt"])
        is_correct = constant_time_compare(encoded, encoded_2)
        return is_correct

    def safe_summary(self, encoded):
        decoded = self.decode(encoded)
        return {
            _("algorithm"): decoded["algorithm"],
            _("rounds"): decoded["rounds"],
            _("salt"): mask_hash(decoded["salt"], show=2),
            _("hash"): mask_hash(decoded["hash"]),
        }

    def must_update(self, encoded):
        decoded = self.decode(encoded)
        return must_update_salt(decoded["salt"], self.salt_entropy)

    def harden_runtime(self, password, encoded):
        pass