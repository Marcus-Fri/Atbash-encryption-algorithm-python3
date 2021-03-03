
"""Алгоритм шифрования 'Атбаш' """

def atbash(x):
	"""Меттод шифрования."""
	alphabet = " АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя0123456789"
	back_alphabet = "9876543210яЯюЮэЭьЬыЫъЪщЩшШчЧцЦхХфФуУтТсСрРпПоОнНмМлЛкКйЙиИзЗжЖёЁеЕдДгГвВбБаА "
	new_x = ""
	for i in x:
		for j in alphabet:
			ind_alp = alphabet.index(j)
			if i == j:
				new_x += back_alphabet[ind_alp]
				break
	
	return new_x


def atbash_deh(y):
	"""Меттод дешифровки."""
	alphabet = " АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя0123456789"
	back_alphabet = "9876543210яЯюЮэЭьЬыЫъЪщЩшШчЧцЦхХфФуУтТсСрРпПоОнНмМлЛкКйЙиИзЗжЖёЁеЕдДгГвВбБаА "
	new_y = ""
	for i in y:
		for j in back_alphabet:
			ind_alp = back_alphabet.index(j)
			if i == j:
				new_y += alphabet[ind_alp]
				break
				
	return new_y




print(atbash(""))
print(atbash_deh(""))	
