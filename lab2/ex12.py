def groupByRhyme(words: list) -> list:
    rhyme = dict()
    for word in words:
        ending = word[-2:]
        if ending in rhyme:
            groupeOfWords = rhyme.get(ending)
            groupeOfWords = groupeOfWords + " " + word
            rhyme.update({ending : groupeOfWords})
        else:
            rhyme.setdefault(ending, word)

    rhymeList = []
    for group in rhyme:
        groupeOfWords = rhyme.get(group)
        listOfWords = groupeOfWords.split()
        rhymeList.append(listOfWords)
    return rhymeList

print(groupByRhyme(['ana', 'banana', 'mamaie', 'carte', 'arme', 'parte', 'oaie', 'oana']))