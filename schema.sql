
CREATE TABLE IF NOT EXISTS sindicos (
    id_sindico INTEGER PRIMARY KEY,
    nome_sindico TEXT NOT NULL,
    cpf_sindico INTEGER NOT NULL UNIQUE,
    telefone_sindico INTEGER
);

CREATE TABLE  IF NOT EXISTS condominio (
    id_condominio INT PRIMARY KEY NOT NULL,
    cnpj_condominio INT NOT NULL UNIQUE,
    endereco_condominio TEXT,
    id_sindico INT, 
    FOREIGN KEY (id_sindico) REFERENCES sindicos(id_sindicos)
   );