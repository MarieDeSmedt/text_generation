import trafilatura
from gen_keywords import myurl




downloaded = trafilatura.fetch_url('https://fr.wikipedia.org/wiki/Roller_derby')

result = trafilatura.extract(downloaded) # trafilatura.process_record is deprecated but works
print("result: ")
print(result)
# newlines preserved, TXT output ...


