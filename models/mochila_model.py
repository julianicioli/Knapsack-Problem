import MySQLdb

class MochilaModel:
    def __init__(self):
        # Defina as credenciais do seu banco MySQL local aqui
        self.config = {
            'host': 'localhost',
            'user': 'root',       
            'passwd': '',        
            'db': 'knapsack_bd' 
        }

    def resolver_knapsack(self, capacidade_maxima, itens):
        """
        Algoritmo 0/1 Knapsack (Mochila) usando Programação Dinâmica.
        Recebe a capacidade máxima (peso) e a lista de itens.
        """
        n = len(itens)
        W = int(capacidade_maxima)
        
        # Cria a tabela de memorização (DP Table)
        K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                # Se o peso do item atual é menor ou igual à capacidade parcial 'w'
                elif int(float(itens[i-1]['peso'])) <= w:
                    peso_item = int(float(itens[i-1]['peso']))
                    valor_item = int(float(itens[i-1]['valor']))
                    
                    K[i][w] = max(
                        valor_item + K[i-1][w - peso_item], 
                        K[i-1][w]
                    )
                else:
                    K[i][w] = K[i-1][w]

        # Reconstrói a solução para descobrir quais itens foram selecionados
        res = K[n][W]
        w = W
        itens_escolhidos = []
        
        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i-1][w]:
                continue
            else:
                itens_escolhidos.append(itens[i-1])
                res -= int(float(itens[i-1]['valor']))
                w -= int(float(itens[i-1]['peso']))

        # Retorna o Valor Total Ótimo e a lista de dicionários dos itens que devem subir no caminhão
        return K[n][W], itens_escolhidos

    def salvar_no_banco(self, dados_transporte, itens_selecionados):
        """Grava os dados da tela e o resultado do algoritmo nas tabelas do MySQL"""
        db = MySQLdb.connect(**self.config)
        cursor = db.cursor()
        
        try:
            # 1. Insere o veículo/transporte
            sql_transporte = """
                INSERT INTO transportes 
                (motorista_nome, veiculo_placa, veiculo_tipo, tipo_carga_permitida, 
                 dimensao_comprimento, dimensao_largura, dimensao_altura, capacidade_maxima_kg) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql_transporte, (
                dados_transporte['motorista'], dados_transporte['placa'], dados_transporte['tipo'],
                dados_transporte['carga'], dados_transporte['comprimento'], dados_transporte['largura'],
                dados_transporte['altura'], dados_transporte['capacidade']
            ))
            transporte_id = cursor.lastrowid # Pega o ID gerado automaticamente

            # 2. Insere a viagem/carregamento vinculado ao transporte
            sql_carregamento = """
                INSERT INTO carregamentos 
                (transporte_id, destino, horario_saida, horario_chegada, observacoes) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql_carregamento, (
                transporte_id, dados_transporte['destino'], dados_transporte['saida'],
                dados_transporte['chegada'], dados_transporte['observacoes']
            ))
            carregamento_id = cursor.lastrowid

            # 3. Insere apenas os itens que o algoritmo selecionou
            sql_item = """
                INSERT INTO itens_estoque (carregamento_id, nome, peso_kg, valor_rs) 
                VALUES (%s, %s, %s, %s)
            """
            for item in itens_selecionados:
                # Como no HTML você tem quantidade, salvamos cada unidade individualmente se selecionada
                qtd = int(item.get('quantidade', 1))
                for _ in range(qtd):
                    cursor.execute(sql_item, (
                        carregamento_id, item['tipo'], item['peso'], item['valor']
                    ))
            
            db.commit()
            return True
        except Exception as e:
            db.rollback()
            print(f"Erro ao salvar no banco: {e}")
            return False
        finally:
            db.close()