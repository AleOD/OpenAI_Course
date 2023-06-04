import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import logging
import json

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

app = Flask(__name__, template_folder='templates', static_url_path = '', static_folder = 'static')
app.logger.setLevel(logging.INFO)

# def get_colors(msg):
#     prompt = f"""
#     You are a color palette generating assitant that responds to text prompts requesting color palettes.
#     YOu should generate color palettes that fit the theme, mood, or instructions in the prompt.
#     The palettes should range between 2 and 6 colors.

#     Q: Convert the following verbal description of a color palette into a list of colors: rain, cold, woods, road
#     A: ["#3E3434","#093428","#CA7D02","#123940","#6B312C"]

#     Q: Convert the following verbal description of a color palette into a list of colors: gryffindor
#     A: ["#740001","#AE0001","#EEBA30","#D3A625","#000000"]

#     Q: Convert the following verbal description of a color palette into a list of colors: taylor swift RED album
#     A: ["#1b1d39","#2a243d","#785f54","#403243","#ab2549","#dfdcce"]

#     Q: Convert the following verbal description of a color palette into a list of colors: ocean, fresh, tropical
#     A: ["#007DD7","#01B8CA","#85DECC","#A8CA36","#DDE6E1"]

#     Desired Format: JSON array of hexadecimal color code

#     Q: Convert the following verbal description of a color palette into a list of colors:{msg}
#     A:
#     """

#     response = openai.Completion.create(
#         prompt=prompt,
#         model="text-davinci-003",
#         max_tokens=200,
#     )

#     colors = json.loads(response["choices"][0]["text"])
#     return colors

def get_colors_chat(msg):

    messages = [
        {"role": "system", "content": "You are a color palette generating assitant that responds to text prompts requesting color palettes. You should generate color palettes that fit the theme, mood, or instructions in the prompt. The palettes should range between 2 and 6 colors."},
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: rain, cold, woods, road"},
        {"role": "system", "content": '["#3E3434","#093428","#CA7D02","#123940","#6B312C"]'},
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: gryffindor"},
        {"role": "system", "content": '["#740001","#AE0001","#EEBA30","#D3A625","#000000"]'},
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: taylor swift RED album"},
        {"role": "system", "content": '["#1b1d39","#2a243d","#785f54","#403243","#ab2549","#dfdcce"]'},
        {"role": "user", "content": "Convert the following verbal description of a color palette into a list of colors: ocean, fresh, tropical"},
        {"role": "system", "content": '["#007DD7","#01B8CA","#85DECC","#A8CA36","#DDE6E1"]'},
        {"role": "user", "content": f"Convert the following verbal description of a color palette into a list of colors:{msg}"}
    ]
    response = openai.ChatCompletion.create(
        messages=messages,
        model="gpt-3.5-turbo",
        max_tokens=200,
    )

    colors = json.loads(response["choices"][0]["message"]["content"])
    return colors

@app.route("/palette", methods=["POST"])
def get_palette():
    query = request.form.get("query")
    colors = get_colors_chat(query)
    return {"colors": colors}
    # if query:
    #     return query
    # else:
    #     return "Invalid request: 'query' field is missing or empty"




@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

