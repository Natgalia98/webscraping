CREATE DATABASE IF NOT EXISTS busca_cursos;
USE busca_cursos;

-- Tabela ADMINISTRADOR
CREATE TABLE administrador
(
    adm_id INT  NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_adm VARCHAR(80) NOT NULL,
    cpf_adm CHAR(11) NOT NULL UNIQUE ,
    senha_adm VARCHAR(20) NOT NULL,
    -- DATETIME é o tipo padrão para data e hora no MySQL
    data_insercao DATETIME NOT NULL, 
    situacao INT NOT NULL
);

-- Tabela PLATAFORMA
CREATE TABLE plataforma
(
    plataforma_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    adm_id INT NOT NULL REFERENCES administrador (adm_id),
    nome_plataforma VARCHAR (80) NOT NULL,
    url_plataforma VARCHAR (255) NOT NULL UNIQUE,
    descricao_plataforma VARCHAR (350) NOT NULL           
);

-- Tabela CATEGORIA
CREATE TABLE categoria
(
    categoria_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(350) NOT NULL,
    data_insercao DATETIME NOT NULL
);

-- Tabela AREACATEGORIA
CREATE TABLE area_categoria(
    area_categoria_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT NOT NULL REFERENCES categoria (categoria_id),
    data_insercao DATETIME NOT NULL,
    situacao INT NOT NULL        
);

-- Tabela CURSO
CREATE TABLE curso
(
    curso_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    area_categoria_id INT NOT NULL REFERENCES area_categoria (area_categoria_id),
    titulo_curso VARCHAR (80) NOT NULL,
    url_curso VARCHAR(255) NOT NULL,
    certificacao VARCHAR(80) NOT NULL,
    -- FLOAT é adequado para o MySQL
    quantidade_horas FLOAT NOT NULL, 
    descricao_curso VARCHAR(350) NOT NULL,
    data_inicio DATETIME NOT NULL,
    nivel_ensino VARCHAR(80) NOT NULL,
    data_insercao DATETIME NOT NULL        
);

-- Tabela USUARIO
CREATE TABLE usuario
(
    usuario_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_usuario VARCHAR(80) NOT NULL,
    email_usuario VARCHAR(80) NOT NULL UNIQUE,
    senha_usuario VARCHAR(80) NOT NULL,
    data_insercao DATETIME NOT NULL,
    situacao INT NOT NULL
);

-- Tabela FEEDBACK
CREATE TABLE feedback
(
    feedback_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL REFERENCES usuario (usuario_id),
    titulo_feedback VARCHAR(80) NOT NULL,
    descricao_feedback VARCHAR(250) NOT NULL,
    avaliacao INT NOT NULL,
    data_publicacao DATETIME NOT NULL,
    comentario VARCHAR(250) NOT NULL        
);

-- Tabela MENTOR
CREATE TABLE mentor
(
    mentor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome_mentor VARCHAR(80) NOT NULL,
    data_insercao DATETIME NOT NULL,
    situacao INT NOT NULL
);

-- Tabela MENTORIA
CREATE TABLE mentoria
(
    mentoria_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    curso_id INT NOT NULL REFERENCES curso (curso_id),
    plataforma_id INT NOT NULL REFERENCES plataforma (plataforma_id),
    mentor_id INT NOT NULL REFERENCES mentor (mentor_id),
    data_insercao DATETIME NOT NULL,
    situacao INT NOT NULL        
);

-- Tabela PLATAFORMACURSO
CREATE TABLE plataforma_curso
(
    plataforma_curso_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    curso_id INT NOT NULL REFERENCES curso (curso_id),
    plataforma_id INT NOT NULL REFERENCES plataforma (plataforma_id)
    -- DATE é o tipo para apenas data no MySQL        
);

-- Tabela HISTORICOUSUARIO
CREATE TABLE historico_usuario
(
    -- Usando AUTO_INCREMENT e corrigindo a referência no CREATE TABLE
    historico_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    data_insercao DATETIME NOT NULL,
    descricao VARCHAR(80) NOT NULL,
    plataforma_curso_id INT NOT NULL REFERENCES plataforma_curso (plataforma_curso_id),
    usuario_id INT NOT NULL REFERENCES usuario (usuario_id),
    curso_id INT NOT NULL REFERENCES curso (curso_id),
    area_categoria_id INT NOT NULL REFERENCES area_categoria (area_categoria_id)        
);
