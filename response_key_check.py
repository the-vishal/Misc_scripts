import bs4 as bs
from urllib import request

url = 'https://ssc.digialm.com//per/g27/pub/.../touchstone/AssessmentQPHTMLMode1//....html'

sauce = request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, "lxml")

questions = soup.findAll("div", {"class": "question-pnl"})

correct_Ans = []
choosen_options = []

for question in questions:
	correct = question.find("td", {"class": "rightAns"})
	choosen = question.findAll("td", {"class": "bold"})[-1]

	correct_Ans.append(correct.text[0])
	choosen_options.append(choosen.text)

# print(choosen_options, len(choosen_options))
# print(correct_Ans, len(correct_Ans))

negative_marking = -1
mark_per_ques = 2

correct = 0
wrong = 0
total = 0


for index,ans in enumerate(choosen_options):
	if ans != ' -- ':
		if correct_Ans[index] == ans:
			correct += 1
		else:
			wrong += 1

total = correct*mark_per_ques + wrong*negative_marking

print("Right Answers : {}".format(correct))
print("Wrong Answers : {}".format(wrong))
print("====================================")
print("\n Total Marks: {}".format(total))