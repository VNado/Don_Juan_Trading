// comparar contraseñas
function validarContrasena() {
    var contrasena = document.getElementById("contrasena").value;
    var contrasena2 = document.getElementById("contrasena2").value;
    if (contrasena != contrasena2) {
        alert("Las contraseñas no coinciden");
        contrasena2.focus();
        document.getElementById("contrasena2").value = "";
        document.getElementById("contrasena").value = "";
        document.getElementById("form1").reset();
        return false;
    }
    return true;
}
// validar telefono
function validarTelefono() {
    var telefono = document.getElementById("telefono").value;
    if (telefomnia.length != 10) {
        alert("El telefono debe ser de 10 digitos");
        telefono.focus();
        return false;
    }
    return true;
}