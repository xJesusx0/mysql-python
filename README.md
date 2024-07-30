Claro, aquí tienes un ejemplo de README para tu proyecto. Este archivo proporciona una visión general de la aplicación, cómo instalarla, cómo usarla y otros detalles importantes.

---

# MySQL Command Line Interface

Este proyecto es una interfaz de línea de comandos para interactuar con bases de datos MySQL. Permite ejecutar consultas SQL directamente desde la terminal y muestra los resultados en una tabla formateada utilizando la biblioteca `rich`.

## Requisitos

- Python 3.6 o superior
- MySQL (Opcional si te quieres conectar a una base de datos remota)
- Paquetes Python necesarios

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone https://github.com/xJesusx0/mysql-python.git
    cd https://github.com/xJesusx0/mysql-python.git
    ```

2. **Crea un entorno virtual y actívalo** (opcional pero recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**:

    Crea un archivo `.env` en la raíz del proyecto con la siguiente estructura y llena con los detalles de tu base de datos MySQL:

    ```plaintext
    MYSQL_HOST=localhost
    MYSQL_USER=tu_usuario
    MYSQL_PASSWORD=tu_contraseña
    MYSQL_DB=tu_base_de_datos
    MYSQL_PORT=3306
    ```

## Uso

1. **Ejecuta el programa**:

    ```bash
    python main.py
    ```

2. **Interacción**:

    - **Ejecutar consultas**: Escribe tus consultas SQL y presiona Enter para ejecutarlas. Los resultados se mostrarán en una tabla formateada.
    - **Salir**: Escribe `exit` para cerrar la aplicación.
    - **Limpiar pantalla**: Escribe `clear` para limpiar la pantalla de la consola.

## Ejemplos

- **Mostrar todas las tablas**:

    ```sql
    SHOW TABLES;
    ```

- **Seleccionar datos de una tabla**:

    ```sql
    SELECT * FROM nombre_de_la_tabla;
    ```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para reportar errores o sugerir mejoras, o envía un pull request con tus cambios.

---

### Notas Adicionales

- **Dependencias**: El archivo `requirements.txt` debería incluir las siguientes dependencias, si no está incluido:

    ```plaintext
    pymysql
    rich
    python-dotenv
    ```
