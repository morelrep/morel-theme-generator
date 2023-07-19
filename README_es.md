# Instrucciones para instalar el tema

## Básico

- Forkea el repositorio. Es decir, crea una copia en tu cuenta [Github](github.com).
- Abre el terminal de tu sistema en el folder de tu computadora local donde trabajarás el sitio (Mac y Linux tienen terminales nativos. Para Windows,tendrás que emplear el [WLS](https://learn.microsoft.com/en-us/windows/wsl/install)
- Corre `$ git clone http://febr3s.github.io/morel-site-generator` para clonar el repositorio
- Corre `$ cd morel-site-generator` para moverte a la carpeta del repositorio
- Corre `$ bundle update` para actualizar el tema y sus dependencias. Si no tienes Ruby en tu sistema, sigue las instrucciones de [Jekyll](https://jekyllrb.com/docs/ruby-101/)
- Abre el archivo `config.yml`y:
  - Descomenta (borra el signo "#") de la línea `#theme: morel-theme`
  - Comenta (añade el signo "#") a la línea `remote_theme: ferbr3s/morel-theme`
- Corre `$ bundle exec jekyll serve` para correr el sitio de prueba

## Personalizar

Ahora tienes en tu computadora local un sitio listo *con el contenido de sample, del sitio MOREL Afro Latin American Writers in Translation (ALAWiT)*. Puedes correrlo localmente para probar con `$ bundle exec jekyll serve`. 

Para llenarlo con los datos de tu sitio, sigue los siguientes pasos:

- Abre _config.yml en tu editor de texto y asígnale a tu sitio:
  - El `título` a tu sitio
  - El `tagline` a tu sitio
  - El `email` y/o cuentas de social media a tu sitio
  - La `description`
  - El `jotform` link (crea tu cuenta gratuita en https://www.jotform.com/)
- Sustituye los archivos de logo, trama y de avatar añadiendo un archivo a:
  - `assets/img/tema/logo.png`
  - `assets/img/tema/avatar.jpg`
  - `assets/img/tema/trama.png`
- Abre el archivo `podcast.md` y cambia el título y el tagline de tu podcast o blog
- La carpeta `_posts` tiene los posts de MOREL. Borra los posts de MOREL y crea los tuyos con la nomenclatura de Jekyll. Si no quieres agregar posts ni episodios de podcast a tu sitio cambia en `_config.yml` el valor `podcast` a `false`

## Generando el contenido a partir de Zotero

- Corre `$ jekyll build` para importar a la carpeta _sites los generadores de contenido actualizados
- Corre `$ unzip -d ./assets/ ./_site/assets/env.zip` para actualizar el ambiente de Python que genera los contenidos
- Abre Zotero y Revisa la [guía](#zotero-fields) para hacer las fichas legibles para MOREL
- Exporta tu colección de Zotero como `csv`. Si no sabes cómo hacerlo sigue las instrucciones [aquí](https://www.zotero.org/support/kb/exporting). 
- Nombra tu archivo `csv` como `books_zotero.csv`. Sustituye el archivo del mismo nombre que se encuentra en la carpeta `assets/data`.
- Corre `$ cd assets/env/bin` para ir a la carpeta donde se activa el ambiente Python
- `$ source activate`
- Corre `$ cd ../src` para moverte a la carpeta donde están los scripts de Python
- Corre `$ python morel-generate` para generar el contenido a partir de tu colección de Zotero
- Corre `$ bundle exec jekyll serve --livereload` para activar el servidor local para navegar 
- Abre el navegador y ve al link proporcionado por el servidor local (generalmente es http://127.0.0.1:4000) 
- ¡Navega tu sitio personalizado!

## Para publicar (deploy)

- Para publicar en Github, sigue sus [instrucciones](https://docs.github.com/en/pages/quickstart) (ignora el paso de "Nuevo repositorio" pues estás trabajando con tu fork de MOREL)
- Para publicar con un third party, sigue las [instrucciones](https://jekyllrb.com/docs/deployment/third-party/) de Jekyll
- Para publicar en tu servidor personal sigue las [instrucciones](https://jekyllrb.com/docs/deployment/manual/) de Jekyll

## Para instalar el tema como Ruby gem local, o sin código

Estamos trabajando en las instrucciones y utilidades para facilitar estas posibilidades. Suscríbete a alguno de nuestros canales para mantenerte actualizado:

- [Twitter](https://twitter.com/morelrep)
- Boletín de correo electrónico
<!-- <script id="mcjs">!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document,"script","https://chimpstatic.com/mcjs-connected/js/users/8aec37d971cdc280e8f9eb567/1a19782d38e75f439e3d5a1fd.js");</script>-->
- [Facebook](https://www.facebook.com/morelrep)

## Zotero fields {#zotero-fields}

Los ítems de MOREL se agregan del mismo modo que se agregan los ítems en cualquier [biblioteca Zotero](https://www.zotero.org/support/adding_items_to_zotero). En su versión actual, MOREL solo puede procesar los ítems de tipo `book`. Dado que no todos los campos necesarios para MOREL están disponibles para el tipo de contenido `book`, hay que hacer tener presente algunas consideraciones:

- Excerpt: el fragmento que se lee en cada registro MOREL corresponde a las `notes` de Zotero (mira la [documentación] de las notas (https://www.zotero.org/support/notes) de Zotero). En su versión actual, MOREL *solo acepta un excerpt por libro*.
- Portada: la portada es un archivo jpg que se añade como `attachment` al ítem de Zotero (mira la [documentación](https://www.zotero.org/support/attaching_files) de los adjuntos de Zotero).
- Traducción u original: para poder filtrar libros traducidos de originales, MOREL emplea el campo "Serie" de Zotero para indicar si es una traducción con el signo `tr`.
- Primera edición: MOREL usa el campo `date` para la fecha de publicación del libro y el campo `edition` para la fecha de primera edición
- Nacionalidad: para indicar la nacionalidad de los autores MOREL emplea el campo `aditional`