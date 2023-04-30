import os
import openai


while True:
  question = input("\033[34mWhat is your question?\n\033[0m")
  if question.lower() == "exit":
    print("\033[31mGoodbye!\n\033[0m")
    break

  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    # prompt = "Generate Book Recommendations based on user input",
    messages=[
      {"role": "system", "content": "Generate a book recommendation based on the given question."},
        {"role": "user", "content": question}
      ]
    )
  print("\033[32m" +
  completion.choices[0].message.content + "\n")