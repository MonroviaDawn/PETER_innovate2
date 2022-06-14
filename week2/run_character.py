from character import Hero

raizo = Hero("Raizo of the Mist", "Raizo", "Wano-kuni", "C" )
saiyaman = Hero("Saiyaman the Great", "Gohan", "East Sky", "A")
hulk = Hero("The Hulk", "Bruce Banner", "M.C.U", "S")
chronos = Hero("Chronos", "Ellington Moss", "Orlone District", "D")

hulk.set_powers("SMASH")
print(hulk.get_powers())
hulk.set_powers("JUMP")

print(hulk.get_powers())