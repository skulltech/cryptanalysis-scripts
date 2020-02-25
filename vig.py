CSTHRES = 150
ic_english = 0.0686
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def chisquared(txt):
	expected = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150, 0.01974, 0.00074]
	expected = [x * len(txt) for x in expected]
	given = [0] * 26
	for c in txt:
		given[chars.index(c)] += 1
	cs = 0
	for i in range(26):
		cs = cs + (((given[i] - expected[i]) ** 2) / expected[i])
	return cs

def caesar(txt, k):
	ret = []
	for c in txt:
		ret.append(chars[(chars.index(c) + k) % 26])
	ret = ''.join(ret)
	return ret

def crack(cipher, klen):
	key = []
	strings = [''] * klen
	for i in range(len(cipher) // klen):
		for j in range(klen):
			try:
				strings[j] = strings[j] + cipher[i*klen + j]
			except IndexError:
				break
	for i in range(klen):
		for j in range(26):
			cs = chisquared(caesar(strings[i], j))
			if cs < CSTHRES:
				key.append(j)
	return key

def decrypt(cipher, key):
	plain = []
	for i, c in enumerate(cipher):
		plain.append(caesar(c, key[i % len(key)]))
	return ''.join(plain)

def IC(txt):
	given = [0] * 26
	for c in txt:
		given[chars.index(c)] += 1
	ic = 0
	for fi in given:
		ic += fi * (fi - 1)
	ic = ic / (len(txt) * (len(txt) + 1))
	return ic


def cracklen(cipher):
	klenb = None
	for klen in range(1, 11):
		strings = [''] * klen
		for i in range(len(cipher) // klen):
			for j in range(klen):
				try:
					strings[j] = strings[j] + cipher[i*klen + j]
				except IndexError:
					break
		icavg = sum([IC(x) for x in strings]) / klen
		print(klen, icavg)
		if icavg > ic_english:
			klenb = klen
			break
	if not klenb:
		print('[*] Could not find key length!')
	else:
		return klenb


cipher = 'SXULW GNXIO WRZJG OFLCM RHEFZ ALGSP DXBLM PWIQT XJGLA RIYRI BLPPC HMXMG CTZDL CLKRU YMYSJ TWUTX ZCMRH EFZAL OTMNL BLULV MCQMG CTZDL CPTBI AVPML NVRJN SSXWT XJGLA RIQPE FUGVP PGRLG OMDKW RSIFK TZYRM QHNXD UOWQT XJGLA RIQAV VTZVP LMAIV ZPHCX FPAVT MLBSD OIFVT PBACS EQKOL BCRSM AMULP SPPYF CXOKH LZXUO GNLID ZVRAL DOACC INREN YMLRH VXXJD XMSIN BXUGI UPVRG ESQSG YKQOK LMXRS IBZAL BAYJM AYAVB XRSIC KKPYH ULWFU YHBPG VIGNX WBIQP RGVXY SSBEL NZLVW IMQMG YGVSW GPWGG NARSP TXVKL PXWGD XRJHU SXQMI VTZYO GCTZR JYVBK MZHBX YVBIT TPVTM OOWSA IERTA SZCOI TXXLY JAZQC GKPCS LZRYE MOOVC HIEKT RSREH MGNTS KVEPN NCTUN EOFIR TPPDL YAPNO GMKGC ZRGNX ARVMY IBLXU QPYYH GNXYO ACCIN QBUQA GELNR TYQIH LANTW HAYCP RJOMO KJYTV SGVLY RRSIG NKVXI MQJEG GJOML MSGNV VERRC MRYBA GEQNP RGKLB XFLRP XRZDE JESGN XSYVB DSSZA LCXYE ICXXZ OVTPW BLEVK ZCDEA JYPCL CDXUG MARML RWVTZ LXIPL PJKKL CIREP RJYVB ITPVV ZPHCX FPCRG KVPSS CPBXW VXIRS SHYTU NWCGI ANNUN VCOEA JLLFI LECSO OLCTG CMGAT SBITP PNZBV XWUPV RIHUM IBPHG UXUQP YYHNZ MOKXD LZBAK LNTCC MBJTZ KXRSM FSKZC SSELP UMARE BCIPK GAVCY EXNOG LNLCC JVBXH XHRHI AZBLD LZWIF YXKLM PELQG RVPAF ZQNVK VZLCE MPVKP FERPM AZALV MDPKH GKKCL YOLRX TSNIB ELRYN IVMKP ECVXH BELNI OETUX SSYGV TZARE RLVEG GNOQC YXFCX YOQYO ISUKA RIQHE YRHDS REFTB LEVXH MYEAJ PLCXK TRFZX YOZCY XUKVV MOJLR RMAVC XFLHO KXUVE GOSAR RHBSS YHQUS LXSDJ INXLH PXCCV NVIPX KMFXV ZLTOW QLKRY TZDLC DTVXB ACSDE LVYOL BCWPE ERTZD TYDXF AILBR YEYEG ESIHC QMPOX UDMLZ VVMBU KPGEC EGIWO HMFXG NXPBW KPVRS XZCEE PWVTM OOIYC XURRV BHCCS SKOLX XQSEQ RTAOP WNSZK MVDLC PRTRB ZRGPZ AAGGK ZIMAP RLKVW EAZRT XXZCS DMVVZ BZRWS MNRIM ZSRYX IEOVH GLGNL FZKHX KCESE KEHDI FLZRV KVFIB XSEKB TZSPE EAZMV DLCSY ZGGYK GCELN TTUIG MXQHT BJKXG ZRFEX ABIAP MIKWA RVMFK UGGFY JRSIP NBJUI LDSSZ ALMSA VPNTX IBSMO'
cipher = ''.join(cipher.split())
klen = cracklen(cipher)
print('[*] Key length:', klen)
key = crack(cipher, klen)
print('[*] Key:', key)
print(decrypt('BELOSZ', key))
