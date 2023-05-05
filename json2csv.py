#!/usr/bin/python3

import argparse
import json
import sys
from csv import DictWriter

SEP = "."

def arguments():
	parser = argparse.ArgumentParser(
		prog="json2csv",
		description="convert JSON file(s) to CSV",
		epilog="made with ❤️ by lion5"
	)
	parser.add_argument("json", nargs="+", help="source JSON files")
	parser.add_argument("--output", "-o", nargs="*", help="target file(s). uses basename of jsons if missing")
	return parser


def write_csv(out_fp, field_names, lines):
	writer = DictWriter(out_fp, field_names, dialect="excel")
	writer.writeheader()
	writer.writerows(lines)


def flat_json(obj, base=""):
	out = dict()
	if type(obj) is list:
		for i, v in enumerate(obj):
			out.update(**flat_json(v, f"{base}{i}{SEP}"))
	elif type(obj) is dict:
		for k in obj:
			out.update(**flat_json(obj[k], f"{base}{k}{SEP}"))
	else:
		key = base.strip(SEP)
		out[key] = obj
	return out


def json2csv(obj, target_fp):
	flat = []
	if type(obj) is list:
		for o in obj:
			flat.append(flat_json(o))
	else:
		flat.append(flat_json(obj))
	write_csv(target_fp, flat[0].keys(), flat)


def file2csv(src, target=None):
	if not target:
		target = src.replace(".json", ".csv")
	with open(src) as src_fp:
		json_data = json.load(src_fp)
	with open(target, "w") as out:
		json2csv(json_data, out)


if __name__ == '__main__':
	args = arguments().parse_args()
	if args.output and len(args.output) != len(args.json):
		print("ERROR: length of JSON input files and output files does not match", file=sys.stderr)
		sys.exit(1)
	for i, json_file in enumerate(args.json):
		file_args = [json_file]
		if args.output:
			file_args.append(args.output[i])
		file2csv(*file_args)
