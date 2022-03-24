create database erpbiblioteca;
use erpbiblioteca;
create table Usuario
(
idUsuario int AUTO_INCREMENT,
nodedocumento int,
nombre varchar(45),
appaterno varchar(45),
apmaterno varchar(45),
sexo varchar(45),
direccion varchar(45),
telefono varchar(45),
email varchar(45),
primary key (idUsuario)
);
create table Bibliotecario
(
idBibliotecario int AUTO_INCREMENT,
idUsuario int,
nombre varchar(45),
password varchar(45),
tipo varchar(45),
estado varchar(45),
horario_turno time,
primary key (idBibliotecario),
foreign key(idUsuario) references Usuario(idUsuario)
);
create table Historial
(
idHistoria int AUTO_INCREMENT,
idBibliotecario int,
fecha datetime,
horaentrada datetime,
horasalida datetime,
primary key (idHistoria),
foreign key(idBibliotecario) references Bibliotecario(idBibliotecario)
);
create table Prestamo
(
idPrestamo int AUTO_INCREMENT,
idUsuario int,
idBibliotecario int,
fechaprestamo datetime,
fechadevolucion datetime,
status int,
primary key (idPrestamo),
foreign key(idUsuario) references Usuario(idUsuario),
foreign key(idBibliotecario) references Bibliotecario(idBibliotecario)
);
create table CatalogoMultas
(
idCatalogoMultas int AUTO_INCREMENT,
nombre varchar(45),
descripcion varchar(45),
precio float,
status int,
primary key(idCatalogoMultas)
);
create table MultasPrestamo
(
idMultasPrestamo int AUTO_INCREMENT,
idPrestamo int,
idCatalogoMultas int,
cantPagar float,
fecha datetime,
primary key(idMultasPrestamo),
foreign key(idPrestamo) references Prestamo(idPrestamo),
foreign key(idCatalogoMultas) references CatalogoMultas(idCatalogoMultas)
);
create table Provedores
(
idProvedor int AUTO_INCREMENT,
nombre varchar(45),
direccion varchar(45),
telefono varchar(45),
correo varchar(45),
pais varchar(45),
primary key(idProvedor)
);
create table Pedidos
(
idPedidos int AUTO_INCREMENT,
idBibliotecario int,
idProvedor int,
fecha date,
cantidad int,
totakPagar float,
status int,
primary key(idPedidos),
foreign key(idBibliotecario) references Bibliotecario(idBibliotecario),
foreign key(idProvedor) references Provedores(idProvedor)
);
create table Membresias
(
idMembresia int AUTO_INCREMENT,
nombre varchar(21),
precio float,
duracion int,
status int,
cantidadLibros int,
primary key(idMembresia)
);
create table Usuarios_membresia
(
idUsuarios_membresia int AUTO_INCREMENT,
idUsuario int,
idMembresia int,
fechaInicio date,
fechaFin date,
primary key(idUsuarios_membresia),
foreign key(idUsuario) references Usuario(idUsuario),
foreign key(idMembresia) references Membresias(idMembresia)
);
create table Tarjetas
(
idTarjeta int AUTO_INCREMENT,
idUsuario int,
noTarjeta varchar(16),
saldo float,
banco varchar(50),
mes int,
año int,
ccv int,
tipo varchar(20),
primary key(idTarjeta),
foreign key(idUsuario) references Usuario(idUsuario)
);
create table Venta
(
idVenta int AUTO_INCREMENT,
idTarjeta int,
idUsuario int,
idBibliotecario int,
fecha date,
total float,
status int,
primary key(idVenta),
foreign key(idTarjeta) references Tarjetas(idTarjeta),
foreign key(idUsuario) references Usuario(idUsuario),
foreign key(idBibliotecario) references Bibliotecario(idBibliotecario)
);
create table Autor
(
idAutor int AUTO_INCREMENT,
nombre varchar(60),
pais varchar(45),
ciudad varchar(45),
anio_nacimiento varchar(45),
estudios varchar(45),
primary key(idAutor)
);
create table Categorias 
(
idCategorias int AUTO_INCREMENT,
nombre varchar(45),
status int,
primary key(idCategorias)
);
create table Editorial
(
idEditorial int AUTO_INCREMENT,
nombre varchar(45),
direccion varchar(45),
telefono varchar(45),
correo varchar(45),
pais varchar(45),
primary key(idEditorial)
);
create table Libros
(
idLibro int AUTO_INCREMENT,
idCategorias int,
idEditorial int,
titulo varchar(50),
numEdiccion int,
numPaginas int,
anio_Publicacion date,
precioVenta float,
precioCompra float,
primary key(idLibro),
foreign key(idCategorias) references Categorias(idCategorias),
foreign key(idEditorial) references Editorial(idEditorial)
);
create table LibrosAutor
(
idLibrosAutor int AUTO_INCREMENT,
idLibro int,
idAutor int,
primary key(idLibrosAutor),
foreign key(idLibro) references Libros(idLibro),
foreign key(idAutor) references Autor(idAutor)
);
create table DetallesPedidos
(
idDetallePedidos int AUTO_INCREMENT,
idPedidos int,
idLibro int,
cantUnidades int,
precioUnitario float,
subtotal float,
primary key(idDetallePedidos),
foreign key(idPedidos) references Pedidos(idPedidos),
foreign key(idLibro) references Libros(idLibro)
);
create table DetallePrestamo
(
idDetallePrestamo int AUTO_INCREMENT,
idPrestamo int,
idLibro int,
fechadevolucion datetime,
Libros_Prestados int,
comentario varchar(124),
librosEntregados int,
primary key(idDetallePrestamo),
foreign key(idPrestamo) references Prestamo(idPrestamo),
foreign key(idLibro) references Libros(idLibro)
);
create table DetalleVenta
(
idDetalleVenta int AUTO_INCREMENT,
idVenta int,
idLibro int,
cantidad int, 
precio float,
subtotal float,
primary key(idDetalleVenta),
foreign key(idVenta) references Venta(idVenta),
foreign key(idLibro) references Libros(idLibro)
)