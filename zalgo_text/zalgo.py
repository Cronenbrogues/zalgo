import random


class zalgo:
    def __init__(self):
        self.numAccentsUp = (1, 3)
        self.numAccentsDown = (1, 3)
        self.numAccentsMiddle = (1, 2)
        self.maxAccentsPerLetter = 3
        self.dd = [
            "̖",
            " ̗",
            " ̘",
            " ̙",
            " ̜",
            " ̝",
            " ̞",
            " ̟",
            " ̠",
            " ̤",
            " ̥",
            " ̦",
            " ̩",
            " ̪",
            " ̫",
            " ̬",
            " ̭",
            " ̮",
            " ̯",
            " ̰",
            " ̱",
            " ̲",
            " ̳",
            " ̹",
            " ̺",
            " ̻",
            " ̼",
            " ͅ",
            " ͇",
            " ͈",
            " ͉",
            " ͍",
            " ͎",
            " ͓",
            " ͔",
            " ͕",
            " ͖",
            " ͙",
            " ͚",
            " ",
        ]
        self.du = [
            " ̍",
            " ̎",
            " ̄",
            " ̅",
            " ̿",
            " ̑",
            " ̆",
            " ̐",
            " ͒",
            " ͗",
            " ͑",
            " ̇",
            " ̈",
            " ̊",
            " ͂",
            " ̓",
            " ̈́",
            " ͊",
            " ͋",
            " ͌",
            " ̃",
            " ̂",
            " ̌",
            " ͐",
            " ́",
            " ̋",
            " ̏",
            " ̽",
            " ̉",
            " ͣ",
            " ͤ",
            " ͥ",
            " ͦ",
            " ͧ",
            " ͨ",
            " ͩ",
            " ͪ",
            " ͫ",
            " ͬ",
            " ͭ",
            " ͮ",
            " ͯ",
            " ̾",
            " ͛",
            " ͆",
            " ̚",
        ]
        self.dm = [
            " ̕",
            " ̛",
            " ̀",
            " ́",
            " ͘",
            " ̡",
            " ̢",
            " ̧",
            " ̨",
            " ̴",
            " ̵",
            " ̶",
            " ͜",
            " ͝",
            " ͞",
            " ͟",
            " ͠",
            " ͢",
            " ̸",
            " ̷",
            " ͡",
        ]

    def zalgofy(self, text):
        """
        Zalgofy a string
        """

        letters = list(text)
        newWord = ""
        newLetters = []

        for letter in letters:
            a = letter

            if not a.isalpha():
                newLetters.append(a)
                continue

            numAccents = 0
            numU = random.randint(self.numAccentsUp[0], self.numAccentsUp[1])
            numD = random.randint(self.numAccentsDown[0], self.numAccentsDown[1])
            numM = random.randint(self.numAccentsMiddle[0], self.numAccentsMiddle[1])
            while numAccents < self.maxAccentsPerLetter and numU + numM + numD != 0:
                randint = random.randint(0, 2)
                if randint == 0:
                    if numU > 0:
                        a = self.combineWithDiacritic(a, self.du)
                        numAccents += 1
                        numU -= 1
                elif randint == 1:
                    if numD > 0:
                        a = self.combineWithDiacritic(a, self.dd)
                        numD -= 1
                        numAccents += 1
                else:
                    if numM > 0:
                        a = self.combineWithDiacritic(a, self.dm)
                        numM -= 1
                        numAccents += 1

            newLetters.append(a)

        newWord = "".join(newLetters)
        return newWord

    def combineWithDiacritic(self, letter, diacriticList):
        """
        Combines letter and a random character from diacriticList
        """
        return (
            letter.strip()
            + diacriticList[random.randrange(0, len(diacriticList))].strip()
        )


if __name__ == "__main__":
    z = zalgo()
    z.numAccentsUp = (10, 33)
    z.numAccentsDown = (10, 33)
    z.numAccentsMiddle = (10, 33)
    z.maxAccentsPerLetter = 40

    print(z.zalgofy("Test text"))
