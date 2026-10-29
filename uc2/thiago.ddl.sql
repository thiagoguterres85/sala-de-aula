CREATE TABLE IF NOT EXISTS cliente (
	id_cliente SERIAL PRIMARY KEY,
	nome VARCHAR(100) NOT NULL,
	email VARCHAR(50),
	telefone VARCHAR(40)
);
CREATE TABLE IF NOT EXISTS quadra (
    id_quadra SERIAL PRIMARY KEY, 
	preco NUMERIC(5,2) NOT NULL,
	coberta BOOLEAN
);CREATE TABLE IF NOT EXISTS partida (
    id_partida INTEGER PRIMARY KEY,
	nome_artilheiro VARCHAR(100),
	total_gols INTEGER  
);
CREATE TABLE IF NOT EXISTS agendamento (
    id_agendamento INTEGER REFERENCES cliente(id_cliente),
	id_quadra INTEGER REFERENCES quadra(id_quadra),
	id_partida INTEGER REFERENCES partida(id_partida),
	hora timestamp,
	tempo_termino_max INTEGER
);
