import people_also_ask


def create_question_and_answers_list_by_suggestion(keyword_suggestion, list_of_q_list, list_of_a_list):
    """
    :param keyword_suggestion: str, one keyword to create
    :param list_of_q_list: list of many list of questions to answer
    :param list_of_a_list: list of answers for each questions
    :return:
    """
    q_list = people_also_ask.get_related_questions(keyword_suggestion, 5)

    for i in range(5):
        if len(q_list) > 0:
            list_of_q_list[i].append(q_list[i])

            answer = people_also_ask.get_simple_answer(q_list[i])
            if answer:
                list_of_a_list[i].append(answer)
            else:
                list_of_a_list[i].append("no answer")
        else:
            list_of_q_list[i].append("no question")
            list_of_a_list[i].append("no answer")