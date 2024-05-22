INSERT INTO `usuario_cargo`(`cargo_nombre`, `cargo_sueldo_basico`, `cargo_empresa`) VALUES ('CEO','3000000','Globant');
INSERT INTO `usuario_cargo`(`cargo_nombre`, `cargo_sueldo_basico`, `cargo_empresa`) VALUES ('Senior','5000000','Globant');
INSERT INTO `usuario_cargo`(`cargo_nombre`, `cargo_sueldo_basico`, `cargo_empresa`) VALUES ('Junior','4000000','Globant');
INSERT INTO `usuario_cargo`(`cargo_nombre`, `cargo_sueldo_basico`, `cargo_empresa`) VALUES ('Gerente','2000000','Globant');

INSERT INTO `usuario_rol`(`rol_nombre`) VALUES ('Administrador');
INSERT INTO `usuario_rol`(`rol_nombre`) VALUES ('Empleado');

INSERT INTO `usuario_usuario`(`cedula`, `usu_nombre`, `usu_correo`, `usu_telefono`, `password`, `usu_direccion`, `usu_fecha_ingreso`,'usu_estado', `usu_id_cargo_id`, `usu_id_rol_id`) 
VALUES ('123','Adan','adan@gmail.com','123123','1234','calle 123','2024/03/28','activo','1','1')