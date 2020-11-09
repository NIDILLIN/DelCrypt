#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright 2020 Nico Dillinger
# LICENSE
"""
This file is part of DelCrypt.
DelCrypt is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

DelCrypt is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with DelCrypt.  If not, see <https://www.gnu.org/licenses/>.
"""
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

# salt = os.urandom(16)

# secret_text = b"tododododdododdod"
# password = b"passcode"


# kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)

# key = base64.urlsafe_b64encode(kdf.derive(password))

# key2 = base64.urlsafe_b64decode(key)


# token = Fernet(key).encrypt(b"Secret message!")


def encrypt (object, password):
	salt = b"abd05bwet035guw="
	this = object
	this_bytes = this.encode('utf-8')

	kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
	key = base64.urlsafe_b64encode(kdf.derive(password.encode('utf-8'))) # must be bytes-like

	token = Fernet(key).encrypt(this_bytes)
	print(token)

def decrypt (object, password):
	pass


encrypt("same string", "pass")

