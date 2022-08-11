# PW2-Lab07
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>
<div align="center">
    <span style="font-weight:bold;"><h2>INFORME DE LABORATORIO</h2></span>
</div>


<div align="center">
<table>
<theader>
    <tr><th colspan="6" style="width:50%; height:auto; text-align:center">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td colspan="5">Laboratorio de Programación Web 2</td>
    </tr>
    <tr>
        <td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Api en Django</td>
    </tr>
    <tr>
        <td>NÚMERO DE PRÁCTICA:</td><td>06</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td colspan="2">FECHA DE PRESENTACIÓN:</td><td>03-Jul-2022</td><td colspan="2">HORA DE PRESENTACIÓN:</td><td>23:55</td>
    </tr>
    <tr>
        <td colspan="3">INTEGRANTES:
        <ol>
        <li>Blanco Trujillo, Antony Jacob</li>
        <li>Cahuana Aguilar, Josué Mathías Miguel</li>
        <li>Hancco Velásquez, Jessica Geraldine</li>
        <li>Mayta Nolasco, Oliver Alessandro</li>
        <li>Umasi Cariapaza, Carlos Daniel</li>
        </ol>
        </td>
        <td colspan="2"> NOTA:</td>
        <td>     </td>
    </tr>
    <tr>
        <td colspan="6">DOCENTE:<br>
        Mg. Richart Smith Escobedo Quispe
        </td>
    </tr>
</tdbody>
</table>

<table>
    <theader>
        <tr>
            <th style="text-align:center">SOLUCIÓN Y RESULTADOS</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
            I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS<br>
            <ol>
                <li>Instalacion de "djangorestframework"</li>
                    <ul>
                        <li>Activar el entorno virtal: .\Scripts\activate</li><br>
                        <li>pip install djangorestframework</li>
                        <img src="Inventario_Vidrios/Imagenes/creacionApp.png"><br>              
                    </ul>
                <li>Creación de la api</li>
                    <ul>
                        <li>django-admin startapp api</li>
                        <img src="Inventario_Vidrios/Imagenes/template.png"><br>
                    </ul>
                <li>Creación del modelo</li>
                    <ul>
                        <li>En models.py</li>
                        <img src="djangocrud/imagenes/modelo.png"><br>
                        <li>Registrar en admin.py</li>
                        <img src="djangocrud/imagenes/registro.png"><><br>
                        <li>vim serializer.py</li>
                        <li>Definir lo campos para la api</li>
                        <img src="djangocrud/imagenes/serial.png"><br>
                        <li>Aplicación funcional</li>
                        <img src="Inventario_Vidrios/Imagenes/inicio4.png"><br>
                        <img src="Inventario_Vidrios/Imagenes/inicio5.png"><br>
                        <img src="Inventario_Vidrios/Imagenes/inicio7.png"><br>
                        <img src="Inventario_Vidrios/Imagenes/inicio6.png"><br>
                    </ul>
            </ol>
            </td>
        </tr>
        <tr>
            <td>
            II. SOLUCIÓN DEL CUESTIONARIO<br>
            <ol>
                <li>------</li>
            </ol>
            </td>
        </tr>
        <tr>
            <td>
                III. CONCLUSIONES<br>
                <ul>
                    <li>Para el diseño de la parte Frontend del proyecto, se están utilizando plantillas ya maquetadas listas para importar al proyecto y enfocarnos más en la funcionalidad de los requisitos que debe tener nuestra página web.</li>
                    <li>...</li>
                    <li>...</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>

<table>
    <theader>
        <tr>
            <th style="text-align:center">RETROALIMENTACIÓN GENERAL</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
            </td>
        </tr>
    </tbody>
</table>
<div>

<table>
    <theader>
        <tr>
            <th style="text-align:center">REFERENCIAS Y BIBLIOGRAFÍA</th>
        </tr>
    </theader>
    <tbody>
        <tr>
            <td>
                [1] Escobedo, R., 2022. pw2/labs/lab01 at main · rescobedoq/pw2. [online] GitHub. Available at: https://github.com/rescobedoq/pw2/tree/main/labs/lab01.<br>
                [2] How to manage static files (e.g. images, JavaScript, CSS). Django documentation. Django (2022). Available at: https://docs.djangoproject.com/en/4.0/howto/static-files/.<br>
                [3] How to manage static files (e.g. images, JavaScript, CSS). Documentación de Django. Django (2022). Available at: https://docs.djangoproject.com/es/4.0/howto/static-files/.<br>
                [4] Escribiendo su primera aplicación en Django, parte 6. Documentación de Django. Django (2022). Available at: https://docs.djangoproject.com/es/4.0/intro/tutorial06/.
            </td>
        </tr>
    </tbody>
</table>