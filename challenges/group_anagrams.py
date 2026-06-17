def group_anagrams(words: list[str]) -> list[list[str]]:
    anagrama = {}
    
    for word in words:
        chave = "".join(sorted(word))
        if chave not in anagrama:
            anagrama[chave] = []
        
        anagrama[chave].append(word)
    return list(anagrama.values())

