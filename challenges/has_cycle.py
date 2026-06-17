def has_cycle(graph: dict[str, list[str]]) -> bool:
    
    estado_no = {no: 0 for no in graph}
    
    def possui_ciclo(no_atual: str) -> bool:
        if estado_no[no_atual] == 1:
            return True
        if estado_no[no_atual] == 2:
            return False
        estado_no[no_atual] = 1 

        for vizinho_no in graph.get(no_atual, []):
            if possui_ciclo(vizinho_no):
                return True
        
        estado_no[no_atual] = 2
        return False
    
    for no in graph:
        if estado_no[no] == 0:
            if possui_ciclo(no):
                return True
    return False

