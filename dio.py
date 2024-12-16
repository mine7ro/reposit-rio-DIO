-- MODELAGEM DE DADOS REFINADA

-- Tabela Cliente
CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    tipo_cliente ENUM('PF', 'PJ') NOT NULL,
    nome VARCHAR(255) NOT NULL,
    documento VARCHAR(14) NOT NULL UNIQUE, -- CPF ou CNPJ dependendo do tipo_cliente
    email VARCHAR(255),
    telefone VARCHAR(20),
    endereco VARCHAR(255)
);

-- Tabela Pagamento
CREATE TABLE Pagamento (
    id_pagamento INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    tipo_pagamento ENUM('Cartão de Crédito', 'Cartão de Débito', 'Boleto', 'Pix', 'Outro') NOT NULL,
    dados_pagamento VARCHAR(255),
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela Pedido
CREATE TABLE Pedido (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    data_pedido DATETIME NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Cliente(id_cliente)
);

-- Tabela Entrega
CREATE TABLE Entrega (
    id_entrega INT AUTO_INCREMENT PRIMARY KEY,
    id_pedido INT NOT NULL,
    status_entrega ENUM('Pendente', 'Em transporte', 'Entregue', 'Cancelada') NOT NULL,
    codigo_rastreio VARCHAR(50),
    data_previsao DATE,
    FOREIGN KEY (id_pedido) REFERENCES Pedido(id_pedido)
);
