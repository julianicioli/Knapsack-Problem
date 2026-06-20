-- 1. Tabela de Vínculo do Transporte (Motorista e Veículo)
CREATE TABLE transportes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    motorista_nome VARCHAR(150) NOT NULL,
    veiculo_placa VARCHAR(10) NOT NULL, 
    -- No MySQL, declaramos o ENUM diretamente na coluna
    veiculo_tipo ENUM('carro', 'van', 'caminhao') NOT NULL,
    tipo_carga_permitida ENUM('perecivel', 'nao-perecivel', 'fragil') NOT NULL,
    dimensao_comprimento NUMERIC(6,2) NOT NULL, 
    dimensao_largura NUMERIC(6,2) NOT NULL,     
    dimensao_altura NUMERIC(6,2) NOT NULL,      
    capacidade_maxima_kg NUMERIC(10,2) NOT NULL,
    -- Sintaxe de data/hora corrigida para o padrão MySQL
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 2. Tabela de Carregamento / Viagem
CREATE TABLE carregamentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    transporte_id INT NOT NULL,
    destino VARCHAR(255) NOT NULL,
    horario_saida TIME NOT NULL,
    horario_chegada TIME NOT NULL,
    observacoes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT fk_carregamento_transporte 
        FOREIGN KEY (transporte_id) 
        REFERENCES transportes(id) 
        ON DELETE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 3. Tabela de Itens do Estoque
CREATE TABLE itens_estoque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    carregamento_id INT NOT NULL,
    nome VARCHAR(150) NOT NULL,
    peso_kg NUMERIC(10,2) NOT NULL,
    valor_rs NUMERIC(10,2) NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_item_carregamento 
        FOREIGN KEY (carregamento_id) 
        REFERENCES carregamentos(id) 
        ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;