/*Se manda a llamar el procedimiento que insertará a los bebés recien nacidos*/
call sp_insertar_nacimientos_bebes(100);
SELECT * FROM bd_hospital_210538.api_nacimientosbebes;
/*Se mandan a llamar a las funciones*/
SELECT fn_contar_nacimientos(); /*Cuenta a todos los bebés nacidos año por año*/
SELECT fn_contar_nacimientos_por_tipo(); /*Cuenta a todos los bebés nacidos por Cesarea o Parto Natural*/
/*Se manda a llamar la vista que muestra la fecha de nacimiento, hora de nacimiento y el tipo de nacimiento*/
SELECT * FROM vw_nacimientos;
SELECT * FROM vw_nacimientos_genero;
SELECT * FROM vw_nacimientos_por_ciudad;
/*Limpia la base de datos completamente*/
call sp_limpia_bd("qwerty");
