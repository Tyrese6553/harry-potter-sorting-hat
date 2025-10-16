from InquirerPy import inquirer
from pyfiglet import Figlet
from ascii_magic import AsciiArt
import time

figlet = Figlet(font="small")


def main():
    my_art = AsciiArt.from_image(r"images\download1.png")
    my_art.to_terminal(columns=100)

    name = get_name()

    answers = get_ans()

    score = calculate_score(answers)

    house = get_house(score)

    time.sleep(2)
    print("Hhm, right, okay.... ")
    time.sleep(3)
    print("Plenty of courage, I see. Not a bad mind, either...")
    time.sleep(2)
    print("Now that's interesting. Better be...got it.")
    time.sleep(3)
    print(figlet.renderText(f"Congratulations, {name}\nYou belong in {house}!"))
    time.sleep(3)

    if house == "GRYFFINDOR":
        my_art = AsciiArt.from_image(r"images\G.png")
        my_art.to_terminal(columns=80)

    elif house == "HUFFLEPUFF":
        my_art = AsciiArt.from_image(r"images\H.png")
        my_art.to_terminal(columns=80)

    elif house == "RAVENCLAW":
        my_art = AsciiArt.from_image(r"images\R.png")
        my_art.to_terminal(columns=80)

    elif house == "SLYTHERIN":
        my_art = AsciiArt.from_image(r"images\S.png")
        my_art.to_terminal(columns=80)


def get_name():

    name = inquirer.text(
        message="State your name, please.\n",
        validate=lambda input: len(input) > 0,
        invalid_message="Your name, please",
        qmark="🌑",
        amark="☀️ ",
    ).execute()
    return name.capitalize()


def get_ans():

    questions = [
        "1. Facing an imminent, terrifying danger, what is your first instinct?",
        "2. Which quality do you secretly or openly admire most in others?",
        "3. You've been given a complex puzzle. What is your primary focus?",
        "4. A friend has cheated on a test. What is your reaction?",
        "5. What does 'success' fundamentally mean to you?",
        "6. Which artifact appeals to you the most?",
        "7. In a group project, what role do you naturally gravitate toward?",
        "8. What is your greatest fear?",
        "9. If you had an important secret, what would you do?",
        "10. Your ideal evening activity involves...",
    ]
    choices = [
        [
            "A. Rush forward to face it head-on, protecting others if necessary.",
            "B. Stand by those you care about, offering support and solidarity.",
            "C. Quickly analyze the threat, looking for a clever way to outwit it.",
            "D. Assess how this situation might be leveraged for personal advantage later.",
        ],
        [
            "A. Boldness and a clear moral code.",
            "B. Dependability and a gentle spirit.",
            "C. Ingenuity and an insatiable curiosity.",
            "D. Dominance and the ability to get things done.",
        ],
        [
            "A. The excitement of the challenge, regardless of the outcome.",
            "B. The satisfaction of working through it diligently until it's complete.",
            "C. Identifying the underlying rules and structure to solve it efficiently.",
            "D. Finding the quickest, most unorthodox way to the solution to impress others.",
        ],
        [
            "A. I confront them about the betrayal of trust and fair play.",
            "B. I'd be loyal to my friend, but secretly wish they hadn't put me in this position.",
            "C. I try to understand the motivations and pressures that led to their choice.",
            "D. I evaluate whether their success could potentially benefit or harm my standing.",
        ],
        [
            "A. Achieving a victory that proves my own courage and convictions.",
            "B. Being surrounded by a loving, supportive, and harmonious community.",
            "C. The constant accumulation of knowledge and understanding.",
            "D. Reaching the highest possible position in my chosen field.",
        ],
        [
            "A. The Sword of Gryffindor, ready for battle.",
            "B. Helga Hufflepuff's Cup, symbolizing unity and hard work.",
            "C. Rowena Ravenclaw's Diadem, granting wisdom.",
            "D. Salazar Slytherin's Locket, a symbol of purity and influence.",
        ],
        [
            "A. The one who volunteers for the riskiest or most difficult parts.",
            "B. The reliable team player who ensures everyone is included and doing their best.",
            "C. The researcher or planner who determines the best strategy.",
            "D. The leader who organizes the workload and delegates tasks effectively.",
        ],
        [
            "A. Being exposed as a coward.",
            "B. Betrayal or being entirely alone.",
            "C. Being ignorant or unable to solve a difficult problem.",
            "D. Being powerless or irrelevant.",
        ],
        [
            "A. Guard it fiercely, ready to fight if someone tries to force it out of me.",
            "B. Only share it with a small, deeply trusted circle of friends.",
            "C. Immediately research the full implications of the secret.",
            "D. Use the knowledge selectively to gain an advantage in a future situation.",
        ],
        [
            "A. Participating in a spontaneous, exciting new sport or adventure.",
            "B. Cooking or sharing a hearty meal with friends and family.",
            "C. Deeply reading or studying a complex, fascinating topic.",
            "D. Networking at an exclusive event, meeting people who can advance your goals.",
        ],
    ]

    answers = []
    print(f"Welcome to the sorting hat! This quiz consists of 10 questions.")

    for index, question in enumerate(questions):
        answer = inquirer.select(
            message=question, choices=choices[index],
            height=4,
            instruction="Please select one from the below options",
            qmark="🌑",
            amark="☀️ ",
        ).execute()
        answers.append(answer[0:1])
    return answers


def calculate_score(answers):
    gryf = 0
    huff = 0
    raven = 0
    sly = 0

    for index, answer in enumerate(answers):
        if index == 0:
            if answer == "A":
                gryf += 3
                sly += 1
            elif answer == "B":
                huff += 3
                raven += 1
            elif answer == "C":
                huff += 1
                raven += 3
            elif answer == "D":
                gryf += 1
                sly += 3

        elif index == 1:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                huff += 3
                sly += 1
            elif answer == "C":
                huff += 1
                raven += 3
            elif answer == "D":
                gryf += 1
                sly += 3

        elif index == 2:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                gryf += 1
                huff += 3
            elif answer == "C":
                raven += 3
                sly += 1
            elif answer == "D":
                huff += 1
                sly += 3

        elif index == 3:
            if answer == "A":
                gryf += 3
                huff += 1
            elif answer == "B":
                gryf += 1
                huff += 3
            elif answer == "C":
                raven += 3
                sly += 1
            elif answer == "D":
                huff += 1
                sly += 3

        elif index == 4:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                huff += 3
                sly += 1
            elif answer == "C":
                huff += 1
                raven += 3
            elif answer == "D":
                gryf += 1
                sly += 3

        elif index == 5:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                huff += 3
                sly += 1
            elif answer == "C":
                gryf += 1
                raven += 3
            elif answer == "D":
                huff += 1
                sly += 3

        elif index == 6:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                huff += 3
                raven += 1
            elif answer == "C":
                raven += 1
                sly += 3
            elif answer == "D":
                gryf += 1
                sly += 3

        elif index == 7:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                huff += 3
                sly += 1
            elif answer == "C":
                huff += 1
                raven += 3
            elif answer == "D":
                huff += 1
                sly += 3

        elif index == 8:
            if answer == "A":
                gryf += 3
                sly += 1
            elif answer == "B":
                huff += 3
                raven += 1
            elif answer == "C":
                gryf += 1
                raven += 3
            elif answer == "D":
                huff += 1
                sly += 3

        elif index == 9:
            if answer == "A":
                gryf += 3
                raven += 1
            elif answer == "B":
                huff += 3
                sly += 1
            elif answer == "C":
                huff += 1
                raven += 3
            elif answer == "D":
                gryf += 1
                sly += 3

    return {"GRYFFINDOR": gryf, "HUFFLEPUFF": huff, "RAVENCLAW": raven, "SLYTHERIN": sly}


def get_house(score):
    return max(score, key=score.get)


if __name__ == "__main__":
    main()
