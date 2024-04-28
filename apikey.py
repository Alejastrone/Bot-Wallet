# Api Key, y Api Secret
wallet = input("Elija la cuenta = Master:1, Developer:2, Produccion:3 = ")
if wallet == "1":
	user = "Master"
	API_KEY = "hq7tGRGwZlcRLu0zXF7XXUGizVBryEEOCKGXJ5qoKHNrmaw638WpAhyhaKNrMrp1"
	API_SECRET = "f5vTDZH6UuajtVFBcO6MKgRfeFaYskLB8oNcxBssXmKohEpNDDdKmySCoxvqRBEt"
elif wallet == "2":
	user = "Developer"
	API_KEY = "E6HbUIdg62mb25OiTV6fKwBB0b1ONoE2JcdL1sWypminROlOwwsS4xeQhoK80B0Y"
	API_SECRET = "KmiVfiu0HRLsxgLtNId0Ph8N4asiKrpSHcFdVgPOzBS9oIpcvcBqKCNPHJrB7256"
elif wallet == "3":
	user = "Produccion"
	API_KEY = "tlvXngay5ZFjgQcO6HEMcPszAM9JGY8MGBlZAZnrNEJ6FAOThjTvNTHofv7WTvuR"
	API_SECRET = "79hWOQzrjQE1s2PUUOw8HgjZ6Qdc9gXnUGt1vbiUpSqF4YHuHq9i5dHaJJ5cUa0B"	