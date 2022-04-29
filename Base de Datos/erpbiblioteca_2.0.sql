create database erpbiblioteca;
use erpbiblioteca;
create table Usuarios(
	idUsuarios int auto_increment not null,
    nodedocumento int not null,
	nombreCompleto varchar (45) not null,
    appaterno varchar(45) not null,
	apmaterno varchar(45) not null,
    sexo boolean not null,
	direccion varchar(45) not null,
	telefono char(15) not null,
	email varchar(45) not null,
	constraint fk_Usuarios primary key(idUsuarios),
	constraint uk_email unique (email),
	constraint uk_telefono unique (telefono)
);
create table Bibliotecario(
	idBibliotecario int AUTO_INCREMENT not null,
	idUsuarios int not null,
	nombre varchar(45) not null,
	password_hash varchar(45) not null,
	tipo int not null,
	estado int not null,
	horario_trabajo int not null,
	constraint fk_Bibliotecario primary key(idBibliotecario),
    constraint fk_Bibliotecario_Usuarios foreign key (idUsuarios) references Usuarios (idUsuarios)
);
create table Historial(
	idHistorial int AUTO_INCREMENT not null,
	idBibliotecario int not null,
	fecha date not null,
	horaentrada datetime not null,
	horasalida datetime not null,
	constraint fk_Historial primary key (idHistorial),
    constraint fk_Historial_Bibliotecario foreign key (idBibliotecario) references Bibliotecario (idBibliotecario)
);
create table Prestamo(
	idPrestamo int AUTO_INCREMENT not null,
	idUsuarios int not null,
	idBibliotecario int not null,
	fechaprestamo datetime not null,
	fechadevolucion datetime not null,
	estatus int not null,
	constraint fk_Prestamo primary key (idPrestamo),
	constraint fk_Prestamo_Usuarios foreign key(idUsuarios) references Usuarios (idUsuarios),
	constraint fk_Prestamo_Bibliotecario foreign key(idBibliotecario) references Bibliotecario(idBibliotecario)
);
create table CatalogoMultas(
	idCatalogoMultas int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	descripcion varchar(140) not null,
	precio float not null,
	estatus int not null,
	constraint fk_CatalogoMultas primary key(idCatalogoMultas)
);
create table MultasPrestamo(
	idMultasPrestamo int AUTO_INCREMENT not null,
    idCatalogoMultas int not null,
	idPrestamo int not null,
	cantPagar float not null,
	fecha date not null,
	constraint fk_MultasPrestamo primary key(idMultasPrestamo),
    constraint fk_MultasPrestamo_CatalogoMultas foreign key(idCatalogoMultas) references CatalogoMultas(idCatalogoMultas),
	constraint fk_MultasPrestamo_Prestamo foreign key(idPrestamo) references Prestamo(idPrestamo)
);
create table Proveedores(
	idProveedores int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	direccion varchar(45) not null,
	telefono char(15) not null,
	correo varchar(45) not null,
	pais varchar(45) not null,
	constraint fk_Proveedores primary key(idProveedores)
);
create table Pedidos(
	idPedidos int AUTO_INCREMENT not null,
	idBibliotecario int not null,
	idProveedores int not null,
	fecha date not null,
	cantidad int not null,
	totalPagar float not null,
	estatus int not null,
	constraint fk_Pedidos primary key(idPedidos),
	constraint fk_Pedidos_Bibliotecario foreign key(idBibliotecario) references Bibliotecario(idBibliotecario),
	constraint fk_Pedidos_Proveedores foreign key(idProveedores) references Proveedores(idProveedores)
);
create table Membresias(
	idMembresias int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	precio float not null,
	duracion int not null,
    cantidadLibros int not null,
	estatus int not null,
	constraint fk_Membresias primary key(idMembresias)
);
create table UsuariosMembresia(
	idUsuariosMembresia int AUTO_INCREMENT not null,
	idUsuarios int not null,
	idMembresias int not null,
	fechaInicio date not null,
	fechaFin date not null,
	constraint fk_UsuariosMembresia primary key(idUsuariosMembresia),
	constraint fk_UsuariosMembresia_Usuarios foreign key(idUsuarios) references Usuarios(idUsuarios),
	constraint fk_UsuariosMembresia_Membresias foreign key(idMembresias) references Membresias(idMembresias)
);
create table Tarjetas(
	idTarjetas int AUTO_INCREMENT not null,
	idUsuarios int not null,
	noTarjeta char(16) not null,
	saldo float not null,
	banco varchar(50) not null,
	mes int not null,
	año int not null,
	ccv int not null,
	tipo varchar(20) not null,
	constraint fk_Tarjetas primary key(idTarjetas),
	constraint fk_Tarjetas_Usuarios foreign key(idUsuarios) references Usuarios(idUsuarios)
);
create table Venta(
	idVenta int AUTO_INCREMENT not null,
	idTarjetas int not null,
	idUsuarios int not null,
	idBibliotecario int not null,
	fecha date not null,
	total float not null,
	estatus int not null,
	constraint fk_Venta primary key(idVenta),
	constraint fk_Venta_Tarjetas foreign key(idTarjetas) references Tarjetas(idTarjetas),
	constraint fk_Venta_Usuarios foreign key(idUsuarios) references Usuarios(idUsuarios),
	constraint fk_Venta_Bibliotecario foreign key(idBibliotecario) references Bibliotecario(idBibliotecario)
);
create table Autor(
	idAutor int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	pais varchar(45) not null,
	ciudad varchar(45) not null,
	anioNacimiento date not null,
	estudios varchar(45) not null,
	constraint fk_Autor primary key(idAutor)
);
create table Categorias( 
	idCategorias int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	estatus int not null,
	constraint fk_Categorias primary key(idCategorias)
);
create table Editorial(
	idEditorial int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	direccion varchar(45) not null,
	telefono char(15) not null,
	correo varchar(45) not null,
	pais varchar(45) not null,
	constraint fk_Editorial primary key(idEditorial)
);
create table Libros(
	idLibros int AUTO_INCREMENT not null,
	idCategorias int not null,
	idEditorial int not null,
	titulo varchar(60) not null,
	numEdicion int not null,
	numPaginas int not null,
	anioPublicacion date not null,
	precioVenta float not null,
	precioCompra float not null,
	constraint fk_Libros primary key(idLibros),
	constraint fk_Libros_Categorias foreign key(idCategorias) references Categorias(idCategorias),
	constraint fk_Libros_Editorial foreign key(idEditorial) references Editorial(idEditorial)
);
create table LibrosAutor(
	idLibrosAutor int AUTO_INCREMENT not null,
	idLibros int not null,
	idAutor int not null,
	constraint fk_LibrosAutor primary key(idLibrosAutor),
	constraint fk_LibrosAutor_Libros foreign key(idLibros) references Libros(idLibros),
	constraint fk_LibrosAutor_Autor foreign key(idAutor) references Autor(idAutor)
);
create table DetallesPedidos(
    idDetallesPedidos int auto_increment not null,
	idPedidos int not null,
	idLibros int not null,
	cantUnidades int not null,
	precioUnitario float not null,
	subtotal float not null,
	constraint fk_DetallesPedidos primary key(idDetallesPedidos),
	constraint fk_idDetallesPedidos_Pedidos foreign key(idPedidos) references Pedidos(idPedidos),
	constraint fk_idDetallesPedidos_Libros foreign key(idLibros) references Libros(idLibros)
);
create table DetallesPrestamo(
	idDetallesPrestamo int AUTO_INCREMENT not null,
	idPrestamo int not null,
	idLibros int not null,
	fechaDevolucion datetime not null,
	librosPrestados int not null,
	librosEntregados int not null,
    comentario varchar(140) not null,
	constraint fk_DetallesPrestamo primary key(idDetallesPrestamo),
	constraint fk_DetallesPrestamo_Prestamo foreign key(idPrestamo) references Prestamo(idPrestamo),
	constraint fk_DetallesPrestamo_Libros foreign key(idLibros) references Libros(idLibros)
);
create table DetallesVenta(
	idDetallesVenta int AUTO_INCREMENT not null,
	idVenta int not null,
	idLibros int not null,
	cantidad int not null, 
	subtotal float not null,
	constraint fk_DetallesVenta primary key(idDetallesVenta),
	constraint fk_DetallesVenta_Venta foreign key(idVenta) references Venta(idVenta),
	constraint fk_DetallesVenta_Libros foreign key(idLibros) references Libros(idLibros)
);

create table Pais(
	idPais int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	constraint fk_Editorial primary key(idPais)
);
create table Ciudad(
	idCiudad int AUTO_INCREMENT not null,
	nombre varchar(45) not null,
	constraint fk_Editorial primary key(idCiudad)
);

/*Crear un usuario para la conexion con la app*/
drop user user_BibliotecaERP;
create user user_BibliotecaERP identified by 'Bibliotecario';
grant select, insert, update, delete on erpbiblioteca.Autor to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Bibliotecario to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.CatalogoMultas to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Categorias to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.DetallesPedidos to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.DetallesPrestamo to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.DetallesVenta to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Editorial to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Historial to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Libros to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.LibrosAutor to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Membresias to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.MultasPrestamo to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Pedidos to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Prestamo to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Proveedores to user_BibliotecaERP;
grant select, insert, update, delete on erpbiblioteca.Tarjetas to user_BibliotecaERP; 
grant select, insert, update, delete on erpbiblioteca.Usuarios to user_BibliotecaERP; 
grant select, insert, update, delete on erpbiblioteca.UsuariosMembresia to user_BibliotecaERP; 
grant select, insert, update, delete on erpbiblioteca.Venta to user_BibliotecaERP;
