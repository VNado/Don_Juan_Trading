import os
class User():
    @classmethod
    def crear_html(nombre, descripcion, precio):
        file=open('test.html', 'w')

        contenido = """ {% extends 'layout2.html' %}
{% block title %}
    <title>Don Juan Trading: Sangre de Indio</title>
{% endblock %}
{% block main %}
    <main class="contenedor">
        <div class="producto">
            <img class="producto__imagen" src="{{ url_for('static', filename='img/mezcal_01.png') }}" alt="imagen mezcal">

            <div class="producto__contenido">
                <h3 class="producto__nombre">"""+nombre+"""</h3>
                <p class="producto__descripcion">"""+descripcion+"""</p>
                <p class="producto__precio">"""+precio+"""</p>

                <form class="producto__formulario">
                    <label class="producto__label">Cantidad:</label>
                    <p></p>
                    <select class="producto__cantidad">
                        <option value="">-- Seleccione --</option>
                        <option value="1">1</option>
                        <option value="2">2</option>
                        <option value="3">3</option>
                        <option value="4">4</option>
                        <option value="5">5</option>
                        <option value="6">6</option>
                        <option value="7">7</option>
                        <option value="8">8</option>
                        <option value="9">9</option>
                        <option value="10">10</option>
                    </select>

                    <input
                        type="submit"
                        class="producto__agregar-carrito"
                        value="Agregar al Carrito"
                    >
                </form>
            </div>
        </div><!--./producto-->
    </main>
{% endblock %}
"""

        file.write(contenido)
        file.close()