import pandas as pd
pd.set_option('display.max_columns', 500)
import people_also_ask
from gen_keywords import keyword, keyword_list, keyword_suggestion_list
from utils_gen import create_question_and_answers_list_by_suggestion

# create dataframe to stock answers
df = pd.DataFrame(columns=['Keywords'])
df['Keywords'] = keyword_list

# create list of questions related to keyword
questions_list = []
PAA_1_k, PAA_2_k, PAA_3_k, PAA_4_k, PAA_5_k = [], [], [], [], []
questions_list = people_also_ask.get_related_questions(keyword, 5)

print('step1')


# create list of answer related to questions
content_PAA_1_k, content_PAA_2_k, content_PAA_3_k, content_PAA_4_k, content_PAA_5_k = [], [], [], [], []


for i in range(5):
    if len(questions_list)>0:
        PAA_1_k.append(questions_list[0])
        answer1 = people_also_ask.get_simple_answer(questions_list[0])
        if answer1:
            content_PAA_1_k.append(answer1)
        else:
            content_PAA_1_k.append("no content")

        PAA_2_k.append(questions_list[1])
        answer2 = people_also_ask.get_simple_answer(questions_list[1])
        if answer2:
            content_PAA_2_k.append(answer2)
        else:
            content_PAA_2_k.append("no content")

        PAA_3_k.append(questions_list[2])
        answer3 = people_also_ask.get_simple_answer(questions_list[2])
        if answer3:
            content_PAA_3_k.append(answer3)
        else:
            content_PAA_3_k.append("no content")

        PAA_4_k.append(questions_list[3])
        answer4 = people_also_ask.get_simple_answer(questions_list[3])
        if answer4:
            content_PAA_4_k.append(answer4)
        else:
            content_PAA_4_k.append("no content")

        PAA_5_k.append(questions_list[4])
        answer5 = people_also_ask.get_simple_answer(questions_list[4])
        if answer5:
            content_PAA_5_k.append(answer5)
        else:
            content_PAA_5_k.append("no content")
    else:
        PAA_1_k.append("no question")
        content_PAA_1_k.append("no content")
        PAA_2_k.append("no question")
        content_PAA_2_k.append("no content")
        PAA_3_k.append("no question")
        content_PAA_3_k.append("no content")
        PAA_4_k.append("no question")
        content_PAA_4_k.append("no content")
        PAA_5_k.append("no question")
        content_PAA_5_k.append("no content")


print('step2')

df['PAA_1_k'] = PAA_1_k
df['PAA_2_k'] = PAA_2_k
df['PAA_3_k'] = PAA_3_k
df['PAA_4_k'] = PAA_4_k
df['PAA_5_k'] = PAA_5_k

df['content_PAA_1_k'] = content_PAA_1_k
df['content_PAA_2_k'] = content_PAA_2_k
df['content_PAA_3_k'] = content_PAA_3_k
df['content_PAA_4_k'] = content_PAA_4_k
df['content_PAA_5_k'] = content_PAA_5_k

# #####################################################################################################################"


# list of questions for one keyword suggestion
PAA_1_ks, PAA_2_ks, PAA_3_ks, PAA_4_ks, PAA_5_ks = [], [], [], [], []
list_of_q_list = [PAA_1_ks, PAA_2_ks, PAA_3_ks, PAA_4_ks, PAA_5_ks]
# list of answers for questions
content_PAA_1_ks, content_PAA_2_ks, content_PAA_3_ks, content_PAA_4_ks, content_PAA_5_ks = [], [], [], [], []
list_of_a_list = [content_PAA_1_ks, content_PAA_2_ks, content_PAA_3_ks, content_PAA_4_ks, content_PAA_5_ks]


print('step3')

df['Keyword_suggestion'] = keyword_suggestion_list

for suggestion in keyword_suggestion_list:
    create_question_and_answers_list_by_suggestion(suggestion, list_of_q_list, list_of_a_list)

df['PAA_1_ks'] = PAA_1_ks
df['PAA_2_ks'] = PAA_2_ks
df['PAA_3_ks'] = PAA_3_ks
df['PAA_4_ks'] = PAA_4_ks
df['PAA_5_ks'] = PAA_5_ks

df['content_PAA_1_ks'] = content_PAA_1_ks
df['content_PAA_2_ks'] = content_PAA_2_ks
df['content_PAA_3_ks'] = content_PAA_3_ks
df['content_PAA_4_ks'] = content_PAA_4_ks
df['content_PAA_5_ks'] = content_PAA_5_ks


print('step4')
# ################################################################################################
# save in csv to transfer to notebook
df.to_csv("for_generation.csv",sep=',', index=False)