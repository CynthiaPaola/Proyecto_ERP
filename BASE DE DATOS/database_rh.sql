CREATE DATABASE RH;
USE RH;

CREATE TABLE Estados(
    idEstado INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    siglas VARCHAR(10) NOT NULL,
    estatus CHAR NOT NULL,
    CONSTRAINT uk_estados UNIQUE (idEstado, nombre, siglas),
    CONSTRAINT chk_estatus CHECK (estatus='A' OR estatus='I'),
    CONSTRAINT pk_estados PRIMARY KEY (idEstado)
);



CREATE TABLE Ciudades(
    idCiudad INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    idEstado INT NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_ciudades UNIQUE (idCiudad, nombre),
    CONSTRAINT chk_estatus_ciudad CHECK (estatus='A' OR estatus='I'),
    CONSTRAINT pk_ciudades PRIMARY KEY (idCiudad),
    CONSTRAINT fk_ciudades_estado FOREIGN KEY (idEstado) REFERENCES Estados (idEstado)
);


CREATE TABLE Sucursales (
    idSucursal INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    direccion VARCHAR(80) NOT NULL,
    colonia VARCHAR(50) NOT NULL,
    codigoPostal VARCHAR(5) NOT NULL,
    presupuesto FLOAT NOT NULL,
    estatus CHAR NOT NULL,
    idCiudad INT NOT NULL,
    CONSTRAINT uk_sucursales UNIQUE (idSucursal, nombre),
    CONSTRAINT chk_estatus_sucursales CHECK (estatus='A' or estatus='I'),
    CONSTRAINT pk_sucursales PRIMARY KEY (idSucursal),
    CONSTRAINT fk_sucursales_ciudades FOREIGN KEY (idCiudad) REFERENCES Ciudades (idCiudad)
);

CREATE TABLE Turnos (
    idTurno INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(20) NOT NULL,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    dias  VARCHAR(30) NOT NULL,
	CONSTRAINT uk_turnos UNIQUE (idTurno),
    CONSTRAINT pk_turnos PRIMARY KEY (idTurno)
);

CREATE TABLE Departamentos (
    idDepartamento INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_departamentos UNIQUE (idDepartamento, nombre),
    CONSTRAINT chk_estatus_departamentos CHECK (estatus='A' OR estatus='I'),
    CONSTRAINT pk_departamentos  PRIMARY KEY (idDepartamento)
);


CREATE TABLE Percepciones (
    idPercepcion INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    diasPagar INT NOT NULL,
    CONSTRAINT uk_percepciones UNIQUE (idPercepcion, nombre),
    CONSTRAINT pk_percepciones PRIMARY KEY (idPercepcion)
);

CREATE TABLE Deducciones (
    idDeduccion INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    descripcion VARCHAR(80) NOT NULL,
    porcentaje FLOAT NOT NULL,
	CONSTRAINT uk_deducciones UNIQUE (idDeduccion, nombre),
    CONSTRAINT pk_deducciones PRIMARY KEY (idDeduccion)
);


CREATE TABLE Periodos (
    idPeriodo INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    estatus CHAR NOT NULL,
    CONSTRAINT uk_periodos UNIQUE (idPeriodo, nombre),
    CONSTRAINT chk_estatus_periodos CHECK (estatus='A' OR estatus='I'),
	CONSTRAINT chk_fechas_periodos CHECK (fechaFin >= fechaInicio),
    CONSTRAINT pk_periodos PRIMARY KEY (idPeriodo)
);

CREATE TABLE FormasPago (
    idFormaPago  INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_formasPago UNIQUE (idFormaPago, nombre),
    CONSTRAINT chk_estatus_formas_pago CHECK (estatus='A' OR estatus='I'),
    CONSTRAINT pk_formasPago PRIMARY KEY (idFormaPago)
);

CREATE TABLE Puestos (
    idPuesto INT  AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    salarioMinimo FLOAT NOT NULL,
    salarioMaximo FLOAT NOT NULL,
    estatus CHAR NOT NULL,
	CONSTRAINT uk_puestos UNIQUE (idPuesto, nombre),
    CONSTRAINT chk_estatus_puestos CHECK (estatus='A' OR estatus='I'),
	CONSTRAINT chk_salario_puestos CHECK (salarioMaximo > salarioMinimo),
    CONSTRAINT pk_puestos PRIMARY KEY (idPuesto)
);

CREATE TABLE Empleados (
    idEmpleado INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    apellidoPaterno VARCHAR(30) NOT NULL,
    apellidoMaterno VARCHAR(30) NOT NULL,
    sexo CHAR NOT NULL,
    fechaNacimiento DATE NOT NULL,
    curp VARCHAR(20) NOT NULL,
    estadoCivil VARCHAR(20) NOT NULL,
    fechaContratacion DATE NOT NULL,
    salarioDiario FLOAT,
    nss VARCHAR(11),
    diasVacaciones INT NOT NULL,
    diasPermiso INT NOT NULL,
    fotografia MEDIUMBLOB NOT NULL,
    direccion VARCHAR (80) NOT NULL,
    colonia VARCHAR (50) NOT NULL,
    codigoPostal VARCHAR (5) NOT NULL,
    escolaridad VARCHAR (80) NOT NULL,
    especialidad VARCHAR (100) NOT NULL, 
    email VARCHAR(100) NOT NULL,
    contraseña VARCHAR(20) NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    estatus CHAR NOT NULL,
    idDepartamento INT NOT NULL,
    idPuesto INT NOT NULL,
    idCiudad INT NOT NULL,
    idSucursal INT NOT NULL,
    idTurno INT NOT NULL,
	CONSTRAINT uk_empleados UNIQUE (idEmpleado, curp, nss, email ),
    constraint chk_empleados_nss CHECK (nss LIKE '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'),
    CONSTRAINT chk_estatus_empleados CHECK (estatus='A' OR estatus='I'),
    CONSTRAINT pk_empleados PRIMARY KEY (idEmpleado),
    CONSTRAINT fk_empleados_ciudades FOREIGN KEY (idCiudad) REFERENCES Ciudades (idCiudad),
    CONSTRAINT fk_empleados_turnos FOREIGN KEY (idTurno) REFERENCES Turnos (idTurno),
    CONSTRAINT fk_empleados_departamentos FOREIGN KEY (idDepartamento) REFERENCES Departamentos (idDepartamento),
    CONSTRAINT fk_empleados_puestos FOREIGN KEY (idPuesto) REFERENCES Puestos (idPuesto),
    CONSTRAINT fk_empleados_sucursales FOREIGN KEY (idSucursal) REFERENCES Sucursales (idSucursal)
);

CREATE TABLE HistorialPuestos (
    idEmpleado INT AUTO_INCREMENT NOT NULL,
    idPuesto INT NOT NULL,
    idDepartamento INT NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    CONSTRAINT chk_fecha CHECK (fechaFin > fechaInicio),
    CONSTRAINT pk_historial_puestos PRIMARY KEY (idEmpleado, idPuesto, idDepartamento, fechaInicio),
    CONSTRAINT fk_historial_puestos_puestos FOREIGN KEY (idPuesto) REFERENCES Puestos (idPuesto),
    CONSTRAINT fk_historial_puestos_empleados FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado),
    CONSTRAINT fk_historial_puestos_departamentos FOREIGN KEY (idDepartamento) REFERENCES Departamentos (idDepartamento)
);

CREATE TABLE Asistencias (
    idAsistencia INT AUTO_INCREMENT NOT NULL,
    fecha DATE NOT NULL,
    horaEntrada TIMESTAMP NOT NULL,
    horaSalida TIMESTAMP NOT NULL,
    dia VARCHAR(10) NOT NULL,
    idEmpleado INT NOT NULL,
    CONSTRAINT pk_asistencias PRIMARY KEY (idAsistencia),
    CONSTRAINT fk_asistencias_empleados FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE AusenciaJustificada (
    idAusencia INT  AUTO_INCREMENT NOT NULL,
    fechaSolicitud DATE NOT NULL,
    fechaInicio DATE NOT NULL,
    fechaFin DATE NOT NULL,
    tipo CHAR NOT NULL,
    idEmpleadoSolicita INT NOT NULL,
    idEmpleadoAutoriza INT NOT NULL,
    evidencia BLOB NOT NULL,
    estatus CHAR NOT NULL,
    motivo VARCHAR(100),
	CONSTRAINT chk_estatus_ausencia CHECK (estatus='A' OR estatus='I'),
    CONSTRAINT chk_empleadosdif CHECK (idEmpleadoSolicita != idEmpleadoAutoriza),
    CONSTRAINT pk_ausencia_justificada PRIMARY KEY (idAusencia),
    CONSTRAINT fk_ausencia_justificada_empleados_2 FOREIGN KEY (idEmpleadoAutoriza) REFERENCES Empleados (idEmpleado),
    CONSTRAINT fk_ausencia_justificada_empleados FOREIGN KEY (idEmpleadoSolicita) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE DocumentacionEmpleado (
    idDocumento INT AUTO_INCREMENT NOT NULL,
    nombre VARCHAR(60) NOT NULL,
    fechaEntrega DATE NOT NULL,
    documento BLOB NOT NULL,
    idEmpleado INT NOT NULL,
    CONSTRAINT pk_documentacion PRIMARY KEY (idDocumento),
    CONSTRAINT fk_documentacion_empleado FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE Nominas (
    idNomina INT AUTO_INCREMENT NOT NULL,
    fechaElaboracion DATE NOT NULL,
    fechaPago DATE NOT NULL,
    subtotal FLOAT NOT NULL,
    retenciones FLOAT NOT NULL,
    total FLOAT NOT NULL,
    diasTrabajados INT NOT NULL,
    estatus CHAR NOT NULL,
    idEmpleado INT NOT NULL,
    idFormaPago INT NOT NULL,
    idPeriodo INT NOT NULL,
    CONSTRAINT chk_estatus_nomina CHECK (estatus='P' OR estatus='D'),
    CONSTRAINT pk_nominas PRIMARY KEY (idNomina),
    CONSTRAINT fk_nominas_formas_pago FOREIGN KEY (idFormaPago) REFERENCES FormasPago (idFormaPago),
    CONSTRAINT fk_nominas_periodos FOREIGN KEY (idPeriodo) REFERENCES Periodos (idPeriodo),
    CONSTRAINT fk_nominas_empleados FOREIGN KEY (idEmpleado) REFERENCES Empleados (idEmpleado)
);

CREATE TABLE NominasPercepciones (
    idNomina INT AUTO_INCREMENT NOT NULL,
    idPercepcion INT NOT NULL,
    importe FLOAT NOT NULL,
    CONSTRAINT pk_nominas_percepciones PRIMARY KEY (idPercepcion, idNomina),
    CONSTRAINT fk_nominas_percepciones_nominas FOREIGN KEY (idNomina) REFERENCES Nominas (idNomina),
    CONSTRAINT fk_nominas_percepciones_percepciones FOREIGN KEY (idPercepcion) REFERENCES Percepciones (idPercepcion)
);

CREATE TABLE NominasDeducciones (
    idNomina INT AUTO_INCREMENT NOT NULL,
    idDeduccion INT NOT NULL,
    importe FLOAT NOT NULL,
    CONSTRAINT pk_nominas_deducciones PRIMARY KEY (idDeduccion, idNomina),
    CONSTRAINT fk_nominas_deducciones_nominas FOREIGN KEY (idNomina) REFERENCES Nominas (idNomina),
    CONSTRAINT fk_nominas_deducciones_deducciones FOREIGN KEY (idDeduccion) REFERENCES Deducciones (idDeduccion)
);