create database miguelronda_db

create table ususario(
	idusuario int not null auto_increment,
    nome text,
    telefone text,
    usuario text,
    senha text,
    primary key (idusuario)
);