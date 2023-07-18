# Instrucciones para instalar el tema

## Básico

- Forkea el repositorio. Es decir, crea una copia en tu cuenta [Github](github.com).
- Abre el terminal de tu sistema en el folder de tu computadora local donde trabajarás el sitio (Mac y Linux tienen terminales nativos. Para Windows,tendrás que emplear el (WLS)[LINK])
- Corre `$ git clone [REP]` para clonar el repositorio
- Corre `$ cd morel-site-generator` para moverte a la carpeta del repositorio
- Corre `$ bundle update` para actualizar el tema y sus dependencias. Si no tienes Ruby en tu sistema, sigue las instrucciones de Jekyll[LINK]
- Abre el archivo `config.yml`y:
  - Descomenta (borra el signo "#") de la línea `#theme: morel-theme`
  - Comenta (añade el signo "#") a la línea `remote_theme: ferbr3s/morel-theme`
- Corre `$ bundle exec jekyll serve` para correr el sitio de prueba

## Personalizar

Ahora tienes un sitio listo *con el contenido de sample, del sitio MOREL Afro Latin American Writers in Translation (ALAWiT)*. Puedes correrlo localmente para probar con `$ bundle exec jekyll serve`. Para llenarlo con tu propio contenido de Zotero y los datos de tu sitio, sigue los siguientes pasos:

- Abre _config.yml en tu editor de texto y asígnale a tu sitio:
  - El `título` a tu sitio
  - El `tagline` a tu sitio
  - El `email` y/o cuentas de social media a tu sitio
  - La `description`
  - El `jotform` link (crea tu cuenta gratuita en https://www.jotform.com/)
- Sustituye los archivos de logo y de avatar en:
  - `assets/img/tema/logo.png`
  - `assets/img/tema/avatar.jpg`
- Corre `$ jekyll build` para importar a la carpeta _sites los generadores de contenido actualizados
- Corre `$ unzip -d ./assets/ ./_site/assets/env.zip` para actualizar el ambiente de Python que genera los contenidos
- Abre Zotero y Revisa la [guía](#zotero-fields) para hacer las fichas legibles para MOREL
- Exporta tu colección de Zotero como `csv`. Si no sabes cómo hacerlo sigue las instrucciones (aquí)[link]. 
- Nombra tu archivo `csv` como `books_zotero.csv`. Sustituye el archivo del mismo nombre que se encuentra en la carpeta `assets/data`.
- Corre `$ cd assets/env/bin` para ir a la carpeta donde se activa el ambiente Python
- `$ source activate`
- Corre `$ cd ../src` para moverte a la carpeta donde están los scripts de Python
- Corre `$ python morel-generate` para generar el contenido a partir de tu colección de Zotero
- Corre `$ bundle exec jekyll serve --livereload` para activar el servidor local para navegar 
- Abre el navegador y ve al link proporcionado por el servidor local (generalmente es [SERVIDOR]) 
- ¡Navega tu sitio personalizado!

## Para publicar (deploy)

- Para publicar en Github, sigue sus (instrucciones)[LINK]
- Para publicar con un third party, sigue las (instrucciones)[LINK] de Jekyll
- Para publicar en tu servidor personal sigue las (instrucciones)[LINK] de Jekyll

## Para instalar el tema como Ruby gem local, o sin código

Estamos trabajando en las instrucciones y utilidades para facilitar estas posibilidades. Suscríbete a alguno de nuestros canales para mantenerte actualizado:

- RSS
- Twitter
- Lista de correo electrónico
- Facebook