#segment별 word 분리 > db저장
#contents_words
#file명/segment수/word/word시작시점/word길이/confidence


import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="*******",
    database="ai_db"
)

cursor=conn.cursor()

a = '03'

for i in range(1,7):
    with open('C:/Users/SEC/PycharmProjects/cv_ai\STT전사/txt10301300/05_'+a+'/05_'+a+'_'+ str(i).zfill(2) +'.txt','r', encoding = 'utf-8') as file:
        mystring = file.read()
        no_file = '05_'+a+'_' + str(i).zfill(2)

    import json
    dict = json.loads(mystring)

    n_segment = len(dict["results"])
    print(n_segment)

    for i in range(n_segment):
        print("★",i+1,"번째 segment★")
        print(no_file)
        count_segment = i+1
        print(count_segment)
        results = dict["results"][i]
        segment = results["segment"]
        print(segment) #1
        result = results["result"]
        # print(result)
        hypotheses = result["hypotheses"]
        # print(hypotheses)
        hypotheses_1 = hypotheses[0]
        # print(hypotheses_1)
        transcript = hypotheses_1["transcript"]
        print(transcript) #2

        for_n_word = hypotheses_1["word-alignment"] #word개수구하려고
        n_word = len(for_n_word) #word개수 아래 for문에 적용

        for j in range(n_word):
            word_alignment = hypotheses_1["word-alignment"][j]
            # print(word_alignment)
            start = word_alignment["start"]
            print(start) #3
            length = word_alignment["length"]
            print(length) #4
            word = word_alignment["word"]
            if word[0] == "|":
                word = word[1:]
            print(word) #5
            confidence = word_alignment["confidence"]
            print(confidence) #6
            print("="*50)

            sql = """insert into contents_words(file, no_segment, word, word_start, word_length, confidence)
                       values(%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, (no_file, count_segment, word, start, length, confidence))
            conn.commit()
conn.close()