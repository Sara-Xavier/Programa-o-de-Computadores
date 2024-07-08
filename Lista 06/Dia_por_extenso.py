def dia(dia, mes, ano):
    # Verificação de validade da data
    if not (1 <= mes <= 12):
        return "Data Invalida"
    
    if mes in [1, 3, 5, 7, 8, 10, 12] and not (1 <= dia <= 31):
        return "Data Invalida"
    elif mes in [4, 6, 9, 11] and not (1 <= dia <= 30):
        return "Data Invalida"
    elif mes == 2 and not (1 <= dia <= 28):
        return "Data Invalida"
    
    # Formatação da data por extenso
    meses = [
        "janeiro", "fevereiro", "marco", "abril", "maio", "junho",
        "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
    ]
    
    if 1 <= dia <= 31 and 1 <= mes <= 12 and -10000 <= ano <= 10000:
        return f"{dia:02d} de {meses[mes - 1]} de {ano}"
    else:
        return "Data Invalida"