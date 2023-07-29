import openai

fileopen = open(r'C:\Users\Vignesh\prodip\Ai\database\api.txt', 'r')
api = fileopen.read().strip()
fileopen.close()

openai.api_key = api

completion = openai.Completion()

def reply(q, chat_log=None):
    filelog = open(r"C:\Users\Vignesh\prodip\Ai\database\chat_log.txt", "r")
    chat_log_template = filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = chat_log_template+ f' \n YOU : {q}\nJarvis:'
    resp = completion.create(model="text-davinci-002", prompt=prompt,
                             temperature=0, max_tokens=100, top_p=1,
                             frequency_penalty=0, presence_penalty=0.5,best_of=1)

    ans = resp.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'{chat_log} \n You: {q}\nJarvis: {ans}'

    filelog = open(r"C:\Users\Vignesh\prodip\Ai\database\chat_log.txt", "w")
    filelog.write(chat_log_template_update)
    filelog.close()

    return ans

import openai


def Qreply(q, chat_log=None):
    filelog = open(r"C:\Users\Vignesh\prodip\Ai\database\chat_q.txt", "r")
    chat_log_template = filelog.read()
    filelog.close()

    if chat_log is None:
        chat_log = chat_log_template

    prompt = chat_log_template+f' \n You: {q}\nJarvis:'
    resp = completion.create(model="text-davinci-002", prompt=prompt,
                             temperature=0, max_tokens=100, top_p=1,
                             frequency_penalty=0, presence_penalty=0.5,best_of=1)

    ans = resp.choices[0].text.strip()
    chat_log_template_update = chat_log_template + f'{chat_log} \n Q: {q}\nA: {ans}'

    filelog = open(r"C:\Users\Vignesh\prodip\Ai\database\chat_q.txt", "w")
    filelog.write(chat_log_template_update)
    filelog.close()

    return ans

