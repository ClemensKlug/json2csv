import filecmp
import os
from tempfile import NamedTemporaryFile

import json2csv

def helper(src_filename, expected_filename, base="fixtures"):
	src = os.path.join(base, src_filename)
	expected = os.path.join(base, expected_filename)
	with NamedTemporaryFile() as tmp:
		json2csv.file2csv(src, tmp.name)
		lines = [line for line in tmp]
		with open(expected, "rb") as ex:
			expected_lines = [line for line in ex]
		assert expected_lines == lines
		assert filecmp.cmp(expected, tmp.name, shallow=False) # nice interface, but ugly test failure :(

def test_column_names():
	helper("column_names.json", "column_names.csv")
	