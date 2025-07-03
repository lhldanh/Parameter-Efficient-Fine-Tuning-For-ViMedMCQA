import json
import asyncio
import os
from googletrans import Translator
from tqdm import tqdm

start = 2001
end = 4000
postfix = '_vi_2'
file_path = 'test.json'

async def translate_text():
	async with Translator() as translator:
		with open(file_path, 'r', encoding='utf-8') as f:
			data = json.load(f)

		# If the JSON is a list of dicts
		if isinstance(data, list):
			items = data
		else:
			items = [data]
		items = items[start:end+1]
		count = 0
		result = []
		for item in items:
			count += 1
			if count % 100 == 0:
				print(f"Translated {count} items...")
			question = await translator.translate(item['question'], dest='vi')
			opa = await translator.translate(item['opa'], dest='vi')
			opb = await translator.translate(item['opb'], dest='vi')
			opc = await translator.translate(item['opc'], dest='vi')
			opd = await translator.translate(item['opd'], dest='vi')
			result.append({
				'question': question.text,
				'opa': opa.text,
				'opb': opb.text,
				'opc': opc.text,
				'opd': opd.text
			})

		# Save to new file
		base, ext = os.path.splitext(file_path)
		output_path = f"{base}{postfix}{ext}"
		with open(output_path, 'w', encoding='utf-8') as f:
			json.dump(result, f, ensure_ascii=False, indent=2)
		print(f"Translated file saved to {output_path}")

if __name__ == "__main__":
	os.environ.pop("SSL_CERT_FILE", None)
	asyncio.run(translate_text())