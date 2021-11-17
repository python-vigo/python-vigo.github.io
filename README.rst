Como publicar un nuevo post
===========================

Se presupone que tenemos el repositorio ya clonado en local, con el entorno virtual creado y las dependencias instaladas.

Además se presupone que si se quiere publicar el post vía "despliegue" se tiene configurado el repositorio local con permisos de escritura en las ramas remotas. Si no es el caso, habrá de hacerse vía pull request para que alguien con permisos haga el despliegue del post.


1. Situarse en la rama src (o crear una rama en base a la rama src si lo que queremos es hacer un pull request porque no tenemos permisos de escritura o queremos que alguien revise antes de publicar)

2. Dentro de la carpeta */posts/* crear un fichero *.rst

   **Si el evento ha de constar en el calendario de VigoTech, el nombre tiene que tener la siguiente estructura**: reunion_del_grupo_*.rst sustituyendo el asterisco por la fecha en formato YYYY-MM-DD (se pueden ver los otros posts ya publicados si no queda claro)

   Cualquier post que no tenga un nombre con esa estructura se considerará un post informativo que no necesita generar "evento" en el calendario de VigoTech.

3. Dentro de ese fichero, ha de usarse formato restructuredText, y contener las siguientes cabeceras::

    .. title: 
    .. slug: 
    .. meeting_datetime: 
    .. date: 
    .. tags: python, vigo, desarrollo
    .. category:
    .. link:
    .. description:
    .. type: text
    .. author: Python Vigo

   Las más importantes son:

   *title*: 
       Aquí pondremos el título que queramos que aparezca en el post publicado

   *slug*:
       Esta es la parte de la URL específica para este post y por tanto ha de ser **única** entre todos los posts, si no puede haber conflictos, por eso se le suele añadir la fecha como en el siguiente ejemplo: reunion-del-grupo-el-20191017

   *meeting_datetime*:
       Esto es MUY importante si el post ha de generar evento, ya que esta fecha es la que se usará como fecha del evento en cuestión. **Su formato ha de ser YYYYMMDD_HHMM**. Por ejemplo: reunion_del_grupo_2019-10-17.rst

   *date*: 
       Esta es la fecha de publicación del post. **Siempre debemos poner una fecha en el pasado**, ya que si ponemos una fecha futura, en el momento de generar la web estática para publicar el post, este no se tendrá en cuenta puesto que todavía no ha llegado la fecha en la que se indica que ha de publicarse.

   Las demás etiquetas pueden dejarse como están o no, pero en principio tienen poca relevancia.


4. Una vez terminamos de editar el fichero y lo hemos guardado, ha de o bien hacerse un pull request o el despliegue.

5. **OJO paso importante** Para publicar el post si se tienen permisos de escritura en la rama remota, hará falta simplemente invocar el comando: **nikola deploy**. Ese comando invoca varios scripts en el orden correcto para generar la web, crear el fichero events.json si fuera necesario y subir los cambios al repositorio remoto.


En un minuto o así, debería de ser visible el post en la web de Python Vigo.
