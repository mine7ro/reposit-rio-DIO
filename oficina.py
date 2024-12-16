-- MODELAGEM DE DADOS PARA UMA OFICINA MECÂNICA

-- Tabela Cliente
CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    tipo_cliente ENUM('PF', 'PJ') NOT NULL, -- Pessoa Física ou Jurídica
    documento VARCHAR(14) NOT NULL UNIQUE, -- CPF ou CNPJ
    telefone VARCHAR(20),
    email VARCHAR(255),
    endereco VARCHAR(255)
);

-- Tabela Veículo
CREATE TABLE Veiculo (
    id_veiculo INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    marca VARCHAR(50) NOT NULL,
    modelo VARCHAR(50) NOT NULL,
    ano INT NOT NULL,
    placa VARCHAR(10) NOT NULL UNIQUE,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela Serviço
CREATE TABLE Servico (
    id_servico INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);

-- Tabela Ordem de Serviço
CREATE TABLE OrdemServico (
    id_ordem INT AUTO_INCREMENT PRIMARY KEY,
    id_veiculo INT NOT NULL,
    data_abertura DATETIME NOT NULL,
    data_conclusao DATETIME,
    status ENUM('Aberta', 'Em Andamento', 'Concluída', 'Cancelada') NOT NULL,
    total DECIMAL(10, 2),
    FOREIGN KEY (id_veiculo) REFERENCES Veiculo(id_veiculo)
);

-- Tabela Itens da Ordem de Serviço
CREATE TABLE ItensOrdemServico (
    id_item INT AUTO_INCREMENT PRIMARY KEY,
    id_ordem INT NOT NULL,
    id_servico INT NOT NULL,
    quantidade INT NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_ordem) REFERENCES OrdemServico(id_ordem),
    FOREIGN KEY (id_servico) REFERENCES Servico(id_servico)
);

-- Tabela Funcionário
CREATE TABLE Funcionario (
    id_funcionario INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    cargo VARCHAR(50) NOT NULL,
    salario DECIMAL(10, 2),
    telefone VARCHAR(20),
    email VARCHAR(255)
);

-- Tabela Funcionários na Ordem de Serviço
CREATE TABLE OrdemFuncionario (
    id_ordem INT NOT NULL,
    id_funcionario INT NOT NULL,
    PRIMARY KEY (id_ordem, id_funcionario),
    FOREIGN KEY (id_ordem) REFERENCES OrdemServico(id_ordem),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);
