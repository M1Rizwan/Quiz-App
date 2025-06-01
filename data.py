# This file will get the random quize questions from "Trivia Question Database" API.

import random
import requests

# Set params for Trivia API.

parameter = {
    "amount": 10,
    "category": random.choice([23, 9, 11, 18, 22, 23]),
    # GK:9 / Films: 11 /Computers Scie:18 /Geography:22 / History:23 ## NOTE: SOME CATEGORIES ARE NOT WORKING.
    "difficulty": "easy",
    "type": "boolean"
}
data = requests.get(url="https://opentdb.com/api.php", params=parameter)
data.raise_for_status()
question_data = data.json()["results"]
typee = data.json()["results"][0]["category"]



# Below is the sample json we get in API response.
# question_data = [
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The HTML5 standard was published in 2014.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     }
# ]
