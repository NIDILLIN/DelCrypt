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


salt = b"abd05bwet035guw="

def encrypt (item, password):
	this_bytes = item.encode('utf-8') # encode to bytes
	passcode = password.encode('utf-8') # encode to bytes

	kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
	key = base64.urlsafe_b64encode(kdf.derive(passcode))

	enc_token = Fernet(key).encrypt(this_bytes)
	return enc_token
	
def decrypt (enc_item, password):
	passcode = password.encode('utf-8') # encode to bytes

	kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
	key = base64.urlsafe_b64encode(kdf.derive(passcode))
	
	dec_token = Fernet(key).decrypt(enc_item).decode('utf-8')
	return dec_token
