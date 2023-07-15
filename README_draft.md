## Instrucciones para instalar el tema como gema

- jekyll new [name-of-your-site]
- cd [name-of-your-site]
- borrar index.markdown [x]
- borrar about.markdown [x]
- borrar _post/2023-07-12-welcome-to-jekyll.markdown [x]
- agregar "morel-theme" a gemfile [x]
- agregar "morel-theme" a _config.yml [x]
- agregar "jekyll-seo-tag" a _config.yml [x]
- agregar "jekyll-seo-tag" a gemfile, en la sección de Jekyll plugins [x]
- $ bundle install # instala el tema y sus dependencias
- $ bundle update # actualiza el tema y sus dependencias a su última versión
- $ jekyll build # construye el sitio básico, e importa a la carpeta _sites los generadores de contenido
- $ COMANDO # descomprime archivo zip que se encuentra en _site/assets y copiar contenido a main folder 
- abre _config.yml en tu editor de texto y:
  - descomenta (borra "#") la línea "theme: morel-theme"
  - asígnale el título a tu sitio
  - asígnale el tagline a tu sitio
  - asígnale datos de contacto y/o redes a tu sitio
  - asígnale el site description a tu sitio
  - asígnale el jotform link a tu sitio (crea tu cuenta gratuita en https://www.jotform.com/)
- $ jekyll build # construye el sitio con su contenido
- $ COMANDO # descomprime el archivo "env.zip", que se encuentra en la carpeta assets que acabamos de copiar a main folder
- Abre Zotero y exporta tu colección de Zotero como csv. Guárdalo en la carpeta assets/data. Nombra el archivo "books_zotero.csv". Revisa la [guía](#zotero-fields) para llenar las fichas de Zotero 100 % legibles para MOREL.
- $ cd assets/env/bin # ve a la carpeta para activar el ambiente Python
- $ source activate
- $ cd ../src # muévete a la carpeta donde están los scripts de Python
- $ python morel-generate # genera el contenido a partir de tu colección de Zotero
- $ bundle exec jekyll serve --livereload # activa el servidor local para navegar tu sitio!

## Instrucciones para instalar el tema como rep

- forkea el repositorio. Es decir, crea una copia en tu cuenta github.
- abre el terminal en el folder de tu computadora local donde trabajarás el sitio
- $ git clone [rep] # clona el repositorio
- $ cd morel-site-generator # te mueves a la carpeta del repositorio
- $ bundle install # instala el tema y sus dependencias
- $ bundle update # actualiza el tema y sus dependencias a su última versión
- $ jekyll build # construye el sitio básico, e importa a la carpeta _sites los generadores de contenido
- $ COMANDO # descomprime archivo zip que se encuentra en _site/assets y copiar contenido a main folder
- abre _config.yml en tu editor de texto y descomenta (borra "#") la línea "theme: morel-theme"
- $ jekyll build # reconstruye el sitio con el contenido agregado
- $ COMANDO # descomprime el archivo "env.zip", que se encuentra en la carpeta assets que acabamos de copiar a main folder

Ahora tienes un sitio listo *con el contenido de sample, del sitio MOREL Afro Latin American Writers in Translation (ALAWiT)*. Puedes correrlo localmente para probar con `$ bundle exec jekyll serve`. Para llenarlo con tu propio contenido de Zotero y los datos de tu sitio, sigue los siguientes pasos:

- abre _config.yml en tu editor de texto y:
  - asígnale el título a tu sitio
  - asígnale el tagline a tu sitio
  - asígnale datos de contacto y/o redes a tu sitio
  - asígnale el site description a tu sitio
  - asígnale el jotform link a tu sitio (crea tu cuenta gratuita en https://www.jotform.com/)
- Abre Zotero y exporta tu colección de Zotero como csv. Guárdalo en la carpeta assets/data. Nombra el archivo "books_zotero.csv". Revisa la [guía](#zotero-fields) para llenar las fichas de Zotero 100 % legibles para MOREL.
- $ cd assets/env/bin # ve a la carpeta para activar el ambiente Python
- $ source activate
- $ cd ../src # muévete a la carpeta donde están los scripts de Python
- $ python morel-generate # genera el contenido a partir de tu colección de Zotero
- $ bundle exec jekyll serve --livereload # activa el servidor local para navegar tu sitio!

## Instrucciones para instalar el tema como rep

- forkea el repositorio. Es decir, crea una copia en tu cuenta github.
- abre el terminal en el folder de tu computadora local donde trabajarás el sitio
- $ git clone [rep] # clona el repositorio
- $ cd morel-site-generator # te mueves a la carpeta del repositorio
- $ bundle install # instala el tema y sus dependencias
- $ bundle update # actualiza el tema y sus dependencias a su última versión

Ahora tienes un sitio listo *con el contenido de sample, del sitio MOREL Afro Latin American Writers in Translation (ALAWiT)*. Puedes correrlo localmente para probar con `$ bundle exec jekyll serve`. Para llenarlo con tu propio contenido de Zotero y los datos de tu sitio, sigue los siguientes pasos:

- $ jekyll build # importa a la carpeta _sites los generadores de contenido actualizados
- 
- abre _config.yml en tu editor de texto y:
  - asígnale el título a tu sitio
  - asígnale el tagline a tu sitio
  - asígnale datos de contacto y/o redes a tu sitio
  - asígnale el site description a tu sitio
  - asígnale el jotform link a tu sitio (crea tu cuenta gratuita en https://www.jotform.com/)
- Abre Zotero y exporta tu colección de Zotero como csv. Guárdalo en la carpeta assets/data. Nombra el archivo "books_zotero.csv". Revisa la [guía](#zotero-fields) para llenar las fichas de Zotero 100 % legibles para MOREL.
- $ cd assets/env/bin # ve a la carpeta para activar el ambiente Python
- $ source activate
- $ cd ../src # muévete a la carpeta donde están los scripts de Python
- $ python morel-generate # genera el contenido a partir de tu colección de Zotero
- $ bundle exec jekyll serve --livereload # activa el servidor local para navegar tu sitio!

## Instrucciones para actualizar el tema (usuario)

- correr bundle u
- correr Jekyll build [x]
- descomprimir el archivo "_/site/assets/env.zip", y sustituir la carpeta "env" que se encuentra en ./assets/ [x]
- activar ambiente de python, corriendo "source activate" en la carpeta "bin" [x]
- cd ../src
- ejecutar python morel-generate
- bundle exec jekyll serve

## Instrucciones para actualizar el tema (admin)