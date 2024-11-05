import pandas as pd
import json

def excel2json(file_path, output_path):
    df = pd.read_excel(file_path)

    json_data = []

    for index, row in df.iterrows():
        incorrect_answers = str(row['incorrect_answers']).split('|')
        incorrect_answers = [answer.strip().replace("\"", "") for answer in incorrect_answers]

        question_data = {
            "type": row['type'],
            "difficulty": row['difficulty'],
            "category": row['category'],
            "question": row['question'],
            "correct_answer": row['correct_answer'],
            "incorrect_answers": incorrect_answers
        }

        json_data.append(question_data)
        
    json_object = {
		"response_code": 0,
		"results": json_data
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)

    print("Convert Excel to JSON successfully!")

excel2json('questions.xlsx', '..\\public\\questions.json')
